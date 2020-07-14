from flameboi.events.IEvent import Event


class ChannelJoinEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'type': self.get_msg_type(),
            'user_id': self.get_user_id(),
            'channel_id': self.get_channel_id(),
            'channel_type': self.get_chan_type(),
            'team': self.get_team(),
            'inviter': self.get_inviter(),
        }
