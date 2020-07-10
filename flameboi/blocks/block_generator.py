import os
from datetime import datetime
from flameboi.blocks.block_element.block_element import BlockElement
from flameboi.blocks.composition_object.text_object import TextObject
from flameboi.blocks.layout_block.section_block import SectionBlock
from flameboi.blocks.block_element.image_element import ImageElement
# from flameboi.blocks.layout_block.divider_block import DividerBlock


class BlockGenerator:
    """
    Constructs block payloads that act as formatted messages for Slack. For more information on blocks, see
    https://api.slack.com/block-kit.
    """

    def __init__(self, channel=None):
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

    def get_message_payload(self, ts: datetime = None, text: str = None, channel: str = None, blocks: list = None,
                            view_type: str = None, link_names: int = 1) -> dict:
        """
        Returns a message block payload used to post messages in a specific channel.

        :param blocks: The blocks to be inserted into the message payload.
        :type blocks: list
        :param channel: channel_id
        :type channel: string
        :param ts: datetime
        :type ts: string
        :param text: channel_id
        :type text: string
        :param link_names: number of linke names, defaults to 1
        :type link_names: int
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

    def get_checkmark(self, task_completed: bool) -> str:
        """
        Returns a check mark emoji indicating the completed task status. If the task is complete, then a white check
        mark is returned. If not, an empty white square is.

        :param task_completed: Whether or not the task was complete.
        :type task_completed: bool
        :return: A checkmark emoji string based on whether or not the task was completed.
        :rtype: str
        """
        if task_completed:
            return ":white_check_mark:"
        return ":white_large_square:"

    def get_information_block(self, info_link: str, info_text: str) -> dict:
        """
        Returns an information block, which is a section with an info icon followed by linked text.

        :param info_link: The link the block redirects the user to.
        :type info_link: str
        :param info_text: The link text.
        :type info_text: str
        :return: A dict in the format of a context block.
        :rtype: dict
        """
        information = f':information_source: *<{info_link}|{info_text}>*'
        return TextObject(btype=TextObject.BTYPE_MARKDOWN, text=information).render()

    def get_text_block_with_accessory(self, text_object: TextObject, accessory: BlockElement) -> dict:
        """
        Returns a text block with an accessory.

        :param text_object: The text block object.
        :type text_object: TextObject
        :param accessory: The accessory object.
        :type accessory: LayoutBlock
        :return: The text block with an accessory layout block.
        :rtype: dict
        """
        return SectionBlock(text=text_object, accessory=accessory).render()

    def get_text_block_with_image(self, text: str, image_url: str, alt_text: str) -> dict:
        """
        Returns a text block with an image to the right of it.

        :param text: The text in the text block.
        :type text: str
        :param image_url: The URL to the image.
        :type image_url: str
        :param alt_text: Alternate text (appears on image hover).
        :type alt_text: str
        :return: The block as a dict.
        :rtype: dict
        """
        text_object = TextObject(btype=TextObject.BTYPE_MARKDOWN, text=text)
        image_element = ImageElement(image_url=image_url, alt_text=alt_text)
        return self.get_text_block_with_accessory(text_object=text_object, accessory=image_element)

    def get_task_block(self, text: str, info_link: str, info_text: str) -> list:
        """
        Returns a task block, which is comprised of a paragraph of text followed by an information link at the bottom.

        :param text: Markdown-supported text to display in the paragraph.
        :type text: str
        :param info_link: The link associated with the task block.
        :type info_link: str
        :param info_text: The link text.
        :type info_text: str
        :return: An array of blocks formatted for a block payload.
        :rtype: list
        """
        return [
            TextObject(btype=TextObject.BTYPE_MARKDOWN, text=text).render(),
            self.get_information_block(info_link=info_link, info_text=info_text)
        ]
