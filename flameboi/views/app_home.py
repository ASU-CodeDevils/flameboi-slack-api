import json
from flameboi.common.flameboi import Flameboi

# from slack_blockkit.block_element import ButtonElement
from slack_blockkit.composition_object import TextObject
from slack_blockkit.layout_block import DividerBlock, SectionBlock, ActionsBlock
from slack_blockkit.utils import get_blocks, get_text_block_with_image


def publish_init_home(user_id: str, theBot: Flameboi):
    """
    Publishes an initial app home view to the specified user and sets the external id
    as the {user_id}_home.

    :return: None.
    """
    response = theBot.bot_client.views_publish(
        user_id=user_id,
        view=json.dumps(
            {
                "type": "home",
                "title": {"type": "plain_text", "text": "Welcome!"},
                "blocks": _get_about_block(),
                "external_id": f"{user_id}_home",
            },
        ),
    )

    assert response["ok"]


def choose_home_view(action: str, user: str, theBot: Flameboi):
    """
    Updates an app home view to the specified external id.  Determined by the 
    Action identified by the button as passed by argument.

    :return: None.
    """
    if action == "About":
        response = theBot.bot_client.views_update(
            view=json.dumps(
                {
                    "type": "home",
                    "title": {"type": "plain_text", "text": "Welcome!"},
                    "blocks": _get_about_block(),
                    "external_id": f"{user}_home",
                },
            ),
            external_id=f"{user}_home",
        )
        assert response["ok"]

    elif action == "Contact":

        response = theBot.bot_client.views_update(
            view=json.dumps(
                {
                    "type": "home",
                    "title": {"type": "plain_text", "text": "Welcome!"},
                    "blocks": _get_contact_block(),
                    "external_id": f"{user}_home",
                },
            ),
            external_id=f"{user}_home",
        )
        assert response["ok"]

    elif action == "Channels":

        response = theBot.bot_client.views_update(
            view=json.dumps(
                {
                    "type": "home",
                    "title": {"type": "plain_text", "text": "Welcome!"},
                    "blocks": _get_channels_block(),
                    "external_id": f"{user}_home",
                },
            ),
            external_id=f"{user}_home",
        )

        assert response["ok"]


def _get_home_buttons() -> ActionsBlock:
    """
    Constructs a block, which contains buttons for easy navigation on flameboi home tab.

    :return: ActionBlock containing 4 ButtonElements.
    :rtype: ActionBlock
    """
    return ActionsBlock(
        elements=[
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "About", "emoji": True,},
                "action_id": "About",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Leadership", "emoji": True,},
                "action_id": "Contact",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Channels", "emoji": True,},
                "action_id": "Channels",
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "CodeDevils Website",
                    "emoji": True,
                },
                "action_id": "Link",
                "url": "https://www.codedevils.org",
            },
        ],
    )


def _get_about_block() -> list:
    """
    Constructs a block, which contains information on and  links to the CodeDevils
    website.

    :return: The about message block as a list.
    :rtype: list
    """

    block = get_blocks(
        ActionsBlock(
            elements=[
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "About", "emoji": True,},
                    "action_id": "About",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Leadership",
                        "emoji": True,
                    },
                    "action_id": "Contact",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Channels", "emoji": True,},
                    "action_id": "Channels",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "CodeDevils Website",
                        "emoji": True,
                    },
                    "action_id": "Link",
                    "url": "https://www.codedevils.org",
                },
            ],
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. "
                    "\n\n*A little about us:*"
                ),
            ),
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "\n\n*Rules:*"
                "\n\n\t- All of <https://eoss.asu.edu/dos/srr/codeofconduct|"
                "ASU's Code of Conduct> applies!"
                "\n\t- Be nice!"
                "\n\t- Be professional!"
                "\n\t- Be postin' in the correct channels!\n"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/media-flat-2/58/012_-_Settings-512.png"
            ),
            alt_text="Rules",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "\n\n*Good Info:*"
                "\n\nGeneral Body Meetings (GBMs) are open to all members and are held every other Monday, "
                "at 6pm AZ time (except during summer) via Slack video conference in #meetings."
                "\n\nPertinent news and reminders are posted in #announcements, be sure to check!"
                "\n\nAdd the <https://calendar.google.com/calendar/b/2?cid=Y29kZWRldm"
                "lscy5pbmZvQGdtYWlsLmNvbQ|calendar> to your own so you don't miss anything!"
                "\n\nWe’ve recently reorganized the Slack, cutting down a lot of bloat. "
                "New members have been automatically added to each channel, but if "
                "you’re a veteran member you may have to join the channels manually.\n"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/media-flat-2/58/001_-_play-512.png"
            ),
            alt_text="Info",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "\n\n*Get Involved:*"
                "\n\nYou’re a part of CodeDevils, take advantage of it!\n"
                "\n\nCodeDevils is a real club, with real memberships and perks. If you haven’t already, "
                "<https://asu.campuslabs.com/engage/organization/codedevils|register> on SunDevil Sync. This helps us with "
                "accurate headcounting, which can be used to justify funding from ASU for fun things.\n"
                "\n\nCheck out various channels with the button above!\n"
                "\n\nCheckout the CodeDevils \n"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/media-flat-2/58/007_-_Record-512.png"
            ),
            alt_text="Get Involved",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=("\n<https://github.com/ASU-CodeDevils|GitHub>\n"),
            image_url=(
                "https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_github_2-512.png"
            ),
            alt_text="Twitter",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=("\n<https://twitter.com/code_devils|Twitter>\n"),
            image_url=(
                "https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_twitter-512.png"
            ),
            alt_text="Twitter",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=("\n<https://www.instagram.com/code.devils/|Instagram>\n"),
            image_url=(
                "https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_instagram-512.png"
            ),
            alt_text="Instagram",
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=("\n<https://www.facebook.com/codedevils.asu|Facebook>\n"),
            image_url=(
                "https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_facebook-512.png"
            ),
            alt_text="Facebook",
        ),
    )
    return block


def _get_contact_block() -> list:
    """
    Constructs an contacts block, which contains information on the leadership of CodeDevils
    website.

    :return: The contacts message block as a list.
    :rtype: list
    """

    block = get_blocks(
        ActionsBlock(
            elements=[
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "About", "emoji": True,},
                    "action_id": "About",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Leadership",
                        "emoji": True,
                    },
                    "action_id": "Contact",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Channels", "emoji": True,},
                    "action_id": "Channels",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "CodeDevils Website",
                        "emoji": True,
                    },
                    "action_id": "Link",
                    "url": "https://www.codedevils.org",
                },
            ],
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. "
                    "\n\n*Our Leadership:*"
                ),
            ),
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "If you have questions or concerns, send an email to info@codedevils.org or reach out "
                    "to any CodeDevils leadership on Slack or email:"
                ),
            ),
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nPresident:"
                    "\n\tDavid Welborn\n\t\tEmail: dswelbor@asu.edu\n\t\tSlack: @dswelbor"
                ),
            ),
        ),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nVice President:"
                    "\n\tJeremy Doubleday\n\t\tEmail: jwdouble@asu.edu\n\t\tSlack: @jwdouble"
                ),
            ),
        ),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nTreasurer:"
                    "\n\tPierson Brannan\n\t\tEmail: pbrannan@asu.edu\n\t\tSlack: @pbrannan "
                ),
            ),
        ),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nSecretary:"
                    "\n\tJerry Naylor\n\t\tEmail: jnaylor3@asu.edu\n\t\tSlack: @jnaylor3"
                ),
            ),
        ),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nWebmasters:"
                    "\n\tTia Peruzzi\n\t\tEmail: vperuzzi@asu.edu\n\t\tSlack: @vperuzzi"
                    "\n\tJoe Reynolds\n\t\tEmail: jcreyno5@asu.edu\n\t\tSlack: @jcreyno5"
                    "\n\tJacob Lebrec\n\t\tEmail: jlabrec@asu.edu\n\t\tSlack: @jlabrec"
                ),
            ),
        ),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "\nStaff Advisor (ASU Professor):"
                    "\n\tRuben Acuna \n\t\tEmail: racuna1@asu.edu\n\t\tSlack:@racuna1"
                ),
            ),
        ),
    )
    return block


def _get_channels_block() -> list:
    """
    Constructs an onboarding block, which contains information on different channels and a link to the CodeDevils
    website.

    :return: The onboarding message block as a list.
    :rtype: list
    """

    hacker_rank_current_url = "https://www.hackerrank.com/codedevils-fall-challenge"

    block = get_blocks(
        ActionsBlock(
            elements=[
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "About", "emoji": True,},
                    "action_id": "About",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Leadership",
                        "emoji": True,
                    },
                    "action_id": "Contact",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Channels", "emoji": True,},
                    "action_id": "Channels",
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "CodeDevils Website",
                        "emoji": True,
                    },
                    "action_id": "Link",
                    "url": "https://www.codedevils.org",
                },
            ],
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Welcome to *CodeDevils*! I'm Flameboi, and I'll help you get settled. "
                    "\n\n*Some of the channels to explore:*"
                ),
            ),
        ),
        DividerBlock(),
        get_text_block_with_image(
            text=(
                "*<#C2N5P84BD>*\nPost literally anything that you want! College is too boring to "
                "be serious all the time, so brighten someone's day up with a random thought"
                " or funny meme."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Messages-512.png"
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
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Books-512.png"
            ),
            alt_text="Intro",
        ),
        get_text_block_with_image(
            text=(
                "*<#C3UQCFHS5>*\nLearn about exciting new job opportunities and internships"
                " from other members, and gain insight on how to succeed during interviews."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Stock-512.png"
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
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Settings-512.png"
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
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Store-512.png"
            ),
            alt_text="Projects and Debugging",
        ),
        get_text_block_with_image(
            text=(
                "*<#C010TCLHME2>*\nTake some time away from studying and play some games with your fellow "
                " CodeDevils!  Here you can find some people to team up with or team up against!"
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_iTunes-512.png"
            ),
            alt_text="Games",
        ),
        get_text_block_with_image(
            text=(
                "*<#CT06NE2AV>*\nTake part in CodeDevils club meetings.  We hold/post"
                " Virtual Study Halls (usually 12-5pm AZ on Saturdays), club  meetings, etc here."
                " These are usually zoom based."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Whatsapp-512.png"
            ),
            alt_text="Meetings",
        ),
        get_text_block_with_image(
            text=(
                "*<#C30L07P18>*\nImportant announcements relating to the CodeDevils Club or "
                "ASU student body can be found here.  Posts can include things such as virtual "
                "study hall or club meetings links, important updates, cancelations, etc."
            ),
            image_url=(
                "https://cdn0.iconfinder.com/data/icons/apple-apps/100/Apple_Note-512.png"
            ),
            alt_text="Announcements",
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
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(
                    "Icons provided by <https://www.iconfinder.com/|IconFinder> under the "
                    "<https://creativecommons.org/licenses/by-nc/3.0/legalcode|Creative Commons "
                    "NonCommercial License v3.0>"
                ),
            ),
        ),
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
