import os
from dotenv import load_dotenv
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from ..blocks.block_generator import BlockGenerator


class Flameboi:
    """
    Methods used to control various features with the Flameboi Slack bot API.

        Args:
            app (Flask obj): the Flask object being used.  Initiated in app.py
            SLACK_SIGNING_SECRET (str): Signing secret stored in dotenv file in the /src directory.  See 
                server_configs/dotenvsample.txt for layout.
            SLACK_BOT_TOKEN (str): Bot User Token secret stored in dotenv file in the /src directory.  See 
                server_configs/dotenvsample.txt for layout.
    """

    def __init__(self, app):
        load_dotenv()
        self.signing_secret = os.getenv("SLACK_SIGNING_SECRET")
        self.bot_token = os.getenv("SLACK_BOT_TOKEN")

        self.blockGen = BlockGenerator()
        self.bot_client = WebClient(token=self.bot_token)
        self.event_adapter = SlackEventAdapter(self.signing_secret, "/", app)

    def getClient(self) -> WebClient:
        """
        Returns the slack web_client.

        :return: The slack client.
        :rtype: slack.WebClient
        """
        return self.bot_client

    def getAdapter(self) -> SlackEventAdapter:
        """
        Returns the slack event adapter.

        :return: The slack client.
        :rtype: slack.WebClient
        """
        return self.event_adapter

    def add_member(self, user_email: str) -> dict:
        """
        This method does not work yet. Enterprise grid access is required for the app to be able to add/remove users
        from the team.

        Adds a member to the workspace using their member ID.

        :param user_email: The Slack ID of the user.
        :type user_email: str
        :return: The response of the member addition request.
        :rtype: dict
        """
        user = self.get_user_by_email(email=user_email)['user']
        channel = self.get_channel_id(channel_name='hangout')
        return self.user_client.channels_invite(channel=channel, user=user['id'])

    def get_user_by_email(self, email: str) -> dict:
        """
        Retrieves a user by their email.

        :param email: The email address of the user.
        :type email: str
        :return: The user as a dict.
        :rtype: dict
        """
        return self.bot_client.users_lookupByEmail(email=email)

    def get_users_list(self) -> dict:
        """
        Returns a list of users.

        :return: A list of users. See https://api.slack.com/methods/users.list for format.
        :rtype: dict
        """
        return self.bot_client.users_list()

    def get_channel_id(self, channel_name: str) -> str:
        """
        Returns the channel ID based on the name. If no ID is found, then none is returned.

        :param channel_name: The name of the channel as a string (w/o the leading hashtag).
        :type channel_name: str
        :return: The channel id as a string.
        :rtype: str
        """
        channel_list = self.get_channel_list()
        for channel in channel_list:
            if channel['name'] == channel_name:
                return channel['id']

        return str(None)

    def get_user_info(self, user_id: str) -> dict:
        """
        Returns the information about the user, identified by user_id.

        :param user_id: The ID of the user as a string (w/o the leading @).
        :return: The user's info as a dict.
        :rtype: dict
        """
        return self.bot_client.users_info(user=user_id)

    def get_channel_list(self) -> dict:
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """
        return self.bot_client.channels_list()

    def send_message(self, channel: str, text: str, mention_email: str = None) -> dict:
        """
        Sends a message (either text or block) to a channel. An optional mention can be added to the beginning of the
        message.

        :param channel: The name of the channel to send the message to.
        :type channel: str
        :param text: The message to send.
        :type text: str
        :param mention_email: The email of the user to mention, default is None.
        :type mention_email: str
        :return: The result of sending the message.
        """

        if mention_email:
            username = self.get_user_by_email(mention_email)['user']['name']
            text = '@{} {}'.format(username, text)
        message = self.blockGen.get_message_payload(text=text, channel=channel)
        return self._send_block_message(message=message)

    def _send_block_message(self, message: dict, user_id: int = 0) -> dict:
        """
        Block message util to send a message using the bot client.

        :param message: Markdown-supported message to be sent.
        :type message: dict
        :param user_id: The user ID (if any) of the user the message was sent to.
        :type user_id: int, optional
        :return: The response from sending the message as a dict.
        :rtype: dict
        """
        return self.bot_client.chat_postMessage(**message)
