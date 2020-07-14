from flameboi.events.IEvent import Event


class ReactionAddedEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_id(),
            'reaction': self.get_reaction(),
            'item_user': self.get_item_user(),
            'channel_id': self.get_item_channel(),
            'item_ts': self.get_item_ts(),
            'reaction_ts': self.get_reaction_ts(),

        }
