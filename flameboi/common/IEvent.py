class EventInterface:
    
    def __init__(self, payload):
        event = self.get_payload(payload)
        user = event.get('user',{})
        channel = event.get('channel_id')
        subtype = event.get('subtype')
        test = event.get('text')
        timestamp = event.get('ts')


        self.user_id = user
        self.channel_id = channel if channel else ""
        self.subtype = subtype if subtype else ""
        self.text = text if text else ""
        self.timestamp = timestamp if timestamp else ""



    def get_payload(self, payload) -> dict:
        event = payload.get("event", {})

    def build_dict(self, channel: str, text: str = None, subtype: str = None, user: str = None, ) -> dict:
        print()