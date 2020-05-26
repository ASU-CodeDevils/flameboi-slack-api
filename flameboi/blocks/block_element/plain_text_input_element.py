from .block_element import BlockElement
from ..composition_object.text_object import TextObject


class PlainTextInputElement(BlockElement):
    """
    A plain-text input, similar to the HTML <input> tag, creates a field where a user can enter freeform data. It can
    appear as a single-line field or a larger textarea using the multiline flag. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#input
    """

    def __init__(self, action_id: str, placeholder: TextObject = None, initial_value: str = None,
                 multiline: bool = False, min_length: int = 0, max_length: int = 0):
        # validate input
        if placeholder:
            placeholder.validate_text_block(max_length=150, required_type=TextObject.BTYPE_PLAIN_TEXT)

        if min_length != 0 or max_length != 0:
            if min_length > max_length:
                raise AttributeError(f'max_length ({max_length}) must be greater than min_length ({min_length})')
            if min_length < 0 or min_length > 3000:
                raise AttributeError(f'min_length ({min_length}) must be between 0 and 3000 (inclusive)')
            if max_length < 0 or max_length > 3000:
                raise AttributeError(f'max_length ({max_length}) must be between 0 and 3000 (inclusive)')

        super().__init__(btype='plain_text_input', action_id=action_id)

        self.placeholder = placeholder
        self.initial_value = initial_value
        self.multiline = multiline
        self.min_length = min_length
        self.max_length = max_length

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'action_id': self.action_id,
            'multiline': self.multiline
        }

        if self.placeholder:
            block.update({'placeholder': self.placeholder.render()})
        if self.initial_value:
            block.update({'initial_value': self.initial_value})
        if self.min_length != 0:
            block.update({'min_length': self.min_length})
        if self.max_length != 0:
            block.update({'max_length': self.max_length})

        return block
