"""
TODO: Need to go through this as each event has distinct flags... some of this is redundant
"""


class Event(object):

    def __init__(self, payload):
        self.event = payload.get('event', {})
        self.item = payload.get('event', {}).get('item', {})

    # Message stuff

    def get_msg_type(self):
        return self.event.get('type')

    def get_user_id(self):
        return self.event.get('user')

    def get_channel_id(self):
        return self.event.get('channel')

    def get_text(self):
        return self.event.get('text')

    def get_event_ts(self):
        return self.event.get('ts')

    def get_subtype(self):
        return self.event.get('subtype')

    # Reaction stuff

    def get_item_user(self):
        return self.event.get('item_user')

    def get_item_type(self):
        return self.item.get('type)')

    def get_reaction(self):
        return self.event.get('reaction')

    def get_item_channel(self):
        return self.item.get('channel')

    def get_reaction_ts(self):
        return self.event.get('event_ts')

    def get_item_ts(self):
        return self.item.get('ts')

    def get_item_file(self):
        return self.item.get('file_id')

    def get_item_file_comment(self):
        return self.item.get('file_comment')

    # Channel Join Stuff

    def get_channel_type(self):
        return self.event.get('channel_type')

    def get_team(self):
        return self.event.get('team')

    def get_inviter(self):
        return self.event.get('inviter')

    # App home stuff

    def get_tab(self):
        return self.event.get('tab')

    def get_view(self):
        return self.event.get('view', {})

    # reserved for future implementation
