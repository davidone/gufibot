import slack
from logging_config import logger


class SlackGufi(object):
    def __init__(self, cfg):
        self._config = None
        self._rtmclient = None
        if "slack" in cfg:
            self._config = cfg["slack"]
        # to include a check on cfg['slack']['api_token']
        self._rtmclient = slack.RTMClient(token=self._config["api_token"], ssl=False)

    def get_token(self):
        return self._config["api_token"] if "api_token" in self._config else None

    def get_botid(self):
        return self._config["bot_id"] if "bot_id" in self._config else None

    def start(self):
        if self._rtmclient is None:
            return -1
        try:
            self._rtmclient.start()
        except Exception as e:
            logger.error(f"{e}")
            return -1
