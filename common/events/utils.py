from kombu import Queue, Exchange

from common.events.enums import Entity, Service, Type


def get_name(service: Service, type: Type, entity: Entity, **kwargs) -> str:
    name = kwargs.get('name', None)
    if name:
        return f'dmm-{service.value}-{name}-{type.value}-{entity.value}'
    return f'dmm-{service.value}-{type.value}-{entity.value}'


def generate_exchange(name: str) -> Exchange:
    return Exchange(
        name=name,
        type='direct',
        durable=True,
    )


def generate_queue(name: str, exchange: Exchange) -> Queue:
    data = {
        'name': name,
        'routing_key': name,
        'exchange': exchange,
        'queue_arguments': {
            'x-queue-type': 'classic'
        },
        'durable': True,
    }
    return Queue(**data)
