"""
Holds utility methods for building a block.
"""

from .block_element.block_element import BlockElement
from .composition_object.text_object import TextObject
from .layout_block.section_block import SectionBlock
from .block_element.image_element import ImageElement
from .layout_block.divider_block import DividerBlock


def get_checkmark(task_completed: bool) -> str:
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


def get_information_block(info_link: str, info_text: str) -> dict:
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


def get_text_block_with_accessory(text_object: TextObject, accessory: BlockElement) -> dict:
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


def get_text_block_with_image(text: str, image_url: str, alt_text: str) -> dict:
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
    return get_text_block_with_accessory(text_object=text_object, accessory=image_element)


def get_task_block(text: str, info_link: str, info_text: str) -> list:
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
        get_information_block(info_link=info_link, info_text=info_text)
    ]


def get_onboarding_block() -> list:
    """
    Constructs an onboarding block, which contains information on different channels and a link to the CodeDevils
    website.

    :return: The onboarding message block as a list.
    :rtype: list
    """

    block = [
        SectionBlock(text=TextObject(btype=TextObject.BTYPE_MARKDOWN,
                                     text="Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. C"
                                          "heck out some of the channels available here:\n\n*Channels:*")).render(),
        DividerBlock().render(),
        get_text_block_with_image(text="*Opportunities*\nLearn about exciting new job opportunities and internships"
                                       " from other members, and gain insight on how to succeed during interviews.",
                                  image_url="https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                                            "Ficons%2Feducation-340%2F100%2FTilda_Icons_1ed_cup-256.png",
                                  alt_text="Opportunities"),
        get_text_block_with_image(text="*Project Discussion*\nEver think about programming something real and "
                                       "usable with a team? Use this channel to join a project, discuss one, or "
                                       "even get one started.",
                                  image_url="https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                                            "Ficons%2Feducation-340%2F100%2FTilda_Icons_1ed_group-256.png",
                                  alt_text="Project Discussion"),
        get_text_block_with_image(text="*Random*\nPost literally anything that you want! College is too boring to "
                                       "be serious all the time, so brighten someone's day up with a random thought"
                                       " or funny meme.",
                                  image_url="https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                                            "Ficons%2Feducation-340%2F99%2FTilda_Icons_1ed_speaker-256.png",
                                  alt_text="Random"),
        DividerBlock().render(),
        get_text_block_with_image(text="*CodeDevils Website*\nDid you know that I'm powered by the CodeDevils "
                                       "website? The website is so much more than just a web page. It's a web "
                                       "application used to communicate with fellow members, register members to "
                                       "CodeDevils, and coordinate on projects.\n\nVisit the "
                                       "<https://www.codedevils.org|CodeDevils website> to learn more.",
                                  image_url="https://www.codedevils.org/static/home/img/favicon.png",
                                  alt_text="CodeDevils Website"),
        DividerBlock().render()
    ]
    print(f'{block}')
    return block
