from flameboi.common.IEvent import Event


class ReactionAddedEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_id,
            'channel_id': self.get_item_channel,
            'text': self.get_text,
            'ts': self.get_item_ts,
            'reaction': self.get_reaction
        }
