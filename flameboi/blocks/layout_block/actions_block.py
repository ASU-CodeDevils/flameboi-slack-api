from flameboi.blocks.layout_block.layout_block import LayoutBlock


class ActionsBlock(LayoutBlock):
    """
    A block that is used to hold interactive elements. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#actions
    """

    def __init__(self, elements: list, block_id: str = None):
        # validate_input
        if len(elements) > 5:
            raise AttributeError('cannot have more than 5 elements in action blocks')

        super().__init__(btype='actions', block_id=block_id)
        self.elements = elements

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'elements': self.elements
        }

        if self.block_id:
            block.update({'block_id': self.block_id})

        return block
