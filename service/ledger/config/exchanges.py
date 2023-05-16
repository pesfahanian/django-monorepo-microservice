from common.events.exchanges import Exchange
from common.events.utils import generate_exchange


class ServiceExchange:
    default = generate_exchange(Exchange.Ledger.default)
    task = generate_exchange(Exchange.Ledger.task)
    consumer = generate_exchange(Exchange.Ledger.task)
