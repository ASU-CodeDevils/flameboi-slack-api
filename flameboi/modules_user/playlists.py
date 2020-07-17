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
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/0lHeOLHPtj3dZnI7hjbEiy?si=vsB1ABcPQZWLDfELbbcPSw|*CodeDevils*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/1d8nCeom1L86vGT2JgSkzN?si=TjIS1iVcTPqIaGwocuaywA|*ReggaeDevils*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/0GqMtAzxxETzI8NtRVST6l?si=inOzMz43QJWL6hgT_1rOnQ|*InstrumentalDevils*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/5jLaarFVeCvkHCAhKnfdod?si=2pJX95vtQv2Pbf81b16p9w|*HipHopDevils*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://www.youtube.com/watch?v=wNzdzqksyiQ|*Stu's Juke Box* :copyright:>",
                },
            ],
        ),
        DividerBlock(),
        SectionBlock(
            text=TextObject(
                btype=TextObject.BTYPE_MARKDOWN,
                text=("Other good playlists on Spotify"),
            ),
            fields=[
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7?si=kdJfP56gS1mAPYEcsOc5fg|*Brain Food*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn?si=SB-cPgIsTL-gvA9xWH3rrg|*LoFi Beats*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ?si=1VgEAzJmRF-nJ0qNRPd-1A|*Deep Focus*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/1VWJjbN7LBzM6M4FG76ImT|*Asian LoFi Hip Hop*>",
                },
                {
                    "type": "mrkdwn",
                    "text": "<https://open.spotify.com/playlist/08fTEpRNEn0FcyXOWZ60wO?si=xCjkW151TNuhsyjHswqlfQ|*Acid Jazz/Lounge/Dub/Triphop*>",
                },
            ],
        ),
        DividerBlock(),
    )
    return blocks
