import os
import ssl
import slack
import logging

from .config import load_config
from .block_kit_builder.block_generator import BlockGenerator


class FlameboiSlackApi:
    """
    Methods used to control various features with the Flameboi Slack bot API.
    """

    def __init__(self):
        logging.basicConfig(filename='slack.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        ssl_context = ssl.create_default_context(cafile=os.environ['WEBSOCKET_CLIENT_CA_BUNDLE'])

        self.config = load_config()
        self.messenger = BlockGenerator(self.config)
        self.bot_client = slack.WebClient(token=self.config['app_credentials']['oauth']['bot_user_access_token'],
                                          headers={'Accept': 'application/json'},
                                          ssl=ssl_context)
        self.user_client = slack.WebClient(token=self.config['app_credentials']['oauth']['access_token'],
                                           headers={'Accept': 'application/json'})

    def send_onboarding_message(self, user_email: str) -> dict:
        """
        Sends the onboarding message to a user.

        :param user_email: The email of the user to be on-boarded.
        :type user_email: str
        :return: The response from the message request as a dict.
        :rtype: dict
        """
        response = None
        try:
            user = self.get_user_by_email(email=user_email)['id']
            response = self.bot_client.conversations_open(users=[user])
            if not response['ok']:
                self._print_slack_error(response)

            channel = response['channel']['id']
            message = self.messenger.get_welcome_block(channel=channel)
            return self._send_block_message(message=message)

        except Exception as e:
            self._print_slack_error(response)
            raise Exception(f'Error sending onboarding message: {str(e)}')

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
        try:
            user = self.get_user_by_email(email=user_email)
            channel = self.get_channel_id(channel_name='hangout')
            response = self.user_client.channels_invite(channel=channel, user=user['id'])
            # response = self.bot_client.channels_invite(channel='#general', user=user['id'])

            if not response['ok']:
                self._print_slack_error(response)
            return response['message']
        except Exception as e:
            raise Exception(f'Failed to add user <ID: {id}> to workspace: {str(e)}')

    def get_slack_client(self):
        """
        Returns the slack web client. Used for if the commands in this module do not suffice for specific use cases.

        :return: The slack client.
        :rtype: slack.WebClient
        """
        return self.bot_client

    def get_user_by_email(self, email: str) -> dict:
        """
        Retrieves a user by their email.

        :param email: The email address of the user.
        :type email: str
        :return: The user as a dict.
        :rtype: dict
        """
        response = self.bot_client.users_lookupByEmail(email=email)
        if not response['ok']:
            self._print_slack_error(response)
        return response['user']

    def get_users_list(self) -> dict:
        """
        Returns a list of users.

        :return: A list of users. See https://api.slack.com/methods/users.list for format.
        :rtype: dict
        """
        try:
            response = self.bot_client.users_list()
            if response['ok']:
                return response['members']
            else:
                self._print_slack_error(response)
        except Exception as e:
            raise Exception(f'Failed to retrieve list of users from workspace: {str(e)}')

    def get_channel_id(self, channel_name: str) -> str:
        """
        Returns the channel ID based on the name. If no ID is found, then none is returned.

        :param channel_name: The name of the channel as a string (w/o the leading hashtag).
        :type channel_name: str
        :return: The channel id as a string.
        :rtype: str
        """
        try:
            channel_list = self.get_channel_list()
            for channel in channel_list:
                if channel['name'] == channel_name:
                    return channel['id']
        except Exception as e:
            raise Exception(f'Failed to obtain channel id: {str(e)}')

    def get_channel_list(self) -> dict:
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """
        try:
            response = self.bot_client.channels_list()
            if response['ok']:
                return response['channels']
            self._print_slack_error(response)
        except Exception as e:
            raise Exception(f'Failed to obtain channels list: {str(e)}')

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
        response = self.bot_client.chat_postMessage(**message)

        if not response['ok']:
            self._print_slack_error(response)
        return response['message']

    def _print_slack_error(self, response):
        """
        Prints a formatted slack API error message.

        :param response: The HTTP response object as a dict.
        :type response: Union[Future, SlackResponse]
        :return: None
        """
        if not response['ok']:
            logging.error(f'Error with Slack API: {response["error"]}\n')
            logging.error(f'Messages:\n')
            for message in response['response_metadata']['messages']:
                logging.error(f'\t{message}\n')

