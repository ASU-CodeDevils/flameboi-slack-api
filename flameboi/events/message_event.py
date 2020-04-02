class Message_Event(EventInterface):


    def __init__(self):
        print()

    # event = payload.get("event", {})

    # sub_type = event.get("subtype")
    # channel_id = event.get("channel")
    # user_id = event.get("user")
    # text = event.get("text")
    # ts = event.get("ts")

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
