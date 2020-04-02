import os
from flameboi.events.app_mention_event import AppMentionEvent
from flameboi.events.channel_join_event import ChannelJoinEvent
from flameboi.events.message_event import MessageEvent
from flameboi.events.pin_added_event import PinAddedEvent
from flameboi.events.reaction_added_event import ReactionAddedEvent
from flameboi.events.slash_command import SlashCommand
from flameboi.events.team_join_event import TeamJoinEvent


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


 # TODO: impplement this
    def handle_team_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """


 # TODO: impplement this
    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """    

 # TODO: impplement this
    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

 # TODO: impplement this
    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

 # TODO: impplement this
    def handle_channel_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

 # TODO: impplement this
    def handle_app_mention(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = AppMentionEvent(payload)

 # TODO: impplement this
    def handle_slash_command(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """