from flameboi.common.IEvent import Event


class AppMentionEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_id,
            'channel_id': self.get_channel_id,
            'text': self.get_text,
            'ts': self.get_event_ts,
        }