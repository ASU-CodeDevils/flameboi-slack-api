'''
TODO: implement this using the newly modular setup
'''

from flameboi.blocks.block_generator import BlockGenerator

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

def send_onboarding_message(self, user_email: str) -> dict:
    """
    Sends the onboarding message to a user.

    :param user_email: The email of the user to be on-boarded.
    :type user_email: str
    :return: The response from the message request as a dict.
    :rtype: dict
    """
    user = self.get_user_by_email(email=user_email)['user']['id']
    response = self.bot_client.conversations_open(users=[user])
    if not response['ok']:
        return response

    channel = response['channel']['id']
    message = self.messenger.get_welcome_block(channel=channel)
    return self._send_block_message(message=message)


def send_onboarding_DM(self, user_id: str) -> dict:
    """
    Sends the onboarding message to a user.

    :param user_id: The slack ID of the user to be on-boarded.
    :type user_id: str
    :return: The response from the message request as a dict.
    :rtype: dict
    """
    response = self.bot_client.conversations_open(users=[user_id])
    if not response['ok']:
        return response

    channel = response['channel']['id']
    message = self.messenger.get_welcome_block(channel=channel)
    return self._send_block_message(message=message)

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