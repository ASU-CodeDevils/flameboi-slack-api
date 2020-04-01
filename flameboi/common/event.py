class Event:
    
    def __init__(self, event: dict):
        user = event.get('user',{})
        channel = event.get('channel_id')
        subtype = event.get('subtype')
        test = event.get('text')
        timestamp = event.get('ts')


        self.user_id = event.get("user",{})
        self.channel_id = event.get("channel") if event.get("channel") else ""


def get_payload(payload) -> dict:
    event = payload.get("event", {})

def build_dict(channel: str, text: str = None, subtype: str = None, user: str = None, ) -> dict:
    print()