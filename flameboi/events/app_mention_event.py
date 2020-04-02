from flameboi.common.IEvent import Event

class AppMentionEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self):
        pass