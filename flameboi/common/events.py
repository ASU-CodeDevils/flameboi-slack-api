class MessageEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})

        self.type = self.event.get("type")
        self.subtype = self.event.get("subtype")
        self.hidden = self.event.get("hidden")
        self.channel_id = self.event.get("channel")
        self.user_id = self.event.get("user")
        self.text = self.event.get("text")
        self.ts = self.event.get("ts")
        self.message = self.event.get("message", {})


# Message sub-types for Slack Events API
#     bot_message
#     ekm_access_denied
#     group_join
#     group_leave
#     me_message
#     message_changed*
#     message_deleted*
#     message_replied*
#     reply_broadcast
#     thread_broadcast

#     * indicates the hidden property


class ReactionAddedEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})
        self.item = self.event.get("item", {})

        self.type = self.event.get("type")
        self.user_id = self.event.get("user")
        self.reaction = self.event.get("reaction")
        self.item_user = self.event.get("item_user")
        self.item_type = self.item.get("type")
        self.item_channel = self.item.get("channel")
        self.item_ts = self.item.get("ts")
        self.event_ts = self.event.get("event_ts")
        self.item_file = self.item.get("file")
        self.file_comment = self.item.get("file_comment")


class PinAddedEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})
        self.item = self.event.get("item", {})

        self.type = self.event.get("type")
        self.user_id = self.event.get("user")
        self.channel_id = self.event.get("channel_id")
        self.event_ts = self.event.get("event_ts")


class AppHomeEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})

        self.type = self.event.get("type")
        self.user_id = self.event.get("user")
        self.channel_id = self.event.get("channel")
        self.event_ts = self.event.get("event_ts")
        self.tab = self.event.get("tab")
        self.view = self.event.get("view", {})


class AppMentionEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})

        self.type = self.event.get("type")
        self.user_id = self.event.get("user")
        self.text = self.event.get("text")
        self.ts = self.event.get("ts")
        self.channel_id = self.event.get("channel")
        self.event_ts = self.event.get("event_ts")


class MemberJoinedChannelEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})

        self.type = self.event.get("type")
        self.user_id = self.event.get("user")
        self.channel_id = self.event.get("channel")
        self.channel_type = self.event.get("channel_type")
        self.team = self.event.get("team")
        self.inviter = self.event.get("inviter")


class TeamJoinEvent:
    def __init__(self, payload):
        self.event = payload.get("event", {})

        self.type = self.event.get("type")
        self.user = self.event.get("user", {})
