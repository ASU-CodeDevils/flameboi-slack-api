import json
import os

from flameboi.common.events import (
    AppHomeEvent,
    AppMentionEvent,
    MemberJoinedChannelEvent,
    MessageEvent,
    PinAddedEvent,
    ReactionAddedEvent,
    TeamJoinEvent,
)
from flameboi.modules.onboard import get_onboarding_block, get_sample_block


class Router:
    """
    Methods used to router/direct events within the Flameboi Slack bot API.

    :return: The list of channels as a dict.
    :rtype: dict
    """

    # TODO: instantiate a modrunner class that will run modules triggered

    def __init__(self, theBot):
        self.bot = theBot.getClient()
        self.admin = theBot.getAdmin()
        self.theBot = theBot

        # Import various ID's for filtering via dotenv
        self.bot_id = os.getenv("BOT_ID")
        self.bot_user_id = os.getenv("USER_ID")
        self.bot_app_id = os.getenv("APP_ID")

        self.home_channel = os.getenv("HOME_CHAN_ID")
        self.debug_chan = os.getenv("DEBUG_CHAN_ID")
        self.stu_user = os.getenv("STU_ID")

    def handle_team_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = TeamJoinEvent(payload)

        theUser = self.theBot.get_user_as_obj(event)
        deets = ""
        if theUser.is_ok:
            deets = (
                f"User ID: {theUser.id}\n"
                f"Name: {theUser.name}\n"
                f"Display Name: {theUser.displyname}\n"
                f"Real Name: {theUser.real_name}\n"
                f"Email: {theUser.email}\n"
                f"Team: {theUser.team}\n"
                f"Team ID: {theUser.team_id}\n"
                f"Time Zone: {theUser.time_zone}\n"
                f"Is Admin: {theUser.is_admin}\n"
                f"Is Owner: {theUser.is_owner}\n"
            )
        else:
            deets = "Invalid user information received!"

        reply = (
            f"Testing Event Triggered...\n"
            f"Team Join Event\n"
            f"\nAnticipated Response: \n"
            f":tada: :partywizard: Welcome to CodeDevils, {theUser.real_name}! :partywizard: :tada:\n"
            f"\nInformation on the User who joined: \n" + deets
        )

        response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)

        assert response["ok"]

    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = ReactionAddedEvent(payload)

        if event.item_channel == self.debug_chan and event.user_id != self.bot_user_id:
            reply = (
                f"Event Type: {event.type}\n"
                f"User ID: {event.user_id}\n"
                f"Reaction: {event.reaction}\n"
                f"Item User ID: {event.item_user}\n"
                f"Item Channel: {event.item_channel}\n"
                f"Item TS: {event.item_ts}\n"
                f"Reaction TS: {event.event_ts}"
            )

            response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)
            assert response["ok"]

        # Test function for looping reaction response

        elif event.user_id != self.bot_user_id:
            if event.reaction and event.reaction == "parrot":
                for i in range(1, 10):
                    response = self.bot.reactions_add(
                        name=f"parrotwave{i}",
                        channel=event.item_channel,
                        timestamp=event.item_ts,
                    )
                    assert response["ok"]
            elif event.reaction and event.reaction == "fuckyouadmin":
                response = self.bot.reactions_add(
                    name="heart", channel=event.item_channel, timestamp=event.item_ts,
                )
                assert response["ok"]
            else:
                response = self.bot.reactions_add(
                    name=event.reaction,
                    channel=event.item_channel,
                    timestamp=event.item_ts,
                )
                assert response["ok"]

    # TODO: implement this

    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = PinAddedEvent(payload)

        reply = (
            f"Testing Event Triggered...\n"
            f"Pin Added Event\n"
            f"Event Type: {event.type}\n"
            f"User ID: {event.user_id}\n"
            f"Channel ID: {event.channel_id}\n"
            f"Event_TS: {event.event_ts}\n"
        )

        response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply)
        assert response["ok"]

    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = MessageEvent(payload)

        if event.channel_id == self.debug_chan and event.user_id != self.bot_user_id:
            reply = (
                f"Event Type: {event.type}\n"
                f"Sub Type: {event.subtype}\n"
                f"Channel ID: {event.channel_id}\n"
                f"User ID: {event.user_id}\n"
                f"Message: {event.text}\n"
                f"Timestamp: {event.ts}"
            )

            response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)

            assert response["ok"]

        # Test function for specific user and chain reaction response

        if event.user_id == "USLACKBOT":

            if event.text and "yes" in event.text.lower():

                removal = self.admin.chat_delete(channel=event.channel_id, ts=event.ts,)
                assert removal["ok"]

                reply = "This response replaced by a better bot..."

                response = self.bot.chat_postMessage(
                    channel=event.channel_id, text=reply,
                )
                assert response["ok"]
            else:
                badbot = ["b", "a1", "letterd", "btrain", "o", "latin_cross"]

                for emote in badbot:
                    response = self.bot.reactions_add(
                        channel=event.channel_id, timestamp=event.ts, name=emote,
                    )
                    assert response["ok"]

        if event.subtype != "bot_message" and event.subtype != "message_deleted":

            # Test to see if flameboi responds quicker that slackbot (it does for now!)

            # if details['text'] and details['text'].lower() == "jesus":

            #     reply = f"Speedtest"

            #     response = self.bot.chat_postMessage(
            #         channel=details['channel_id'],
            #         text=reply,
            #     )

            #       assert response["ok"]

            # Test function for unthreaded response

            if event.text and event.text.lower() == "!test":

                reply = f":tada: :partywizard: I'm here <@{event.user_id}>! :partywizard: :tada:"

                response = self.bot.chat_postMessage(
                    channel=event.channel_id, text=reply,
                )

                assert response["ok"]

            # Test function for threaded response

            elif event.text and event.text.lower() == "!testthread":

                reply = f":tada: :partywizard: I'm here <@{event.user_id}>! :partywizard: :tada:"

                response = self.bot.chat_postMessage(
                    channel=event.channel_id, text=reply, thread_ts=event.ts,
                )

                assert response["ok"]

            # Test function for block response

            elif event.text and event.text.lower() == "!testblock":

                response = self.bot.chat_postMessage(
                    channel=event.channel_id,
                    text="testing...",
                    blocks=json.dumps(get_sample_block()),
                )
                assert response["ok"]

            # Test function for reaction response

            elif (
                event.text
                and "party" in event.text.lower()
                and ":partywizard:" not in event.text
            ):

                reply = ":partywizard:"

                response = self.bot.chat_postMessage(
                    channel=event.channel_id, text=reply,
                )

                assert response["ok"]

            # Test function for to get channel info and links

            elif event.text and event.text.lower() == "!channel":

                name = self.bot.conversations_info(channel=event.channel_id)

                usable = name.get("channel", {}).get("name")

                reply = (
                    f"Channel ID: {event.channel_id}\n"
                    f"Channel Name: {usable}\n"
                    f"Channel Link: <#{event.channel_id}>"
                )

                response = self.bot.chat_postMessage(
                    channel=event.channel_id, text=reply,
                )

                assert response["ok"]

            # TODO: Expand on block kit builder base (which is awesome Kevin!)
            # Below is example use of blocks using !onboard to send the onboarding block

            # if details['text'] and details['text'].lower() == "!onboard":
            #     assert self.bot.send_onboarding_DM(details['user_id'])["ok"]
            #
            # if details['text'] and details['text'].lower() == "!qod":
            #     assert self.bot.send_qod(details['channel_id'])["ok"]

    def handle_channel_join(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = MemberJoinedChannelEvent(payload)

        theUser = self.theBot.get_user_as_obj(event.user_id)

        reply = (
            f"Testing Event Triggered...\n"
            f"Channel Join Event\n"
            f"Anticipated Response: \n"
            f":tada: :partywizard: Welcome to <#{event.channel_id}>, {theUser.real_name}! :partywizard: :tada:\n"
            f"\nInformation on the User who joined: \n"
            f"User ID: {theUser.id}\n"
            f"Name: {theUser.name}\n"
            f"Display Name: {theUser.displyname}\n"
            f"Real Name: {theUser.real_name}\n"
            f"Email: {theUser.email}\n"
            f"Team: {theUser.team}\n"
            f"Team ID: {theUser.team_id}\n"
            f"Time Zone: {theUser.time_zone}\n"
            f"Is Admin: {theUser.is_admin}\n"
            f"Is Owner: {theUser.is_owner}\n"
        )

        response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)
        assert response["ok"]

    def handle_app_mention(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = AppMentionEvent(payload)

        # Test function for app mention

        if (
            event.channel_id == self.debug_chan
            and event.user_id != self.bot_user_id
            and "whoami" in event.text.lower()
        ):

            theUser = self.theBot.get_user_as_obj(event.user_id)

            reply = (
                f"User ID: {theUser.id}\n"
                f"Name: {theUser.name}\n"
                f"Display Name: {theUser.displyname}\n"
                f"Real Name: {theUser.real_name}\n"
                f"Email: {theUser.email}\n"
                f"Team: {theUser.team}\n"
                f"Team ID: {theUser.team_id}\n"
                f"Time Zone: {theUser.time_zone}\n"
                f"Is Admin: {theUser.is_admin}\n"
                f"Is Owner: {theUser.is_owner}\n"
            )

            response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)

            assert response["ok"]

        elif (
            event.channel_id == self.debug_chan
            and event.user_id != self.bot_user_id
            and "onboard" in event.text.lower()
        ):
            response = self.bot.chat_postMessage(
                channel=self.debug_chan, blocks=json.dumps(get_onboarding_block())
            )
            assert response["ok"]

        elif event.channel_id == self.debug_chan and event.user_id != self.bot_user_id:
            reply = (
                f"Event Type: {event.type}\n"
                f"User ID: {event.user_id}\n"
                f"Message: {event.text}\n"
                f"Timestamp: {event.ts}\n"
                f"Channel ID: {event.channel_id}\n"
                f"Event TS: {event.event_ts}"
            )

            response = self.bot.chat_postMessage(channel=self.debug_chan, text=reply,)

            assert response["ok"]

        else:
            reply = f"You talking to me, <@{event.user_id}>?!?"

            response = self.bot.chat_postMessage(channel=event.channel_id, text=reply,)
            assert response["ok"]

    def handle_app_home(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = AppHomeEvent(payload)

        response = (
            self.bot.views_publish(
                user_id=event.user_id,
                view=json.dumps(
                    {
                        "type": "home",
                        "title": {"type": "plain_text", "text": "Welcome!"},
                        "blocks": get_onboarding_block(),
                    },
                ),
            ),
        )

        assert response["ok"]

    # TODO: Add endpoint for easy trigger of simple functions (like existing slash commands)

    # def handle_slash_command(self, payload):
    #     """
    #     Returns the list of channels available to the bot.
    #
    #     :return: The list of channels as a dict.
    #     :rtype: dict
    #     """
