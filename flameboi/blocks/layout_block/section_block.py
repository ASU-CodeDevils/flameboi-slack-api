from flameboi.blocks.layout_block.layout_block import LayoutBlock
from flameboi.blocks.composition_object.text_object import TextObject
from flameboi.blocks.block_element.block_element import BlockElement


class SectionBlock(LayoutBlock):
    """
    Basic section block. For more information, see: https://api.slack.com/reference/block-kit/blocks#section
    """

    def __init__(self, text: TextObject, block_id: str = None, fields: list = None, accessory: BlockElement = None):
        super().__init__(btype='section', block_id=block_id)

        # field validation
        # text can be no longer than 3000 characters
        if text.get_text_length() > 3000:
            raise AttributeError(f'text cannot be more than 3000 characters, but got {text.get_text_length()}')

        if block_id and len(block_id) > 255:
            raise AttributeError(f'block_id cannot be more than 255 characters, but got {len(block_id)}')

        self.text = text
        self.block_id = block_id
        self.fields = fields
        self.accessory = accessory

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'text': self.text.render(),
        }

        if self.block_id:
            block.update({'block_id': self.block_id})
        if self.fields:
            block.update({'fields': self.fields})
        if self.accessory:
            block.update({'accessory': self.accessory.render()})

        return block
