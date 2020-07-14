from flameboi.events.IEvent import Event


class AppHomeEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_id(),
            'channel_id': self.get_channel_id(),
            'tab': self.get_tab(),
            'view': self.get_view(),
        }
