from flameboi.blocks.block import Block
from flameboi.blocks.composition_object.text_object import TextObject
from flameboi.blocks.composition_object.option_object import OptionObject


class OptionGroupObject(Block):
    """
    Provides a way to group options in a select menu or multi-select menu. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#option_group
    """

    def __init__(self, label: TextObject, options: list):
        # validate input
        label.validate_text_block(max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT)
        if not isinstance(options[0], OptionObject):
            raise AttributeError('options list needs to be a list of OptionObject objects')
        if len(options) > 100:
            raise AttributeError('options list cannot exceed 100 options')

        self.label = label
        self.options = options

    @staticmethod
    def expand_options_group(options: [OptionObject]) -> list:
        ret = []
        for option in options:
            ret.append(option.render())
        return ret

    def render(self) -> dict:
        return {
            'label': self.label.render(),
            'options': self.expand_options_group(self.options)
        }