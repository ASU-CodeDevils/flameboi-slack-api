# Primarly based on KevinThePepper's original code with some generic sample onboarding 
# functions from PythOnBoarding 

import logging
import message
import os
from slackclient import SlackClient

from .block_kit_builder.block_generator import BlockGenerator

authed_teams = {}

class Flameboi:
    """
    Methods used to control various features with the Flameboi Slack bot API.
    """

    def __init__(self):
        super(Flameboi, self).__init__()
        self.name = "Flameboi"
        self.emoji = ":flameboi:"
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      # Scopes provide and limit permissions to what our app
                      # can access. It's important to use the most restricted
                      # scope that your app will need.
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        # NOTE: Python-slack requires a client connection to generate
        # an OAuth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        self.client = SlackClient("")
        # We'll use this dictionary to store the state of each message object.
        # In a production environment you'll likely want to store this more
        # persistently in  a database.
        self.messages = {}

    # def __init__(self):
    #     logging.basicConfig(filename='slack.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    #     self.config = load_config()
    #     self.messenger = BlockGenerator(self.config)
    #     self.bot_client = slack.WebClient(token=self.config['app_credentials']['oauth']['bot_user_access_token'],
    #                                       headers={'Accept': 'application/json'})
    #     self.user_client = slack.WebClient(token=self.config['app_credentials']['oauth']['access_token'],
    #                                        headers={'Accept': 'application/json'})

    def auth(self, code):
        """
        Authenticate with OAuth and assign correct scopes.
        Save a dictionary of authed team information in memory on the bot
        object.
        Parameters
        ----------
        code : str
            temporary authorization code sent by Slack to be exchanged for an
            OAuth token
        """
        # After the user has authorized this app for use in their Slack team,
        # Slack returns a temporary authorization code that we'll exchange for
        # an OAuth token using the oauth.access endpoint
        auth_response = self.client.api_call(
                                "oauth.access",
                                client_id=self.oauth["client_id"],
                                client_secret=self.oauth["client_secret"],
                                code=code
                                )
        # To keep track of authorized teams and their associated OAuth tokens,
        # we will save the team ID and bot tokens to the global
        # authed_teams object
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}
        # Then we'll reconnect to the Slack Client with the correct team's
        # bot token
        self.client = SlackClient(authed_teams[team_id]["bot_token"])

    def open_dm(self, user_id):
        """
        Open a DM to send a welcome message when a 'team_join' event is
        recieved from Slack.
        Parameters
        ----------
        user_id : str
            id of the Slack user associated with the 'team_join' event
        Returns
        ----------
        dm_id : str
            id of the DM channel opened by this method
        """
        new_dm = self.client.api_call("im.open",
                                      user=user_id)
        dm_id = new_dm["channel"]["id"]
        return dm_id

    def onboarding_message(self, team_id, user_id):
        """
        Create and send an onboarding welcome message to new users. Save the
        time stamp of this message on the message object for updating in the
        future.
        Parameters
        ----------
        team_id : str
            id of the Slack team associated with the incoming event
        user_id : str
            id of the Slack user associated with the incoming event
        """
        # We've imported a Message class from `message.py` that we can use
        # to create message objects for each onboarding message we send to a
        # user. We can use these objects to keep track of the progress each
        # user on each team has made getting through our onboarding tutorial.

        # First, we'll check to see if there's already messages our bot knows
        # of for the team id we've got.
        if self.messages.get(team_id):
            # Then we'll update the message dictionary with a key for the
            # user id we've received and a value of a new message object
            self.messages[team_id].update({user_id: message.Message()})
        else:
            # If there aren't any message for that team, we'll add a dictionary
            # of messages for that team id on our Bot's messages attribute
            # and we'll add the first message object to the dictionary with
            # the user's id as a key for easy access later.
            self.messages[team_id] = {user_id: message.Message()}
        message_obj = self.messages[team_id][user_id]
        # Then we'll set that message object's channel attribute to the DM
        # of the user we'll communicate with
        message_obj.channel = self.open_dm(user_id)
        # We'll use the message object's method to create the attachments that
        # we'll want to add to our Slack message. This method will also save
        # the attachments on the message object which we're accessing in the
        # API call below through the message object's `attachments` attribute.
        message_obj.create_attachments()
        post_message = self.client.api_call("chat.postMessage",
                                            channel=message_obj.channel,
                                            username=self.name,
                                            icon_emoji=self.emoji,
                                            text=message_obj.text,
                                            attachments=message_obj.attachments
                                            )
        timestamp = post_message["ts"]
        # We'll save the timestamp of the message we've just posted on the
        # message object which we'll use to update the message after a user
        # has completed an onboarding task.
        message_obj.timestamp = timestamp

    def update_emoji(self, team_id, user_id):
        """
        Update onboarding welcome message after recieving a "reaction_added"
        event from Slack. Update timestamp for welcome message.
        Parameters
        ----------
        team_id : str
            id of the Slack team associated with the incoming event
        user_id : str
            id of the Slack user associated with the incoming event
        """
        # These updated attachments use markdown and emoji to mark the
        # onboarding task as complete
        completed_attachments = {"text": ":white_check_mark: "
                                         "~*Add an emoji reaction to this "
                                         "message*~ :thinking_face:",
                                 "color": "#439FE0"}
        # Grab the message object we want to update by team id and user id
        message_obj = self.messages[team_id].get(user_id)
        # Update the message's attachments by switching in incomplete
        # attachment with the completed one above.
        message_obj.emoji_attachment.update(completed_attachments)
        # Update the message in Slack
        post_message = self.client.api_call("chat.update",
                                            channel=message_obj.channel,
                                            ts=message_obj.timestamp,
                                            text=message_obj.text,
                                            attachments=message_obj.attachments
                                            )
        # Update the timestamp saved on the message object
        message_obj.timestamp = post_message["ts"]

    def update_pin(self, team_id, user_id):
        """
        Update onboarding welcome message after receiving a "pin_added"
        event from Slack. Update timestamp for welcome message.
        Parameters
        ----------
        team_id : str
            id of the Slack team associated with the incoming event
        user_id : str
            id of the Slack user associated with the incoming event
        """
        # These updated attachments use markdown and emoji to mark the
        # onboarding task as complete
        completed_attachments = {"text": ":white_check_mark: "
                                         "~*Pin this message*~ "
                                         ":round_pushpin:",
                                 "color": "#439FE0"}
        # Grab the message object we want to update by team id and user id
        message_obj = self.messages[team_id].get(user_id)
        # Update the message's attachments by switching in incomplete
        # attachment with the completed one above.
        message_obj.pin_attachment.update(completed_attachments)
        # Update the message in Slack
        post_message = self.client.api_call("chat.update",
                                            channel=message_obj.channel,
                                            ts=message_obj.timestamp,
                                            text=message_obj.text,
                                            attachments=message_obj.attachments
                                            )
        # Update the timestamp saved on the message object
        message_obj.timestamp = post_message["ts"]

    def update_share(self, team_id, user_id):
        """
        Update onboarding welcome message after recieving a "message" event
        with an "is_share" attachment from Slack. Update timestamp for
        welcome message.
        Parameters
        ----------
        team_id : str
            id of the Slack team associated with the incoming event
        user_id : str
            id of the Slack user associated with the incoming event
        """
        # These updated attachments use markdown and emoji to mark the
        # onboarding task as complete
        completed_attachments = {"text": ":white_check_mark: "
                                         "~*Share this Message*~ "
                                         ":mailbox_with_mail:",
                                 "color": "#439FE0"}
        # Grab the message object we want to update by team id and user id
        message_obj = self.messages[team_id].get(user_id)
        # Update the message's attachments by switching in incomplete
        # attachment with the completed one above.
        message_obj.share_attachment.update(completed_attachments)
        # Update the message in Slack
        post_message = self.client.api_call("chat.update",
                                            channel=message_obj.channel,
                                            ts=message_obj.timestamp,
                                            text=message_obj.text,
                                            attachments=message_obj.attachments
                                            )
        # Update the timestamp saved on the message object
        message_obj.timestamp = post_message["ts"]

    def send_onboarding_message(self, user_email: str) -> dict:
        """
        Sends the onboarding message to a user.

        :param user_email: The email of the user to be on-boarded.
        :type user_email: str
        :return: The response from the message request as a dict.
        :rtype: dict
        """
        user = self.get_user_by_email(email=user_email)['user']['id']
        response = self.bot_client.conversations_open(users=[user])
        if not response['ok']:
            return response

        channel = response['channel']['id']
        message = self.messenger.get_welcome_block(channel=channel)
        return self._send_block_message(message=message)

    def send_message(self, channel: str, text: str, mention_email: str = None) -> dict:
        """
        Sends a message (either text or block) to a channel. An optional mention can be added to the beginning of the
        message.

        :param channel: The name of the channel to send the message to.
        :type channel: str
        :param text: The message to send.
        :type text: str
        :param mention_email: The email of the user to mention, default is None.
        :type mention_email: str
        :return: The result of sending the message.
        """

        if mention_email:
            username = self.get_user_by_email(mention_email)['user']['name']
            text = '@{} {}'.format(username, text)
        message = self.messenger.get_message_payload(text=text, channel=channel)
        return self._send_block_message(message=message)

    def add_member(self, user_email: str) -> dict:
        """
        This method does not work yet. Enterprise grid access is required for the app to be able to add/remove users
        from the team.

        Adds a member to the workspace using their member ID.

        :param user_email: The Slack ID of the user.
        :type user_email: str
        :return: The response of the member addition request.
        :rtype: dict
        """
        user = self.get_user_by_email(email=user_email)['user']
        channel = self.get_channel_id(channel_name='hangout')
        return self.user_client.channels_invite(channel=channel, user=user['id'])

    def get_slack_client(self):
        """
        Returns the slack web client. Used for if the commands in this module do not suffice for specific use cases.

        :return: The slack client.
        :rtype: slack.WebClient
        """
        return self.bot_client

    def get_user_by_email(self, email: str) -> dict:
        """
        Retrieves a user by their email.

        :param email: The email address of the user.
        :type email: str
        :return: The user as a dict.
        :rtype: dict
        """
        return self.bot_client.users_lookupByEmail(email=email)

    def get_users_list(self) -> dict:
        """
        Returns a list of users.

        :return: A list of users. See https://api.slack.com/methods/users.list for format.
        :rtype: dict
        """
        return self.bot_client.users_list()

    def get_channel_id(self, channel_name: str) -> str:
        """
        Returns the channel ID based on the name. If no ID is found, then none is returned.

        :param channel_name: The name of the channel as a string (w/o the leading hashtag).
        :type channel_name: str
        :return: The channel id as a string.
        :rtype: str
        """
        channel_list = self.get_channel_list()
        for channel in channel_list:
            if channel['name'] == channel_name:
                return channel['id']

        return str(None)

    def get_channel_list(self) -> dict:
        """
        Returns the list of channels available to the bot.

        :return: The list of channels as a dict.
        :rtype: dict
        """
        return self.bot_client.channels_list()

    def _send_block_message(self, message: dict, user_id: int = 0) -> dict:
        """
        Block message util to send a message using the bot client.

        :param message: Markdown-supported message to be sent.
        :type message: dict
        :param user_id: The user ID (if any) of the user the message was sent to.
        :type user_id: int, optional
        :return: The response from sending the message as a dict.
        :rtype: dict
        """
        return self.bot_client.chat_postMessage(**message)
