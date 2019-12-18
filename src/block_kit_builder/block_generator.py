from datetime import datetime

from .block_util import *


class BlockGenerator:
    """
    Constructs block payloads that act as formatted messages for Slack. For more information on blocks, see
    https://api.slack.com/block-kit.
    """

    def __init__(self, config, channel=None):
        """
        Initializes the payload parameters to be sent with each message.

        :param config: The configuration as a dict.
        :type config: dict
        :param channel: The default channel. If not specified, it takes the default channel from the
            config, defaults to None
        :type channel: str, optional
        """
        self.channel = channel if channel else config['defaults']['channel']
        self.username = config['display_information']['username']
        self.icon_emoji = config['display_information']['icon_emoji']
        self.timestamp = str(datetime.now())

    def get_welcome_block(self, channel: str) -> dict:
        """
        Sends the welcome message to the user.

        :param channel: The channel ID of the user as a string.
        :type channel: str
        :return: The response from the message payload.
        :rtype: dict
        """
        self.channel = channel
        return self.get_message_payload(blocks=get_onboarding_block())

    def get_message_payload(self, blocks: list, view_type: str = None) -> dict:
        """
        Returns a message block payload used to post messages in a specific channel.

        :param blocks: The blocks to be inserted into the message payload.
        :type blocks: list
        :param view_type: Used to determine the type of block for a view publish,
            defaults to None
        :type view_type: str, optional
        :return: The message payload as a dict.
        :rtype: dict
        """
        payload = {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": blocks
        }

        if view_type:
            payload.update({'type': view_type})

        return payload
