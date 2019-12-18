from .block_element import BlockElement


class ImageElement(BlockElement):
    """
    An element to insert an image as part of a larger block of content. If you want a block with only an image in it,
    you're looking for the image block. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#image
    """

    def __init__(self, image_url: str, alt_text: str):
        super().__init__(btype='image')
        self.image_url = image_url
        self.alt_text = alt_text

    def render(self) -> dict:
        return {
            'type': self.btype,
            'image_url': self.image_url,
            'alt_text': self.alt_text
        }
