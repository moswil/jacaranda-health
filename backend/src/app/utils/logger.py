import logging.config
import logging
import sys

LOGGING_APPLICATION_CONF = {
    'version': 1,  # required
    'disable_existing_loggers': True,  # this config overrides all other loggers
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s -- %(message)s'
        },
        'sysout': {
            'format': '%(asctime)s\t%(levelname)s -- %(filename)s:%(funcName)s:%(lineno)s -- %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sysout'
        }
    },
    'loggers': {
        'app': {  # 'root' logge
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}


def get_logger():
    """This method sets the configuration for the logger
        Returns:
            [Logger] --  An instance of Logging with the right handlers set
    """
    logging.config.dictConfig(LOGGING_APPLICATION_CONF)
    logger = logging.getLogger(__name__)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s— %(levelname)s —\
                %(funcName)s:%(lineno)d — %(message)s")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger
