from slack_blockkit.composition_object import TextObject
from slack_blockkit.layout_block import DividerBlock, SectionBlock
from slack_blockkit.utils import get_blocks


def get_playlist_block():

    blocks = get_blocks(
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=(":partywizard: CodeDevils playlists on Spotify :partywizard:"),
            ),
            fields=[
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/0lHeOLHPtj3dZnI7hjbEiy?si|*CodeDevils*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/1d8nCeom1L86vGT2JgSkzN?si|*ReggaeDevils*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/0GqMtAzxxETzI8NtRVST6l?si|*InstrumentalDevils*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/5jLaarFVeCvkHCAhKnfdod?si|*HipHopDevils*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://www.youtube.com/watch?v=wNzdzqksyiQ|*Stu's Juke Box* :copyright:>",
                ).render(),
            ],
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=("Other good playlists on Spotify"),
            ),
            fields=[
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7?si|*Brain Food*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn?si|*LoFi Beats*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ?si|*Deep Focus*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/1VWJjbN7LBzM6M4FG76ImT|*Asian LoFi Hip Hop*>",
                ).render(),
                TextObject(
                    btype=TextObject.BTYPE_MARKDOWN,
                    text="<https://open.spotify.com/playlist/08fTEpRNEn0FcyXOWZ60wO?si|*Acid Jazz/Lounge/Triphop*>",
                ).render(),
            ],
        ),
        DividerBlock(),
    )
    return blocks
