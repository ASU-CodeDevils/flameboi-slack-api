import os
from flameboi.events import *

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