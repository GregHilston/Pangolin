import time
from slackclient import SlackClient
from parser import Parser
from commander import Commander

# BOT_ID = os.environ.get("BOT_ID") # starterbot's ID as an environment variable
# SLACK_BOT_TOEKN = os.environ.get('SLACK_BOT_TOKEN')
# slack_client = SlackClient() # instantiate Slack & Twilio clients

class SlackBot:
    def __init__(self):
        self._BOT_ID = "pangolin"
        self._AT_BOT = "<@" + str(self._BOT_ID) + ">"
        self._SLACK_TOKEN = "xoxb-117271731920-X4MHwxePsMDC6lovijQRXj1d"
        self._slack_client = SlackClient(self._SLACK_TOKEN)
        self._parser = Parser(self._BOT_ID, self._AT_BOT)
        self._commander = Commander()

    def connect(self):
        """
        Connect the slack bot to the chatroom
        """

        READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose

        if self._slack_client.rtm_connect():
            print("StarterBot connected and running!")
            while True:
                json = self._slack_client.rtm_read()
                command, channel = self._parser.parse(json)

                if command and channel:
                    self._commander.handle_command(command, channel)

                time.sleep(READ_WEBSOCKET_DELAY)
        else:
            print("Connection failed. Invalid Slack token or bot ID?")
