class Event(object):
    
    def __init__(self, payload):
        self.event = payload.get('event', {})
        

    def get_user_ID(self):
        return self.event.get('user')


    def get_channel_ID(self):
        return self.event.get('channel')


    def get_text(self):
        return self.event.get('text')


    def get_event_ts(self):
        return self.event.get('ts')


    def get_subtype(self):
        return self.event.get('subtype')


    def get_reaction(self):
        return self.event.get('reaction')


    def _get_item(self):
        return self.event.get('item',{})


    def get_item_channel(self):
        return self._get_item.get('channel')


    def get_item_ts(self):
        return self._get_item.get('ts')

    def get_item_file(self):
        return self._get_item.get('file')

    def get_specs(self) -> dict:
        pass
    # reserved for future implementation