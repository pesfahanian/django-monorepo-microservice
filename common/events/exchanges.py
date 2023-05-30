from common.events.enums import Entity, Service, Type
from common.events.utils import get_name

ENTITY = Entity.exchange


class Exchange:
    class Ledger:

        default = get_name(
            service=Service.ledger,
            type=Type.default,
            entity=ENTITY,
        )
        task = get_name(
            service=Service.ledger,
            type=Type.task,
            entity=ENTITY,
        )
        consumer = get_name(
            service=Service.ledger,
            type=Type.consumer,
            entity=ENTITY,
        )

    class Wallet:

        default = get_name(
            service=Service.wallet,
            type=Type.default,
            entity=ENTITY,
        )
        task = get_name(
            service=Service.wallet,
            type=Type.task,
            entity=ENTITY,
        )
