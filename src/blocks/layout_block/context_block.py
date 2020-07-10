from flameboi.blocks.layout_block.layout_block import LayoutBlock


class ContextBlock(LayoutBlock):
    """
    Displays message context, which can include both images and text. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#context
    """

    def __init__(self, elements: list, block_id: str = None):
        # validate input
        if len(elements) > 10:
            raise AttributeError('cannot have more than 10 elements in context blocks')

        super().__init__(btype='context', block_id=block_id)
        self.elements = elements

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'elements': self.elements
        }

        if self.block_id:
            block.update({'block_id': self.block_id})

        return block
