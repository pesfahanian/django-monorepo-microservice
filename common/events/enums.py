from enum import Enum


class Service(Enum):
    ledger = 'LG'
    wallet = 'WL'


class Entity(Enum):
    exchange = 'x'
    queue = 'q'


class Type(Enum):
    default = 'd'
    task = 't'
    consumer = 'c'
