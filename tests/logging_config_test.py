import logging
from logging_config import LOGGER


def test_logger():
    assert isinstance(LOGGER, logging.RootLogger) is True


def test_logger_level():
    assert LOGGER.getEffectiveLevel() == logging.DEBUG