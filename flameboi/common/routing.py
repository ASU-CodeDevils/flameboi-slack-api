import os
import json
from flameboi.events.app_mention_event import AppMentionEvent
from flameboi.events.channel_join_event import ChannelJoinEvent
from flameboi.events.message_event import MessageEvent
from flameboi.events.pin_added_event import PinAddedEvent
from flameboi.events.reaction_added_event import ReactionAddedEvent
from flameboi.events.team_join_event import TeamJoinEvent
from flameboi.events.app_home_event import AppHomeEvent
# from flameboi.events.slash_command import SlashCommand


class Router:
    """
    Methods used to router/direct events within the Flameboi Slack bot API.

    :return: The list of channels as a dict.
    :rtype: dict
    """

    """
    TODO: instantiate a modrunner class that will run modules triggered
    """

    def __init__(self, bot_client):
        self.bot = bot_client

        # Import various ID's for filtering via dotenv
        self.bot_id = os.getenv("BOT_ID")
        self.bot_user_id = os.getenv("USER_ID")
        self.bot_app_id = os.getenv("APP_ID")

    # TODO: implement this
    def handle_team_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = TeamJoinEvent(payload)

    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = ReactionAddedEvent(payload)
        details = event.get_details()

        if details['user_id'] != self.bot_user_id:
            if details['reaction'] and details['reaction'] == "parrot":
                for i in range(1,10):
                    response = self.bot.reactions_add(
                        name=f"parrotwave{i}",
                        channel=details['channel_id'],
                        timestamp=details['ts'],
                    )
                    assert response["ok"]
            elif details['reaction'] and details['reaction'] == "fuckyouadmin":
                response = self.bot.reactions_add(
                    name="heart",
                    channel=details['item_channel'],
                    timestamp=details['item_ts'],
                )
                assert response["ok"]
            else:
                response = self.bot.reactions_add(
                    name=details['reaction'],
                    channel=details['channel_id'],
                    timestamp=details['ts'],
                )
                assert response["ok"]

    # TODO: implement this
    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = PinAddedEvent(payload)
        details = event.get_details()

        # reply = f"<@{details['user_id']}> seems to think something of importance happened in <@{details['channel_id']}>"

        # assert self.bot.chat_postMessage('C30L07P18', reply)["ok"]

    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = MessageEvent(payload)
        details = event.get_details()

        if details['sub_type'] != 'bot_message':
            
            """TODO: Address block builder issues.  Currently something is preventing Flameboi calls 
            involving the block kit builder. 
            """

            if details['text'] and details['text'].lower() == "!testthread":

                reply = f":tada: :partywizard: I'm here <@{details['user_id']}>! :partywizard: :tada:" 

                response = self.bot.chat_postMessage(
                    channel=details['channel_id'], 
                    text=reply,
                    thread_ts=details['ts'],
                )

                assert response["ok"]

            elif details['text'] and details['text'].lower() == "!test":

                reply = f":tada: :partywizard: I'm here <@{details['user_id']}>! :partywizard: :tada:" 

                response = self.bot.chat_postMessage(
                    channel=details['channel_id'], 
                    text=reply,
                )

                assert response["ok"]

            elif details['text'] and details['text'].lower() == "!testblock":

                response = self.bot.chat_postMessage(
                    channel=details['channel_id'],
                    text="testing...",
                    blocks=json.dumps(self.get_sample_block())
                )
                assert response["ok"]


            elif details['text'] and "party" in details['text'].lower() and ":partywizard:" not in details['text']:
                
                reply = ":partywizard:"

                assert self.bot.chat_postMessage(channel=details['channel_id'], text=reply)["ok"]

            elif details['text'] and details['text'].lower() == "!channel":

                name = self.bot.conversations_info(channel=details['channel_id'])
                
                usable = name.get('channel', {}).get('name')

                reply = f"Channel ID: {details['channel_id']}\nChannel Name: {usable}\nChannel Link: <#{details['channel_id']}>"

                response = self.bot.chat_postMessage(
                    channel=details['channel_id'], 
                    text=reply,
                )

                assert response["ok"]


            """
            TODO: Expand on block kit builder base (which is awesome Kevin!)
            Below is example use of blocks using !onboard to send the onboarding block
            """

            # if details['text'] and details['text'].lower() == "!onboard":
            #     assert self.bot.send_onboarding_DM(details['user_id'])["ok"]
            #
            # if details['text'] and details['text'].lower() == "!qod":
            #     assert self.bot.send_qod(details['channel_id'])["ok"]

    def handle_channel_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = ChannelJoinEvent(payload)
        details = event.get_details()

        # reply = f"Welcome to <@{details['channel_id']}>, <@{details['user_id']}>!!"

        # assert self.bot.chat_postMessage(details['channel_id'], reply)["ok"]

    def handle_app_mention(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = AppMentionEvent(payload)
        details = event.get_details()

        reply = f"You talking to me, <@{details['user_id']}>?!?"

        response = self.bot.chat_postMessage(
            channel=details['channel_id'],
            text=reply,
        )
        assert response["ok"]

    def get_sample_block(self) -> list:
        sample = [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Danny Torrence left the following review for your property:"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
                            "237 was far too rowdy, whole place felt stuck in the 1920s."
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
                            "alt_text": "Haunted hotel image"
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                            "type": "mrkdwn",
                            "text": "*Average Rating*\n1.0"
                            }
                        ]
                    }
                ]

        return sample  

    def handle_app_home(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = AppHomeEvent(payload)
        details = event.get_details()

       

    """
    TODO: Add endpoint for easy trigger of simple functions (like existing slash commands)
    """
    # def handle_slash_command(self, payload):
    #     """
    #     Returns the list of channels available to the bot.
    #
    #     :return: The list of channels as a dict.
    #     :rtype: dict
    #     """
