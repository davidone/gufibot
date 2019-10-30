import pytest
import slack
from unittest.mock import Mock, patch
import gufi


class TestGufi(object):
    @classmethod
    def setup_class(cls):
        cls.mock_rtm_patcher = patch('slack.RTMClient')
        cls.mock_rtm = cls.mock_rtm_patcher.start()
        cls.mock_gufi_patcher = patch('gufi.SlackGufi.send_message')
        cls.mock_gufi = cls.mock_gufi_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_rtm_patcher.stop()
        cls.mock_gufi_patcher.stop()

    def test_rtmclient(self):
        self.mock_rtm.return_value = Mock()
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foobar"
        sg_rtm = gufi.SlackGufi(cfg).get_rtmclient()
        assert sg_rtm is not None

    def test_get_token(self):
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foobar"
        sg = gufi.SlackGufi(cfg)
        assert sg.get_token() == "foobar"

    def test_get_botid(self):
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foo"
        cfg['slack']['bot_id'] = "bar"
        sg = gufi.SlackGufi(cfg)
        assert sg.get_botid() == "bar"

    def test_send_message(self):
        resp = {'ok': True, 'message': {'text': "text"}}
        self.mock_gufi.return_value = Mock()
        self.mock_gufi.return_value.json.return_value = resp
        cfg = {}
        cfg['slack'] = {}
        cfg['slack']['api_token'] = "foo"
        cfg['slack']['bot_id'] = "bar"
        sg = gufi.SlackGufi(cfg)
        ret_val = sg.send_message("text")
        assert ret_val.json() == resp
