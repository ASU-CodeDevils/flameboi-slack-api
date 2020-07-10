from flameboi.blocks.layout_block.layout_block import LayoutBlock


class FileBlock(LayoutBlock):
    """
    Displays a remote file. For more information, see:
    https://api.slack.com/reference/block-kit/blocks#file
    """

    def __init__(self, external_id: str, source: str = 'remote', block_id: str = None):
        super().__init__(btype='file', block_id=block_id)
        self.external_id = external_id
        self.source = source

    def render(self) -> dict:
        block = {
            'type': self.btype,
            'external_id': self.external_id,
            'source': self.source
        }

        if self.block_id:
            block.update({'block_id': self.block_id})

        return block
