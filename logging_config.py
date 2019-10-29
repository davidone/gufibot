"""
Define a logging instance
"""
import logging

LOGGER = logging.getLogger()
HANDLER = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.DEBUG)
