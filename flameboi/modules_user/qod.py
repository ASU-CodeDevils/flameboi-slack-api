"""
TODO: implement this using the newly modular setup... create QOD class and import it in the message_event.py files
"""

import requests
from slack_blockkit.utils import get_text_block_with_image


def getQOD() -> list:

    output = []

    url = "https://quotes.rest/qod"
    api_token = "YOUR API KEY HERE"
    headers = {
        "content-type": "application/json",
        "X-TheySaidSo-Api-Secret": format(api_token),
    }

    response = requests.get(url, headers=headers)
    # print(response)
    output.append(response.json()["contents"]["quotes"][0]["quote"])
    output.append(response.json()["contents"]["quotes"][0]["author"])

    return output


# def get_quote(self, channel: str) -> dict:
#     """
#     Send a quote of the day to the specified channel.

#     :param channel: The channel ID as a string.
#     :type channel: str
#     :return: The response from the message payload.
#     :rtype: dict
#     """
#     self.channel = channel
#     return self.get_message_payload(blocks=get_qod_block())


# def send_qod(self, channel_id) -> dict:
#     """
#     Sends the quote of the day to specified channel.

#     :param channel_id: The channel ID.
#     :type channel_id: str
#     :return: The response from the message request as a dict.
#     :rtype: dict
#     """
#     message = self.messenger.get_quote(channel=channel_id)
#     return self._send_block_message(message=message)


def get_qod_block() -> list:
    """
    Constructs a quote of the day block.

    :return: The quote of the day block as a list.
    :rtype: list
    """

    quote = getQOD()

    block = [
        get_text_block_with_image(
            text=f"*Quote of the Day*\n{quote[0]}\n\t~~{quote[1]}~~",
            image_url="https://media.giphy.com/media/3og0IMJcSI8p6hYQXS/giphy.gif",
            alt_text="QOD",
        )
    ]
    return block
