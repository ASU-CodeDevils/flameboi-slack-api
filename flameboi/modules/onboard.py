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

    hacker_rank_current_url = "http://www.hackerrank.com/codedevils-summer-2020"

    block = get_blocks(
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. "
                    "\n\n*Some of the channels to explore:*"
                ),
            )
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "*<#C2N5P84BD>*\nPost literally anything that you want! College is too boring to "
                "be serious all the time, so brighten someone's day up with a random thought"
                " or funny meme."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_85ui-128.png"
            ),
            alt_text="Hangout",
        ),
        get_text_block_with_image(
            text=(
                "*<#CMGU8033K>*\n Take a minute to introduce yourself here.  Tells us about yourself,"
                " what you're looking to get out of your time at ASU, the program you're in, or something"
                " that interests you outside of your academic life!"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_67ui-256.png"
            ),
            alt_text="Intro",
        ),
        get_text_block_with_image(
            text=(
                "*<#C3UQCFHS5>*\nLearn about exciting new job opportunities and internships"
                " from other members, and gain insight on how to succeed during interviews."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_49ui-128.png"
            ),
            alt_text="Careers",
        ),
        get_text_block_with_image(
            text=(
                "*<#C46E4B24Q>*\nTake part in our "
                f"<{hacker_rank_current_url}|HackerRank> challenges to improve your skills and compete to win "
                "CodeDevil's swag!  We hold a new contest each term, jump in and get yourself a CodeDevils Tee!"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_69ui-256.png"
            ),
            alt_text="Coding Challenges",
        ),
        get_text_block_with_image(
            text=(
                "*<#C311NUV6C>* and *<#C0111TQ05ML>*\nEver think about programming something"
                " real and usable with a team? Need help with something you're working on?  These channels to join"
                " a project, discuss a problem, or even get something started."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_8ui-256.png"
            ),
            alt_text="Projects and Debugging",
        ),
        get_text_block_with_image(
            text=(
                "*<#C010TCLHME2>*\nTake some time away from studying and play some games with your fellow "
                " CodeDevils!  Here you can find some people to team up with or team up against!"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_53ui-256.png"
            ),
            alt_text="Games",
        ),
        get_text_block_with_image(
            text=(
                "*<#CT06NE2AV>*\nTake part in CodeDevils club meetings.  We hold/post"
                " Virtual Study Halls, Organization meetings, etc here.  These are usually zoom based."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/ui-essence/32/_77ui-256.png"
            ),
            alt_text="Meetings",
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
