import os
from dotenv import load_dotenv
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
        self.channel = channel if channel else os.getenv("DEFAULT_CHANNEL")
        self.username = os.getenv("USERNAME")
        self.icon_emoji = os.getenv("ICON_EMOJI")
        self.icon_url = os.getenv("ICON_URL")

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

    def get_message_payload(self, ts: datetime = None, text: str = None, channel: str = None, blocks: list = None,
                            view_type: str = None, link_names: int = 1) -> dict:
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
            "ts": str(ts if ts else datetime.now()),
            "channel": channel if channel else self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "icon_url": self.icon_url,
        }
        payload.update({'text': text}) if text else payload.update({'blocks': blocks})
        payload.update({'link_names': link_names}) if link_names == 1 else payload.update({'link_names': 0})

        if view_type:
            payload.update({'type': view_type})

        return payload
