from .block_element import BlockElement
from ..composition_object.text_object import TextObject
from ..composition_object.confirm_object import ConfirmObject


class ButtonElement(BlockElement):
    STYLE_PRIMARY = 'primary'
    STYLE_DANGER = 'danger'
    STYLE_DEFAULT = 'default'

    """
    An interactive component that inserts a button. The button can be a trigger for anything from opening a simple link
    to starting a complex workflow. For more information, see:
    https://api.slack.com/reference/block-kit/block-elements#button
    """

    def __init__(self, text: TextObject, action_id: str, url: str = None, value: str = None, style: str = 'default',
                 confirm: ConfirmObject = None):
        # validate input
        text.validate_text_block(max_length=75, required_type=TextObject.BTYPE_PLAIN_TEXT)
        self.validate_input('url', url, max_length=3000)
        self.validate_input('value', value, max_length=2000)
        self.validate_input('style', style, equality_fields=[self.STYLE_DANGER, self.STYLE_DEFAULT, self.STYLE_PRIMARY])

        super().__init__(btype='button', action_id=action_id)

        self.text = text
        self.url = url
        self.value = value
        self.style = style
        self.confirm = confirm

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'text': self.text.render(),
            'action_id': self.action_id,
        }

        if self.url:
            block.update({'url': self.url})
        if self.value:
            block.update({'value': self.value})
        if self.style:
            block.update({'style': self.style})
        if self.confirm:
            block.update({'confirm': self.confirm.render()})

        return block
