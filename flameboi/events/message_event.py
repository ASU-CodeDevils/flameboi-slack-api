from ..common.IEvent import Event

class MessageEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_ID,
            'channel_id': self.get_channel_ID,
            'text': self.get_text,
            'ts': self.get_event_ts,
            'sub_type': self.get_subtype
        }
