from slack_blockkit.utils import get_text_block_with_image


def get_meeting_block() -> list:
    """
    Constructs a quote of the day block.

    :return: The quote of the day block as a list.
    :rtype: list
    """

    block = [
        get_text_block_with_image(
            text="*Meeting happening now!!!* Check #meetings for link!!!",
            image_url="https://media.tenor.com/images/40d4e9cbbf99578879815abc165ed5e9/tenor.gif",
            alt_text="Meeting!",
        )
    ]
    return block

