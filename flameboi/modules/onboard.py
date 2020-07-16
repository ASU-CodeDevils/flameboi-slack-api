from slack_blockkit.composition_object import TextObject
from slack_blockkit.layout_block import DividerBlock, SectionBlock
from slack_blockkit.utils import get_blocks, get_text_block_with_image


def get_onboarding_block() -> list:
    """
    Constructs an onboarding block, which contains information on different channels and a link to the CodeDevils
    website.

    :return: The onboarding message block as a list.
    :rtype: list
    """

    block = get_blocks(
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. C"
                    "heck out some of the channels available here:\n\n*Channels:*"
                ),
            )
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "*Careers - <#C3UQCFHS5>*\nLearn about exciting new job opportunities and internships"
                " from other members, and gain insight on how to succeed during interviews."
            ),
            image_url=(
                "https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                "Ficons%2Feducation-340%2F100%2FTilda_Icons_1ed_cup-256.png"
            ),
            alt_text="Careers",
        ),
        get_text_block_with_image(
            text=(
                "*Projects - <#C311NUV6C>*\nEver think about programming something real and "
                "usable with a team? Use this channel to join a project, discuss one, or "
                "even get one started."
            ),
            image_url=(
                "https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                "Ficons%2Feducation-340%2F100%2FTilda_Icons_1ed_group-256.png"
            ),
            alt_text="Projects",
        ),
        get_text_block_with_image(
            text=(
                "*Hangout - <#C2N5P84BD>*\nPost literally anything that you want! College is too boring to "
                "be serious all the time, so brighten someone's day up with a random thought"
                " or funny meme."
            ),
            image_url=(
                "https://slack-imgs.com/?c=1&url=https%3A%2F%2Fcdn0.iconfinder.com%2Fdata%2"
                "Ficons%2Feducation-340%2F99%2FTilda_Icons_1ed_speaker-256.png"
            ),
            alt_text="Hangout",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "*CodeDevils Website*\nDid you know that I'm powered by the CodeDevils "
                "website? The website is so much more than just a web page. It's a web "
                "application used to communicate with fellow members, register members to "
                "CodeDevils, and coordinate on projects.\n\nVisit the "
                "<https://www.codedevils.org|CodeDevils website> to learn more."
            ),
            image_url="https://www.codedevils.org/static/home/img/favicon.png",
            alt_text="CodeDevils Website",
        ),
        DividerBlock(),
    )
    return block


def get_sample_block() -> list:
    sample = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Danny Torrance left the following review for your property:",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in"
                " room 237 was far too rowdy, whole place felt stuck in the 1920s.",
            },
            "accessory": {
                "type": "image",
                "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
                "alt_text": "Haunted hotel image",
            },
        },
        {
            "type": "section",
            "fields": [{"type": "mrkdwn", "text": "*Average Rating*\n1.0"}],
        },
    ]

    return sample
