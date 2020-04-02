from flameboi.common.IEvent import Event

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


    # if sub_type != 'bot_message':
    #     if text and text.lower() == "!test" :
    #         logger.info("Responding to !test command")
    #         reply = "I'm here <@%s>! :tada:" % user_id
                
    #         assert theBot.send_message(channel_id, reply)["ok"]

    #     """
    #     TODO: Expand on block kit builder base (which is awesome Kevin!)
    #     Below is example use of blocks using !onboard to send the onboarding block
    #     """
        
    #     if text and text.lower() == "!onboard":
    #         logger.info("Responding to !onboard command")
            
    #         assert theBot.send_onboarding_DM(user_id)["ok"]

    #     if text and text.lower() == "!qod":
    #         logger.info("Responding to !qod command")
            
    #         assert theBot.send_qod(channel_id)["ok"]
