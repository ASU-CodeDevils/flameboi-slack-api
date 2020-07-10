from .block_element import BlockElement
from ..composition_object.option_object import OptionObject
from ..composition_object.option_group_object import OptionGroupObject
from ..composition_object.confirm_object import ConfirmObject


class RadioButtonGroupElement(BlockElement):
    """
    A radio button group that allows a user to choose one item from a list of possible options. For more information,
    see: https://api.slack.com/reference/block-kit/block-elements#radio
    """

    def __init__(self, action_id: str, options: [OptionObject], intitial_option: OptionObject = None,
                 confirm: ConfirmObject = None):
        # validate input
        if intitial_option and intitial_option not in options:
            raise AttributeError('initial_option must be an option within options')
        super().__init__(btype='radio_buttons', action_id=action_id)

        self.options = options
        self.initial_option = intitial_option
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'action_id': self.action_id,
            'options': OptionGroupObject.expand_options_group(self.options)
        }

        if self.initial_option:
            block.update({'initial_option': self.initial_option.render()})
        if self.confirm:
            block.update({'confirm': self.confirm.render()})

        return block
