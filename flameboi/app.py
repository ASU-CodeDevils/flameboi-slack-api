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


bot_id = os.getenv("BOT_ID")
bot_user_id= os.getenv("USER_ID")
bot_app_id = os.getenv("APP_ID")

# ================ Team Join Event =============== #

@slack_events_adapter.on("team_join")
def onboarding_message(payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    event = payload.get("event", {})
    user_id = event.get("user", {}).get("id")
    logger.info("Received team joined event!")

    # assert theBot.send_onboarding_DM(user_id)["ok"]


# ============= Reaction Added Events ============= #

@slack_events_adapter.on("reaction_added")
def update_emoji(payload):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    logger.info("Received reaction added event!")

    event = payload.get("event", {})

    user_id = event.get('user')
    emoji = event.get('reaction')
    channel_id = event.get("item", {}).get("channel")
    ts = event.get("item", {}).get("ts")
    
    """
    TODO: Create function in flameboi.py that builds a reaction_add block if possible?
    """
    sub_type = event.get("subtype")

    if user_id != bot_user_id:
        logger.info("Responding to reaction added.")
        response = slack_web_client.reactions_add(
            name=emoji,
            channel=channel_id,
            timestamp=ts
            )
        assert response["ok"]
    else:
        logger.info("Reaction added was bots!")
        logger.info(sub_type)

   
# =============== Pin Added Events ================ #

@slack_events_adapter.on("pin_added")
def update_pin(payload):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    logger.info("Received pin added event!")

    event = payload.get("event", {})

    channel_id = event.get("channel_id")
    user_id = event.get("user")


# ============== Message Events ============= #

@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    logger.info("Received message event!")

    event = payload.get("event", {})

    sub_type = event.get("subtype")
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    ts = event.get("ts")

    if sub_type != 'bot_message':
        if text and text.lower() == "!test" :
            logger.info("Responding to !test command")
            reply = "I'm here <@%s>! :tada:" % user_id
                
            assert theBot.send_message(channel_id, reply)["ok"]

        """
        TODO: Expand on block kit builder base (which is awesome Kevin!)
        Below is example use of blocks using !onboard to send the onboarding block
        """
        
        if text and text.lower() == "!onboard":
            logger.info("Responding to !onboard command")
            
            assert theBot.send_onboarding_DM(user_id)["ok"]

        if text and text.lower() == "!qod":
            logger.info("Responding to !qod command")
            
            assert theBot.send_qod(channel_id)["ok"]


@slack_events_adapter.on("member_joined_channel")
def member_joined(payload):
    """Display the channel welcome message after someone joins a channel.
    """
    logger.info("Received member joined channel event!")

    event = payload.get("event", {})

    user_id = event.get("user")
    channel_id = event.get("channel")
    
    logger.info("Responding to member joined event")

    name = theBot.get_user_info(user_id)
    text = ":tada: Welcome to channel, %s!!! :tada:" % name['user']['real_name']
    
    assert theBot.send_message(channel_id, text)["ok"]

# ============== App Mention Events ============= #

@slack_events_adapter.on("app_mention")
def mention(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    logger.info("Received app mention event!")

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