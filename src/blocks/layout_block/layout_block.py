from flameboi.blocks.block import Block


class LayoutBlock(Block):
    """
    Defines a basic layout block. For more information, see: https://api.slack.com/reference/block-kit/blocks
    """

    def __init__(self, btype: str, block_id: str = None):
        if block_id and len(block_id) > 255:
            raise AttributeError(f'block_id cannot be greater than 255 characters, but is {block_id}')

        self.btype = btype
        self.block_id = block_id

    def render(self) -> dict:
        block = {
            'type': self.btype
        }

        if self.block_id:
            block.update({'block_id': self.block_id})

        return block
