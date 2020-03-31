import os
import logging
from flask import Flask
from flameboi import Flameboi


# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Initialize a Web API client and Slack Events adapter
theBot = Flameboi(app)
slack_web_client = theBot.getClient()
slack_events_adapter = theBot.getAdapter()

bot_id = 'U010N6U09T3'


# ================ Team Join Event =============== #

@slack_events_adapter.on("team_join")
def onboarding_message(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    event = payload.get("event", {})
    user_id = event.get("user", {}).get("id")

    assert theBot.send_onboarding_DM(user_id)["ok"]


# ============= Reaction Added Events ============= #

@slack_events_adapter.on("reaction_added")
def update_emoji(payload):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    event = payload.get("event", {})

    user_id = event.get('user')
    emoji = event.get('reaction')
    channel_id = event.get("item", {}).get("channel")
    ts = event.get("item", {}).get("ts")
    
    """
    TODO: Create function in flameboi.py that builds a reaction_add block
    """

    if user_id != bot_id:
        logger.info("Responding to reaction added.")

        response = slack_web_client.reactions_add(
            name=emoji,
            channel=channel_id,
            timestamp=ts
            )
        assert response["ok"]

   
# =============== Pin Added Events ================ #

@slack_events_adapter.on("pin_added")
def update_pin(payload):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    event = payload.get("event", {})

    channel_id = event.get("channel_id")
    user_id = event.get("user")


# ============== Message Events ============= #

@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})

    sub_type = event.get("subtype")
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    ts = event.get("ts")

    if text and text.lower() == "!test" and user_id != bot_id:
        logger.info("Responding to !test command")
        reply = "I'm here <@%s>! :tada:" % user_id
        
        response = slack_web_client.chat_postMessage(
            channel=channel_id,
            text=reply
            )
        assert response["ok"]


    """
    TODO: Expand on block kit builder base (which is awesome Kevin!)
    Below is example use of blacks using !onboard to send the onboarding block
    """
    
    if text and text.lower() == "!onboard" and user_id != bot_id:
        logger.info("Responding to !onboard command")
        
        assert theBot.send_onboarding_DM(user_id)["ok"]



# ============== App Mention Events ============= #

@slack_events_adapter.on("app_mention")
def mention(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})
    
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    event_ts = event.get("ts")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=5000)