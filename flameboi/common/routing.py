import os
from flameboi.events.app_mention_event import App_Mention
from flameboi.events.channel_join_event import Channel_Join
from flameboi.events.message_event import Message_Event
from flameboi.events.pin_added_event import Pin_Added
from flameboi.events.reaction_added_event import Reaction_Added
from flameboi.events.slash_command import Slash_Command
from flameboi.events.team_join_event import Team_Join


class Router:
    """
    Methods used to router/direct events within the Flameboi Slack bot API.

    :return: The list of channels as a dict.
    :rtype: dict
    """  

    def __init__(self, bot_client: WebClient):
        self.bot = bot_client
        # Import various ID's for filtering via dotenv
        self.bot_id = os.getenv("BOT_ID")
        self.bot_user_id= os.getenv("USER_ID")
        self.bot_app_id = os.getenv("APP_ID")


    def handle_team_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """
        event = Team_Join(payload)


    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """    


    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """


    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """


    def handle_channel_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """


    def handle_app_mention(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """


    def handle_slash_command(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """