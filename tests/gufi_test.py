import pytest

from gufi import SlackGufi


def test_get_token():
    cfg = {}
    cfg['slack'] = {}
    cfg['slack']['api_token'] = "foobar"
    sg = SlackGufi(cfg)
    assert sg.get_token() == "foobar"


def test_get_botid():
    cfg = {}
    cfg['slack'] = {}
    cfg['slack']['api_token'] = "foo"
    cfg['slack']['bot_id'] = "bar"
    sg = SlackGufi(cfg)
    assert sg.get_botid() == "bar"
