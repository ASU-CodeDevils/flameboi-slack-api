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
    def __init__(self, user_dict: dict):
        self.profile = Profile(user_dict.get("profile", {}))

        self.id = user_dict.get("id")
        self.name = user_dict.get("name")
        self.real_name = user_dict.get("real_name")
        self.team_id = user_dict.get("team_id")
        self.time_zone = user_dict.get("tz")
        self.tz_label = user_dict.get("tz_label")
        self.tz_offset = user_dict.get("tz_offset")
        self.is_admin = user_dict.get("is_admin")
        self.is_owner = user_dict.get("is_owner")


class Profile:
    def __init__(self, prof_dict: dict):
        self.avatar_hash = prof_dict.get("avatar_hash")
        self.status_text = prof_dict.get("status_text")
        self.status_emoji = prof_dict.get("status_emoji")
        self.real_name = prof_dict.get("real_name")
        self.display_name = prof_dict.get("display_name")
        self.real_name_normalized = prof_dict.get("real_name_normalized")
        self.display_name_normalized = prof_dict.get("display_name_normalized")
        self.email = prof_dict.get("email")
        self.image_original = prof_dict.get("image_original")
        self.image_24 = prof_dict.get("image_24")
        self.image_32 = prof_dict.get("image_32")
        self.image_48 = prof_dict.get("image_48")
        self.image_72 = prof_dict.get("image_72")
        self.image_192 = prof_dict.get("image_192")
        self.image_512 = prof_dict.get("image_512")
        self.team = prof_dict.get("team")


class Item:
    def __init__(self, item_dict: dict):
        self.channel_id = item_dict.get("channel")
        self.created_by = item_dict.get("created_by")
        self.message = item_dict.get("message, {}")
        self.type = item_dict.get("type")
