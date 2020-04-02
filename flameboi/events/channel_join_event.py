from flameboi.common.IEvent import Event

class ChannelJoin(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.get_user_ID,
            'channel_id': self.get_channel_ID
        }
    
    # logger.info("Responding to member joined event")

    # name = theBot.get_user_info(user_id)
    # text = ":tada: Welcome to channel, %s!!! :tada:" % name['user']['real_name']
    
    # assert theBot.send_message(channel_id, text)["ok"]