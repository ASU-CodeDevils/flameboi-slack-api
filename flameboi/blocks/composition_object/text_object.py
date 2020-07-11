from flameboi.blocks.block import Block


class TextObject(Block):
    """
    Represents a text object. For more information, see:
    https://api.slack.com/reference/block-kit/composition-objects#text
    """

    BTYPE_PLAIN_TEXT = 'plain_text'
    BTYPE_MARKDOWN = 'mrkdwn'

    def __init__(self, btype: str, text: str, emoji: bool = False, verbatim: bool = False):
        # validate that the type is correct
        if btype == self.BTYPE_PLAIN_TEXT or btype == self.BTYPE_MARKDOWN:
            self.btype = btype
        else:
            raise AttributeError(f'Invalid btype. Must be {self.BTYPE_MARKDOWN} or {self.BTYPE_PLAIN_TEXT}: {btype}')

        self.text = text

        # emoji field is only usable if the type is plain text
        self.emoji = (emoji and btype == self.BTYPE_PLAIN_TEXT)
        self.verbatim = verbatim

    def is_plain_text(self):
        return self.btype == self.BTYPE_PLAIN_TEXT

    def is_markdown(self):
        return self.btype == self.BTYPE_MARKDOWN

    def get_text_length(self):
        return len(self.text)

    def validate_text_block(self, max_length: int = 0, required_type: str = None):
        # check that the text is not greater than the max length
        if max_length != 0 and len(self.text) > max_length:
            raise AttributeError(f'text object text should not be greater than {max_length} characters, but is '
                                 f'{len(self.text)}')
        if required_type and self.btype != required_type:
            raise AttributeError(f'text object type should be {required_type}, but is {self.btype}')

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'text': self.text
        }

        if self.emoji:
            block.update({'emoji': self.emoji})

        if self.verbatim:
            block.update({'verbatim': self.verbatim})

        return block
