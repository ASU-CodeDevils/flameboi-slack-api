import re
import flameboi.parser.bang_commands as bang
import flameboi.parser.query_commands as query


class Parser:
    def __init__(self):
        self.compiled_regexes = [
            re.compile(bang.regex),
            re.compile(query.regex),
        ]
        self.commands = [
            bang.commands,
            query.commands,
        ]

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
        return funcs_to_run
