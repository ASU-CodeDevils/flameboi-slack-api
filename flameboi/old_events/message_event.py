from flameboi.events.IEvent import Event

"""
TODO: import specific modules here that will respond to the designated type of event that occurs
from flameboi.modules.qod import QOD
"""


class MessageEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'type': self.get_msg_type(),
            'sub_type': self.get_subtype(),
            'channel_id': self.get_channel_id(),
            'user_id': self.get_user_id(),
            'text': self.get_text(),
            'ts': self.get_event_ts(),
        }

        # self.sub_types = [
        #     "bot_message",
        #     "ekm_access_denied",
        #     "me_message",
        #     "message_changed",
        #     "message_deleted",
        #     "message_replied",
        #     "reply_broadcast",
        #     "thread_broadcast",
        # ]