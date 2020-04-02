import logging
import os
from ..events.app_mention_event import AppMentionEvent
from ..events.channel_join_event import ChannelJoinEvent
from ..events.message_event import MessageEvent
from ..events.pin_added_event import PinAddedEvent
from ..events.reaction_added_event import ReactionAddedEvent
from ..events.slash_command import SlashCommand
from ..events.team_join_event import TeamJoinEvent


class Router:
    """
    Methods used to router/direct events within the Flameboi Slack bot API.

    :return: The list of channels as a dict.
    :rtype: dict
    """  

    def __init__(self, bot_client):
        self.bot = bot_client
        self.logger = logging.getLogger()
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

        event = TeamJoinEvent(payload)


 # TODO: impplement this
    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = ReactionAddedEvent(payload)
        details = event.get_details()

        if details['user_id'] != self.bot_user_id:
            self.logger.info("Responding to reaction added...")
            reponse = self.bot.reactions_add(
                name=details['reaction'],
                channel=details['channel_id'],
                timestamp=details['ts']
            )
        else:
            self.logger.info("Reaction added was the bot's!")


 # TODO: impplement this
    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = PinAddedEvent(payload)

 # TODO: impplement this
    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = MessageEvent(payload)

 # TODO: impplement this
    def handle_channel_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = ChannelJoinEvent(payload)

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