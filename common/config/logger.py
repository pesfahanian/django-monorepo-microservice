import logging

services = [
    'wallet',
    'ledger',
    'pg',
]


class CustomFilter(logging.Filter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filter_items = [
            'GET /static/',
            '"GET /static/',
            'GET /favicon.ico',
            '"GET /favicon.ico',
            'Not Found: /static/',
            '"Not Found: /static/',
            'Not Found: /favicon.ico',
            '"Not Found: /favicon.ico',
        ]
        self.filter_items += [
            f'GET /api/v1/{service}/healthcheck/' for service in services
        ]
        self.filter_items += [
            f'"GET /api/v1/{service}/healthcheck/' for service in services
        ]

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        return all([
            not message.startswith(filter_item)
            for filter_item in self.filter_items
        ]) and (not 'svg' in message)


class CustomFormat(logging.Formatter):
    grey = '\x1b[38;21m'
    green = '\x1b[32;21m'
    yellow = '\x1b[33;21m'
    red = '\x1b[31;21m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    format = '[%(asctime)s] %(levelname)s | %(message)s (%(filename)s:%(lineno)d)'

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record: logging.LogRecord) -> logging.LogRecord:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
