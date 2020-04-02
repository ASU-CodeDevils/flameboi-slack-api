from flameboi.common.IEvent import Event

class PinAddedEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self):
        pass
    
    # event = payload.get("event", {})

    # channel_id = event.get("channel_id")
    # user_id = event.get("user")
