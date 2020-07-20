import re
import flameboi.parser.bang_commands as bang
import flameboi.parser.query_commands as query


class Parser:
    """
    Methods used to find and extract various command phrases from a string.

        Args:
            currently no args needed for constructor.  Only externally accessible method takes a string
            such as that found in a message text and uses instance variables that store commands and 
            compiled regex terms relating to those commands.
    """

    def __init__(self):
        self.compiled_regexes = [
            re.compile(bang.regex),
            re.compile(query.regex),
        ]
        self.commands = [
            bang.commands,
            query.commands,
        ]

    def _has_commands(self, message: str) -> set:
        """
        Helper function that takes the message as a string, iterates through the class' list of compiled
        regex terms.  Finds all instances of each type of command (!command, ?command, etc) and appends
        each to a singular list of found commands.  List is then converted to set to remove duplicate
        commands.

        :param message: The message to find commands within.
        :type message: str
        :return: A set of regex matches.
        :rtype: set
        """

        list_matches = []
        for reg in self.compiled_regexes:
            list_matches.append(reg.findall(message))
        return set(list_matches)

    def _get_commands(self, message: str) -> list:
        """
        Helper function that takes the message as a string, passes it to _has_commands, then processes the
        returned set of found regex matches, removes leading or trailing whitespace.

        :param message: The message to find commands within.
        :type message: str
        :return: A set of commands as strings.
        :rtype: set
        """

        cmds = []
        for list_match in self._has_commands(message):
            for cmd in list_match:
                cmds.append(cmd.strip())
        return set(cmds)

    def parse_commands(self, message: str) -> list:
        """
        This message takes a message as a string passes it to _getcommands, which returns a list of commands
        in string form. This function then iterates through them and returns a list of functions to run.

        :param message: The message to find commands within.
        :type message: str
        :return: A list of functions.
        :rtype: list
        """

        funcs_to_run = []
        for cmd in self._get_commands(message):
            funcs_to_run.append(self.commands[cmd])
        return funcs_to_run
