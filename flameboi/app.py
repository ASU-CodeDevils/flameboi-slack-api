from flameboi.common.flameboi import Flameboi
from flameboi.common.routing import Router
from flask import Flask, request, Response, jsonify
import json
import os

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Initialize a Web API client, Router and Slack Events adapter
theBot = Flameboi(app)

admin_client = theBot.getAdmin()
bot_client = theBot.getClient()

slack_events_adapter = theBot.getAdapter()
router = Router(theBot)


# ================ Team Join Event =============== #


@slack_events_adapter.on("team_join")
def onboarding_message(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """

    router.handle_team_join(payload)


# ============= Reaction Added Events ============= #


@slack_events_adapter.on("reaction_added")
def update_emoji(payload):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """

    router.handle_reaction_added(payload)


# =============== Pin Added Events ================ #


@slack_events_adapter.on("pin_added")
def update_pin(payload):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """

    router.handle_pin_added(payload)


# ============== Message Events ============= #


@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """

    router.handle_message(payload)


# ============== Member Join Events ============= #


@slack_events_adapter.on("member_joined_channel")
def member_joined(payload):
    """Display the channel welcome message after someone joins a channel.
    """

    router.handle_channel_join(payload)


# ============== App Mention Events ============= #


@slack_events_adapter.on("app_mention")
def mention(payload):
    """
    Triggers handler for when the bot received an @ mention event..
    """

    router.handle_app_mention(payload)


# ============== App Home Events ============= #


@slack_events_adapter.on("app_home_opened")
def home_open(payload):
    """
    Triggers handler for when the bot received an @ mention event..
    """

    router.handle_app_home(payload)


# ============== Other Endpoints ============= #


@app.route("/slash/", methods=["GET", "POST"])
def slashcommand():
    """
    Triggers handler for when the bot received slash command..
    """

    if request.method == "GET":
        return "These are not the slackbots you're looking for."

    elif request.method == "POST":

        if request.form.get("token") == os.getenv("VERIFICATION_TOKEN"):

            text = request.form.get("text")
            channel_id = request.form.get("channel_id")
            user_id = request.form.get("user_id")
            user_name = request.form.get("user_name")
            response_url = request.form.get("response_url")
            command = request.form.get("command")
            trigger_id = request.form.get("trigger_id")

            reply = (
                f"User ID: <@{user_id}>\n"
                f"User Name: {user_name}\n"
                f"Channel: <#{channel_id}>\n"
                f"Command: {command}\n"
                f"Text: {text}\n"
                f"Response URL: {response_url}\n"
                f"Trigger ID: {trigger_id}\n"
            )

            payload = {"text": reply, "response_type": "ephemeral"}

        return Response(
            response=json.dumps(payload), status=200, mimetype="application/json"
        )


# @app.route('/newuser')
# def addNewUser():
#     """
#     Triggers slackbot to add new user to CodeDevils Slack (secured by jwt) using
#     grid approved email
#     """
#     # TODO: JWT Secured endpoint for web to add user


if __name__ == "__main__":

    app.run(port=5000)
