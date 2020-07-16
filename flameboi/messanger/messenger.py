# TODO: Split off messaging/posting/chatting functions to a Messenger class... keep the admin stuff in Flameboi


def send_message(
    self, channel: str, text: str, mention_email: str = None, mention_name: str = None,
) -> dict:
    """
    Sends a message (either text or block) to a channel. An optional mention can be added to the beginning of
    the message.

    :param channel: The name of the channel to send the message to.
    :type channel: str
    :param text: The message to send.
    :type text: str
    :param mention_email: The email of the user to mention, default is None.
    :type mention_email: str
    :return: The result of sending the message.
    """

    if mention_email:
        username = self.get_user_by_email(mention_email)["user"]["name"]
        text = f"@{username} {text}"
    elif mention_name:
        username = "<@{mention_name}>"
        text = f"{username} {text}"
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
    user = self.get_user_by_email(email=user_email)["user"]["id"]
    response = self.bot_client.conversations_open(users=[user])
    if not response["ok"]:
        return response

    channel = response["channel"]["id"]
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
    if not response["ok"]:
        return response

    channel = response["channel"]["id"]
    message = self.messenger.get_welcome_block(channel=channel)
    return self._send_block_message(message=message)
