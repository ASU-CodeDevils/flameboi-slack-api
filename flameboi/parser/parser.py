import re
from flameboi.modules_admin.onboard import get_onboarding_block
from flameboi.modules_user.qod import get_qod_block
from flameboi.modules_user.playlists import get_playlist_block


class Parser:
    def __init__(self):
        self.compiled_regexes = [
            re.compile(r"[ ]*![a-zA-Z]{1,10}[ ]*"),
        ]
        self.commands = {
            "!qod": get_qod_block,
            "!playlists": get_playlist_block,
            "!onboard": get_onboarding_block,
        }

    def _has_commands(self, message: str) -> list:
        list_matches = []
        for reg in self.compiled_regexes:
            list_matches.append(reg.findall(message))

    def _get_commands(self, message: str) -> list:
        cmds = []
        for list_match in self._has_commands(message):
            for cmd in list_match:
                cmds.append(cmd.strip())
        return cmds

    def parse_commands(self, message: str) -> list:
        funcs_to_run = []
        for cmd in self._get_commands(message):
            funcs_to_run.append(self.commands[cmd])
