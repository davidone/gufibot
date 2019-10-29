import pytest
from logging_config import logger
import slack
from unittest.mock import Mock, patch
from gufi import SlackGufi


class TestGufi(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('slack.RTMClient')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_rtmclient(self):
        self.mock_get.return_value = Mock(ok=True)
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foobar"
        sg_rtm = SlackGufi(cfg).get_rtmclient()
        assert sg_rtm is not None

    def test_get_token(self):
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foobar"
        sg = SlackGufi(cfg)
        assert sg.get_token() == "foobar"

    def test_get_botid(self):
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foo"
        cfg['slack']['bot_id'] = "bar"
        sg = SlackGufi(cfg)
        assert sg.get_botid() == "bar"
