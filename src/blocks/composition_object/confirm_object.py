from flameboi.blocks.block import Block
from flameboi.blocks.composition_object.text_object import TextObject


class ConfirmObject(Block):
    """
    An object that defines a dialog that provides a confirmation step to any interactive element. This dialog will ask
    the user to confirm their action by offering a confirm and deny buttons. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#confirm
    """

    def __init__(self, title: TextObject, text: TextObject, confirm: TextObject, deny: TextObject):
        # validate input
        title.validate_text_block(max_length=100, required_type=TextObject.BTYPE_PLAIN_TEXT)
        text.validate_text_block(max_length=300)
        confirm.validate_text_block(max_length=30, required_type=TextObject.BTYPE_PLAIN_TEXT)
        deny.validate_text_block(max_length=30, required_type=TextObject.BTYPE_PLAIN_TEXT)

        self.title = title
        self.text = text
        self.confirm = confirm
        self.deny = deny

    def render(self) -> dict:
        return {
            'title': self.title.render(),
            'text': self.text.render(),
            'confirm': self.confirm.render(),
            'deny': self.deny.render()
        }
