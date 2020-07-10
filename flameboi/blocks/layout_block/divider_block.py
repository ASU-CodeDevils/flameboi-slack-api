from flameboi.blocks.layout_block.layout_block import LayoutBlock


class DividerBlock(LayoutBlock):
    """
    Defines a divider block. For more information, see: https://api.slack.com/reference/block-kit/blocks#divider
    """

    def __init__(self, block_id: str = None):
        super().__init__(btype='divider', block_id=block_id)
