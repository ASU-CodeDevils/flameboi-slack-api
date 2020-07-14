from flameboi.events.IEvent import Event


class AppMentionEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'type': self.get_msg_type(),
            'user_id': self.get_user_id(),
            'text': self.get_text(),
            'ts': self.get_event_ts(),
            'channel_id': self.get_channel_id(),
            'event_ts': self.get_item_ts(),
        }
