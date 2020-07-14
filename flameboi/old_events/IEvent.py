

class Event(object):

    def __init__(self, payload):
        self.event = payload.get('event', {})
        self.item = payload.get('event', {}).get('item', {})

    """
    Message stuff
    """

    def get_msg_type(self) -> str:
        return self.event.get('type')

    def get_user_id(self) -> str:
        return self.event.get('user')

    def get_channel_id(self) -> str:
        return self.event.get('channel')

    def get_text(self) -> str:
        return self.event.get('text')

    def get_event_ts(self) -> str:
        return self.event.get('ts')

    def get_subtype(self) -> str:
        return self.event.get('subtype')

    def get_is_starred(self) -> bool:
        return self.event.get('is_starred')

    def get_pinned_to(self) -> list:
        return self.event.get('pinned_to')

    def get_reaction_list(self) -> list:
        return self.event.get('reactions', [])

    def get_reaction_stats(self, reaction: str) -> dict:
        for emote in self.get_reactions():
            if emote.get('name') == reaction:
                return emote
            else:
                return None

    def is_hidden_type(self) -> bool:
        return self.event.get('hidden')

    """
    Reaction stuff
    """

    def get_item_user(self) -> str:
        return self.event.get('item_user')

    def get_item_type(self) -> str:
        return self.item.get('type)')

    def get_reaction(self) -> str:
        return self.event.get('reaction')

    def get_item_channel(self) -> str:
        return self.item.get('channel')

    def get_reaction_ts(self) -> str:
        return self.event.get('event_ts')

    def get_item_ts(self) -> str:
        return self.item.get('ts')

    def get_item_file(self) -> str:
        return self.item.get('file_id')

    def get_item_file_comment(self) -> str:
        return self.item.get('file_comment')

    """
    Channel Join Stuff
    """

    def get_channel_type(self) -> str:
        return self.event.get('channel_type')

    def get_team(self) -> str:
        return self.event.get('team')

    def get_inviter(self) -> str:
        return self.event.get('inviter')

    """
    App home stuff
    """

    def get_tab(self):
        return self.event.get('tab')

    def get_view(self):
        return self.event.get('view', {})
