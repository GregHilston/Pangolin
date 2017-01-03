class Parser:
    def __init__(self, BOT_ID, AT_BOT):
        self._BOT_ID = BOT_ID
        self._AT_BOT = AT_BOT


    def parse(self, json_list):
        """
        Returns the dictionary of a message, non-message types return None
        """

        if json_list and len(json_list) > 0:
            for dictionary in json_list:

                if dictionary:
                    json_type = str(dictionary["type"])

                    if json_type == "message":
                        text = str(dictionary["text"])

                        print("message received! content {}".format(text))
                        return dictionary
        return None
