from flameboi.blocks.layout_block.layout_block import LayoutBlock
from flameboi.blocks.composition_object.text_object import TextObject


class ImageBlock(LayoutBlock):
    """
    A simple image block, designed to make those cat photos really pop. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#image
    """

    def __init__(self, image_url: str, alt_text: str, title: TextObject = None, block_id: str = None):
        # validate input
        self.validate_input('image_url', image_url, max_length=3000)
        self.validate_input('alt_text', alt_text, max_length=2000)
        if title:
            title.validate_text_block(max_length=200, required_type=TextObject.BTYPE_PLAIN_TEXT)

        # initialize the parent
        super().__init__(btype='image', block_id=block_id)

        # set values once validation has passed
        self.image_url = image_url
        self.alt_text = alt_text
        self.title = title

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'image_url': self.image_url,
            'alt_text': self.alt_text
        }

        # add optional fields if specified
        if self.title:
            block.update({'title': self.title.render()})
        if self.block_id:
            block.update({'block_id': self.block_id})

        return block
