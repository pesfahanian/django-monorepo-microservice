from common.events.exchanges import Exchange
from common.events.utils import generate_exchange


class ServiceExchange:
    default = generate_exchange(Exchange.Wallet.default)
    task = generate_exchange(Exchange.Wallet.task)


class ProducerExchange:
    ledger = generate_exchange(Exchange.Ledger.consumer)
