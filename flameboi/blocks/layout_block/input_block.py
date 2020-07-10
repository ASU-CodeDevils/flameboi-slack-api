from flameboi.blocks.layout_block.layout_block import LayoutBlock
from flameboi.blocks.composition_object.text_object import TextObject
from flameboi.blocks.block_element.block_element import BlockElement


class InputBlock(LayoutBlock):
    """
    A block that collects information from users - it can hold a plain-text input element, a select menu element,
    a multi-select menu element, or a datepicker. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#input
    """

    def __init__(self, label: TextObject, element: BlockElement, block_id: str = None, hint: TextObject = None,
                 optional: bool = False):
        # validate input
        label.validate_text_block(max_length=2000, required_type=TextObject.BTYPE_PLAIN_TEXT)
        if hint:
            hint.validate_text_block(max_length=2000, required_type=TextObject.BTYPE_PLAIN_TEXT)

        super().__init__(btype='input', block_id=block_id)

        self.label = label
        self.element = element
        self.hint = hint
        self.optional = optional

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'label': self.label,
            'element': self.element,
            'optional': self.optional
        }

        if self.block_id:
            block.update({'block_id', self.block_id})
        if self.hint:
            block.update({'hint': self.hint})

        return block
