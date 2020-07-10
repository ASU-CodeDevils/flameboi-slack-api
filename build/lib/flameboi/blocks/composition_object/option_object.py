from flameboi.blocks.block import Block
from flameboi.blocks.composition_object.text_object import TextObject


class OptionObject(Block):
    """
    An object that represents a single selectable item in a select menu, multi-select menu, radio button group,
    or overflow menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option
    """

    def __init__(self, text: TextObject, value: str, url: str = None):
        # validate input
        text.validate_text_block(max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT)
        self.validate_input('value', value, max_length=75)
        self.validate_input('url', url, max_length=3000)

        self.text = text
        self.value = value
        self.url = url

    def render(self) -> dict:
        block = {
            'text': self.text.render(),
            'value': self.value
        }

        if self.url:
            block.update({'url': self.url})

        return block
