"""
Main Gufi Slackbot class
"""
import slack


class SlackGufi:
    """
    Main Slack Gufi class
    """
    def __init__(self, cfg):
        """
        Constructor
        """
        self._config = None
        self._rtmclient = None
        if "slack" in cfg:
            self._config = cfg["slack"]
        # to include a check on cfg['slack']['api_token']
        self._rtmclient = slack.RTMClient(token=self._config["api_token"], ssl=False)
        self._webclient = slack.WebClient(token=self._config["api_token"], ssl=False)

    def get_token(self):
        """
        Return the API token
        """
        return self._config["api_token"] if "api_token" in self._config else None

    def get_botid(self):
        """
        Return the bot ID
        """
        return self._config["bot_id"] if "bot_id" in self._config else None

    def get_rtmclient(self):
        """
        Return the RTMClient
        """
        return self._rtmclient

    def start(self):
        """
        Start the RTMClient
        """
        return self._rtmclient.start() if self._rtmclient else None

    def send_message(self, text):
        response = self._webclient.chat_postMessage(
            channel='#general',
            text=text)
        assert response["ok"]
        assert response["message"]["text"] == text