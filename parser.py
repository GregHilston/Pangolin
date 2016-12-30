class Parser:
    def __init__(self, BOT_ID, AT_BOT):
        self._BOT_ID = BOT_ID
        self._AT_BOT = AT_BOT


    def parse(self, json):
        """
            Returns author name and messaged directed at this Bot, otherwise
            returns None
        """
        print("json {}".format(str(json)))

        if json and len(json) > 0:
            for val in json:
                print("val {}".format(str(val)))

                if val and 'content' in json and self._AT_BOT in output['content']:
                    # return text after the @ mention, whitespace removed
                    return output['content'].split(self._AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None
