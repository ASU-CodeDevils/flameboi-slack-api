from flameboi.modules_admin.onboard import get_onboarding_block
from flameboi.modules_user.qod import get_qod_block
from flameboi.modules_user.playlists import get_playlist_block

regex = r"[ ]{0,1}\?[\w]+[ ]{0,1}"

commands = {
    "?qod": get_qod_block,
    "?playlists": get_playlist_block,
    "?onboard": get_onboarding_block,
}
