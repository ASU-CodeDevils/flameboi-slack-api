class Message:
    def __init__(self, messageAsDict: dict):
        self.poster = messageAsDict.get('user')
        self.channel = messageAsDict.get('channel')
        self.timestamp = messageAsDict.get('ts')
        self.text = messageAsDict.get('text')


class User:
    def __init__(self, response: dict):
        self.user = response.get('user', {})
        self.profile = self.user.get('profile', {})

        self.id = self.user.get('id')
        self.name = self.user.get('name')
        self.displyname = self.profile.get('display_name')
        self.real_name = self.user.get('real_name')
        self.email = self.profile.get('email')
        self.team = self.profile.get('team')
        self.team_id = self.user.get('team_id')
        self.time_zone = self.user.get('tz')
        self.tz_label = self.user.get('tz_label')
        self.tz_offset = self.user.get('tz_offset')
        self.is_admin = self.user.get('is_admin')
        self.is_owner = self.user.get('is_owner')
