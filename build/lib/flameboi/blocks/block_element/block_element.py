from ..block import Block


class BlockElement(Block):
    """
    Defines a basic block element. For more information, see: https://api.slack.com/reference/block-kit/block-elements
    """

    def __init__(self, btype: str, action_id: str = None):
        # validate the action id
        if action_id and len(action_id) > 255:
            raise AttributeError(f'action_id cannot be more than 255 characters long, but is {len(action_id)}')

        self.btype = btype
        self.action_id = action_id

    def render(self) -> dict:
        block = {
            'type': self.btype
        }

        if self.action_id:
            block.update({'action_id': self.action_id})

        return block
