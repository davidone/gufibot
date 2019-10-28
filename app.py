import yaml
import os
import re
import slack
from gufi import SlackGufi
from logging_config import logger

RGX_MSG = r"^([a-zA-Z0-9]+)$"


@slack.RTMClient.run_on(event="message")
def rtm_message(**payload):
    data = payload["data"]
    if "subtype" in data and data["subtype"] == "bot_message":
        # We don't reply to bots, only humans
        return
    # logger.debug(f"{data}")
    web_client = payload["web_client"]
    text = data.get("text", [])
    re_text = re.match(RGX_MSG, text)
    if re_text is None or len(re_text.groups()) == 0:
        return

    if type(text) == str and text.lower() == "fortune":
        fortune_path = "/usr/local/bin/fortune"
        if not (os.path.isfile(fortune_path) or os.access(fortune_path, os.X_OK)):
            fortune_out = f"{fortune_path} not available"
        else:
            fortune_out = os.popen(fortune_path).read()
        channel_id = data["channel"]
        web_client.chat_postMessage(channel=channel_id, text=f"```{fortune_out}```")


if __name__ == "__main__":
    try:
        with open("config.yaml", "r") as stream:
            cfg_yaml = yaml.safe_load(stream)
    except FileNotFoundError as e:
        print(f"{e}")
        exit(e.errno)
    slack_gufi = SlackGufi(cfg_yaml)
    logger.info(f"Application started")
    slack_gufi.start()
