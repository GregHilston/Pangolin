import requests


class Decoder:
    def __init__(self, SLACK_TOKEN):
        self._SLACK_TOKEN = SLACK_TOKEN


    def decode(self, dictionary):
        if dictionary:
            if dictionary["channel"]:
                dictionary["channel"] = self.decode_channel(dictionary["channel"])
            if dictionary["user"]:
                dictionary["user"] = self.decode_user(dictionary["user"])
        return None


    def decode_channel(self, coded_channel):
        if coded_channel:
            payload = {'token': self._SLACK_TOKEN, 'channel': coded_channel}
            response = requests.get('https://slack.com/api/channels.info', params=payload)
            response_data = response.json()
            print("Decoded channel from {} to {}".format(str(coded_channel), str(response_data["channel"]["name"])))
            return response_data["channel"]["name"]
        return None


    def decode_user(self, coded_user):
        if coded_user:
            payload = {'token': self._SLACK_TOKEN, 'user': coded_user}
            response = requests.get('https://slack.com/api/users.info', params=payload)
            response_data = response.json()
            print("Decoded user from {} to {}".format(str(coded_user), str(response_data["user"]["name"])))
            return response_data["user"]["name"]
        return None
