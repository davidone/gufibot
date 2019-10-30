import app


def test_main():
    assert app.RGX_MSG == r"^([a-zA-Z0-9]+)$"
    # assert app.SLACK_GUFI is not None
    assert app.LOGGER is not None


def test_rtm_bot_message():
    payload = {
        'subtype': 'bot_message'
    }

    ret_val = app.rtm_message(data=payload)
    assert ret_val is None


def test_rtm_message():
    payload = {
        'subtype': 'message',
        'text': 'this is a test'
    }

    ret_val = app.rtm_message(data=payload)
    assert ret_val is None
