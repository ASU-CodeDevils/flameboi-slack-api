def team_join(event):
    theUser = event.user
    deets = ""
    if theUser:
        deets = (
            f"User ID: {theUser.id}\n"
            f"Name: {theUser.name}\n"
            f"Display Name: {theUser.profile.display_name}\n"
            f"Real Name: {theUser.profile.real_name}\n"
            f"Email: {theUser.profile.email}\n"
            f"Time Zone: {theUser.time_zone}\n"
            f"Is Admin: {theUser.is_admin}\n"
            f"Is Owner: {theUser.is_owner}\n"
        )
    else:
        deets = "Invalid user information received!"

    reply = (
        f"Event Type: {event.type}\n"
        f"\nInformation on the User who joined: \n" + deets
    )

    return reply


def reaction_add(event):
    reply = (
        f"Event Type: {event.type}\n"
        f"User ID: {event.user_id}\n"
        f"Reaction: :{event.reaction}:\n"
        f"Item User ID: {event.item_user}\n"
        f"Item Channel: {event.item_channel}\n"
        f"Item TS: {event.item_ts}\n"
        f"Reaction TS: {event.event_ts}"
    )
    return reply


def pin_add(event):
    reply = (
        f"Event Type: {event.type}\n"
        f"User ID: {event.user_id}\n"
        f"Channel ID: {event.channel_id}\n"
        f"Event_TS: {event.event_ts}\n"
    )
    return reply


def channel_join(event, user):
    theUser = user
    deets = ""
    if theUser:
        deets = (
            f"User ID: {theUser.id}\n"
            f"Name: {theUser.name}\n"
            f"Display Name: {theUser.profile.display_name}\n"
            f"Real Name: {theUser.real_name}\n"
            f"Email: {theUser.profile.email}\n"
            f"Time Zone: {theUser.time_zone}\n"
            f"Is Admin: {theUser.is_admin}\n"
            f"Is Owner: {theUser.is_owner}\n"
        )
    else:
        deets = "Invalid user information received!"

    reply = (
        f"Event Type: {event.type}\n"
        f"Channel Joined: <#{event.channel_id}>"
        f"\nInformation on the User who joined: \n" + deets
    )
    return reply


def message(event):
    reply = (
        f"Event Type: {event.type}\n"
        f"Sub Type: {event.subtype}\n"
        f"Channel ID: {event.channel_id}\n"
        f"Channel Name: <#{event.channel_id}>\n"
        f"User ID: {event.user_id}\n"
        f"Message: {event.text}\n"
        f"Timestamp: {event.ts}"
    )
    return reply


def app_mention(event):
    reply = (
        f"Event Type: {event.type}\n"
        f"User ID: {event.user_id}\n"
        f"Message: {event.text}\n"
        f"Timestamp: {event.ts}\n"
        f"Channel ID: {event.channel_id}\n"
        f"Event TS: {event.event_ts}"
    )
    return reply
