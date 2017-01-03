import time, os
from slackclient import SlackClient
from parser import Parser
from decoder import Decoder
from commander import Commander


class SlackBot:
    def __init__(self):
        self._BOT_ID = os.environ.get("BOT_ID")
        self._AT_BOT = "<@" + str(self._BOT_ID) + ">"
        self._SLACK_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
        self._slack_client = SlackClient(self._SLACK_TOKEN)
        self._parser = Parser(self._BOT_ID, self._AT_BOT)
        self._decoder = Decoder(self._SLACK_TOKEN)
        self._commander = Commander()


    def connect(self):
        """
        Connect the slack bot to the chatroom
        """

        READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose

        if self._slack_client.rtm_connect():
            print("{} connected and running!".format(self._BOT_ID))

            while True:
                json_list = self._slack_client.rtm_read()
                dictionary = self._parser.parse(json_list)

                if dictionary:
                    dictionary = self._decoder.decode(dictionary) # Potentially encoded values
                    self._commander.listen_message(dictionary)

                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Are you connected to the internet? Invalid Slack token or bot ID?")
