import json
import os
import re
import flameboi.modules_admin.debug as debug
import flameboi.modules_admin.meeting as meeting
import flameboi.common.events as events

from flameboi.common.objects import User
import flameboi.views.app_home as views
from flameboi.modules_user.playlists import get_playlist_block


class Router:
    """
    Methods used to router/direct events within the Flameboi Slack bot API.

    :return: The list of channels as a dict.
    :rtype: dict
    """

    def __init__(self, theBot):
        self.bot = theBot.getClient()
        self.admin = theBot.getAdmin()
        self.theBot = theBot

        # Import various ID's for filtering via dotenv
        self.bot_id = os.getenv("BOT_ID")
        self.bot_user_id = os.getenv("USER_ID")
        self.bot_app_id = os.getenv("APP_ID")
        self.cd_team_id = os.getenv("CODE_DEVILS_TEAM_ID")
        self.home_channel = os.getenv("HOME_CHAN_ID")
        self.debug_chan = os.getenv("DEBUG_CHAN_ID")
        self.stu_user = os.getenv("STU_ID")
        self.jer_user = os.getenv("JER_ID")
        self.cal_user = os.getenv("GCAL_ID")
        self.seth_user = os.getenv("SETH_ID")
        self.pol_chan = os.getenv("POL_CHAN")

    # def handle_slash_command(self, payload):

    #     event = events.SlashCommand(payload)

    #     self.text_sender_test(self.debug_chan, event.raw)

    def handle_team_join(self, payload):
        """
        Handles a Member Joined Team event.  Currently passes event to a debug function which posts
        various details on the user and channel involved to the logging channel. Also DM's specified
        admin the information of the new user.

        :return: None.
        """

        event = events.TeamJoinEvent(payload)

        reply = debug.team_join(event)

        self.text_sender_test(self.debug_chan, reply)

        dm_chan = (
            self.bot.conversations_open(users=self.jer_user)
            .get("channel", {})
            .get("id")
        )

        self.text_sender_test(dm_chan, reply)

    def handle_reaction_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = events.ReactionAddedEvent(payload)

        reactions_posted = (
            self.bot.reactions_get(channel=event.item_channel, timestamp=event.item_ts)
            .get("message", {})
            .get("reactions", [])
        )

        if event.user_id != self.bot_user_id:

            self.text_sender_test(self.debug_chan, debug.reaction_add(event))

            already_posted = False

            for react in reactions_posted:
                if self.bot_user_id in react.get("users", []):
                    already_posted = True
                    break

            if not already_posted:

                if event.reaction and event.reaction == "parrot":
                    for i in range(1, 10):

                        response = self.bot.reactions_add(
                            name=f"parrotwave{i}",
                            channel=event.item_channel,
                            timestamp=event.item_ts,
                        )
                        assert response["ok"]

                elif event.reaction and "fuckyou" in event.reaction:

                    # res = self.admin.reactions_remove(
                    #     name="fuckyouadmin",
                    #     channel=event.item_channel,
                    #     timestamp=event.item_ts,
                    # )
                    # assert res["ok"]

                    self.text_sender_test(
                        chan=event.item_channel,
                        txt=f"That's not very nice <@{event.user_id}>!",
                    )

                    response = self.bot.reactions_add(
                        name="heart",
                        channel=event.item_channel,
                        timestamp=event.item_ts,
                    )
                    assert response["ok"]

                else:

                    self.text_sender_test(
                        self.debug_chan, f"Not yet reacted, adding :{event.reaction}:\n"
                    )
                    response = self.bot.reactions_add(
                        name=event.reaction,
                        channel=event.item_channel,
                        timestamp=event.item_ts,
                    )
                    assert response["ok"]

            elif already_posted and event.user_id:
                self.text_sender_test(
                    chan=self.debug_chan,
                    txt=f"Already reacted to item/message, not reacting to :{event.reaction}:.\n",
                )

        else:
            self.text_sender_test(
                chan=self.debug_chan,
                txt=f"Not responding to bot reaction :{event.reaction}:.\n",
            )

    def handle_pin_added(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = events.PinAddedEvent(payload)

        self.text_sender_test(self.debug_chan, debug.pin_add(event))

    def handle_message(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = events.MessageEvent(payload)

        if os.getenv("SWATTER") == "1" and event.user_id != self.bot_id:
            if event.subtype == "bot_message" or event.user_id == os.getenv("BOT1"):
                delete = self.admin.chat_delete(
                    channel=event.channel_id,
                    ts=event.ts,
                )
                assert delete["ok"]

                self.text_sender_test(chan=event.channel_id, txt="One bot left...")

        if (
            event.subtype == "None"
            and event.channel_id == self.debug_chan
            and event.user_id != self.bot_user_id
        ):

            self.text_sender_test(self.debug_chan, debug.message(event))

        if event.channel_id == self.pol_chan and event.user_id == "USLACKBOT":
            delete = self.admin.chat_delete(channel=event.channel_id, ts=event.ts)
            assert delete["ok"]

            response = self.bot.chat_postMessage(
                channel=event.channel_id, text="Get out of here..."
            )
            assert response["ok"]

            # if "delete this" in event.text:

            #     delete = self.admin.chat_delete(channel=event.channel_id, ts=event.ts,)
            #     assert delete["ok"]

            #     response = self.bot.chat_postMessage(
            #         channe=self.debug_chan, text="Deleted Message"
            #     )
            #     assert response["ok"]

        if event.channel_id != self.debug_chan:
            self.text_sender_test(self.debug_chan, debug.message(event=event))

    def handle_channel_join(self, payload):
        """
        Handles a Member Joined Channel event.  Currently passes event to a debug function which posts
        various details on the user and channel involved to the loggin channel.

        :return: None.
        """

        event = events.MemberJoinedChannelEvent(payload)

        theUser = self.theBot.get_user_as_obj(event.user_id)

        self.text_sender_test(self.debug_chan, debug.channel_join(event, theUser))

    def handle_app_mention(self, payload):
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """

        event = events.AppMentionEvent(payload)

        if event.user_id == self.stu_user or event.user_id == self.seth_user:
            if "bot-b-gone" in event.text.lower() and os.getenv("SWATTER") == "0":
                os.environ["SWATTER"] = "1"
                self.text_sender_test(chan=event.channel_id, txt="Bot-B-Gone Enabled")
            elif "bot-b-gone" in event.text.lower() and os.getenv("SWATTER") == "1":
                os.environ["SWATTER"] = "0"
                self.text_sender_test(chan=event.channel_id, txt="Bot-B-Gone Disabled")

        if (
            event.channel_id == self.debug_chan
            and event.user_id != self.bot_user_id
            and "whoami" in event.text.lower()
        ):

            theUser = self.theBot.get_user_as_obj(event.user_id)
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

            self.text_sender_test(self.debug_chan, deets)

        elif (
            event.channel_id == self.debug_chan
            and event.user_id != self.bot_user_id
            and "lookup" in event.text.lower()
        ):

            regex = r"[ ]*[a-z0-9]+[\._]?[a-z0-9]+[@]asu.edu"
            comp = re.compile(regex)
            eml = comp.search(event.text)
            plain = eml.group().strip()

            theUser = User(self.bot.users_lookupByEmail(email=plain).get("user", {}))

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

            self.text_sender_test(self.debug_chan, deets)

        # elif (
        #     event.channel_id == self.debug_chan
        #     and event.user_id != self.bot_user_id
        #     and "onboard" in event.text.lower()
        # ):
        #     self.block_sender_test(self.debug_chan, get_onboarding_block)

        # elif event.user_id != self.bot_user_id and "qod" in event.text.lower():

        #     self.ephemeral_sender(
        #         user=event.user_id,
        #         channel=event.channel_id,
        #         text="",
        #         func=get_qod_block,
        #     )

        elif event.user_id != self.bot_user_id and "playlists" in event.text.lower():

            self.block_sender_test(event.channel_id, get_playlist_block)

        elif event.user_id == self.stu_user or event.user_id == self.seth_user:
            if "meeting" in event.text.lower():

                if "now" in event.text.lower():
                    self.block_sender_test(
                        os.getenv("HOME_CHAN_ID"), meeting.get_meeting_now
                    )
                elif "hour" in event.text.lower():
                    self.block_sender_test(
                        os.getenv("HOME_CHAN_ID"), meeting.get_meeting_hour
                    )

        if event.user_id != self.bot_user_id:

            self.text_sender_test(self.debug_chan, debug.app_mention(event))

    def handle_app_home(self, payload):
        """
        Handles a App Home Opened event.  Tests to see if the user has a home or a home with an outdated
        external_id (not conforming to the {user_id}_home syntax).  If true, calls a function to publish
        a new view to the user's app home view.  If the view exists and is of the proper form, does nothing.

        :return: None.
        """
        event = events.AppHomeEvent(payload)

        # # Debuggin output commented out.
        # self.text_sender_test(
        #     self.debug_chan,
        #     f"Event: App Home Opened\nUser ID: <@{event.user_id}>\n
        #     View ID: {event.view_id}\nExternal ID: {event.ext_id}\n",
        # )

        if event.ext_id is None or f"{event.user_id}_home" not in event.ext_id:

            views.publish_init_home(event.user_id, self.theBot)
        #     self.text_sender_test(self.debug_chan, "Home updated")

        # else:
        #     self.text_sender_test(self.debug_chan, "Home not updated.")

    #
    # Just used here for experimentation... will be moved to Messenger once complete.
    #

    def ephemeral_sender(
        self,
        user: str,
        channel: str,
        text: str,
        func=None,
        attach: list = None,
    ):

        blkout = json.dumps(func()) if func else None
        attout = json.dumps(attach) if attach else None

        response = self.bot.chat_postEphemeral(
            user=user, channel=channel, text=text, blocks=blkout, attachments=attout
        )
        assert response["ok"]

    def block_sender_test(self, chan, get_blk):

        response = self.bot.chat_postMessage(channel=chan, blocks=json.dumps(get_blk()))
        assert response["ok"]

    def text_sender_test(self, chan, txt):

        response = self.bot.chat_postMessage(channel=chan, text=txt)
        assert response["ok"]

    def reaction_sender_test(self, reaction: str, channel: str, timestamp: str):

        response = self.bot.reactions_add(
            name=reaction,
            channel=channel,
            timestamp=timestamp,
        )
        assert response["ok"]
