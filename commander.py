class Commander():
    def listen_message(self, text):
        """
        Listens to all messages
        """
        pass


    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."
        if command.startswith(EXAMPLE_COMMAND):
            response = "Sure...write some more code then I can do that!"
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)
