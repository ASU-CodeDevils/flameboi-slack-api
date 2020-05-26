from datetime import date

from .block_element import BlockElement
from ..composition_object.text_object import TextObject
from ..composition_object.confirm_object import ConfirmObject


class DatepickerElement(BlockElement):
    """
    An element which lets users easily select a date from a calendar style UI. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#datepicker
    """

    def __init__(self, action_id: str, placeholder: TextObject, initial_date: str = None,
                 confirm: ConfirmObject = None):
        # validate input
        placeholder.validate_text_block(max_length=150, required_type=TextObject.BTYPE_PLAIN_TEXT)

        # set date if not already set
        if not initial_date:
            initial_date = str(date.today())

        super().__init__(btype='datepicker', action_id=action_id)

        self.placeholder = placeholder
        self.initial_date = initial_date
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'action_id': self.action_id,
            'placeholder': self.placeholder.render(),
            'initial_date': self.initial_date
        }

        if self.confirm:
            block.update({'confirm': self.confirm.render()})

        return block
