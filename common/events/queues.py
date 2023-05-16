from common.events.enums import Entity, Service, Type
from common.events.utils import get_name

ENTITY = Entity.queue


class Queue:

    class Ledger:

        default = get_name(
            service=Service.ledger,
            type=Type.default,
            entity=ENTITY,
        )

        def task_name(name: str) -> str:
            return get_name(
                service=Service.ledger,
                type=Type.task,
                entity=ENTITY,
                name=name,
            )

        class Consumer:

            entry_create = get_name(
                service=Service.ledger,
                type=Type.consumer,
                entity=ENTITY,
                name='entry-create',
            )

    class Wallet:

        default = get_name(
            service=Service.wallet,
            type=Type.default,
            entity=ENTITY,
        )

        def task_name(name: str) -> str:
            return get_name(
                service=Service.wallet,
                type=Type.task,
                entity=ENTITY,
                name=name,
            )
