class Reaction_Added(EventInterface):

    def __init__(self):
        print()

    # event = payload.get("event", {})

    # user_id = event.get('user')
    # emoji = event.get('reaction')
    # channel_id = event.get("item", {}).get("channel")
    # ts = event.get("item", {}).get("ts")
    
    # """
    # TODO: Create function in flameboi.py that builds a reaction_add block if possible?
    # """
    # sub_type = event.get("subtype")

    # if user_id != bot_user_id:
    #     logger.info("Responding to reaction added.")
    #     response = slack_web_client.reactions_add(
    #         name=emoji,
    #         channel=channel_id,
    #         timestamp=ts
    #         )
    #     assert response["ok"]
    # else:
    #     logger.info("Reaction added was bots!")
    #     logger.info(sub_type)
