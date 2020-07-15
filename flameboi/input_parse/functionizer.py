import flameboi.input_parse.commands as cmd


class Functionizer:

    def __init__(self, bot_client, admin_client):
        self.bot = bot_client
        self.admin = admin_client
        self.funcs = cmd.commands

    def respond(self, args: list):

        self.funcs.get(args.pop(), lambda: 'Invalid')(*args, self.bot)

    def do_the_dirty_module(self, args):
        pass
