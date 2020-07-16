class Message:
    def __init__(self, messageAsDict: dict):
        self.type = messageAsDict.get("type")
        self.subtype = messageAsDict.get("subtype")
        self.hidden = messageAsDict.get("hidden")
        self.user = messageAsDict.get("user")
        self.channel = messageAsDict.get("channel")
        self.timestamp = messageAsDict.get("ts")
        self.text = messageAsDict.get("text")
        self.is_starred = messageAsDict.get("is_starred")
        self.pinned_to = messageAsDict.get("pinned_to")
        self.reactions = messageAsDict.get("reactions")
        self.permalink = messageAsDict.get("permalink")


class Reactions:
    def __init__(self, reaction_as_dict: dict):
        self.name = reaction_as_dict.get("name")
        self.count = reaction_as_dict.get("count")
        self.users = reaction_as_dict.get("users")


class User:
    def __init__(self, response: dict):
        self.is_ok = response.get("ok")
        self.user = response.get("user", {})
        self.profile = self.user.get("profile", {})

        self.id = self.user.get("id")
        self.name = self.user.get("name")
        self.displyname = self.profile.get("display_name")
        self.real_name = self.user.get("real_name")
        self.email = self.profile.get("email")
        self.team = self.profile.get("team")
        self.team_id = self.user.get("team_id")
        self.time_zone = self.user.get("tz")
        self.tz_label = self.user.get("tz_label")
        self.tz_offset = self.user.get("tz_offset")
        self.is_admin = self.user.get("is_admin")
        self.is_owner = self.user.get("is_owner")


class Item:
    def __init__(self, item_dict: dict):
        self.channel_id = item_dict.get("channel")
        self.created_by = item_dict.get("created_by")
        self.message = item_dict.get("mesage")
        self.type = item_dict.get("type")
