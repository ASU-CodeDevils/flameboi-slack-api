from .block_element import BlockElement
from ..composition_object.option_object import OptionObject
from ..composition_object.option_group_object import OptionGroupObject
from ..composition_object.confirm_object import ConfirmObject


class OverflowElement(BlockElement):
    """
    This is like a cross between a button and a select menu - when a user clicks on this overflow button, they will be
    presented with a list of options to choose from. Unlike the select menu, there is no typeahead field, and the
    button always appears with an ellipsis ("…") rather than customisable text. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#overflow
    """

    def __init__(self, action_id: str, options: [OptionObject], confirm: ConfirmObject = None):
        # validate input
        if len(options) > 5 or len(options) < 2:
            raise AttributeError('Must have between 2 and 5 options (inclusive)')
        super().__init__(btype='overflow', action_id=action_id)
        self.options = options
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'action_id': self.action_id,
            'options': OptionGroupObject.expand_options_group(self.options),
        }

        if self.confirm:
            block.update({'confirm': self.confirm.render()})

        return block
