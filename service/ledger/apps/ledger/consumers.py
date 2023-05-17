import logging
from kombu import Queue, Exchange

from common.events.consumers import AMQPConsumer

# from apps.ledger.callbacks import entry_create_callback

from config.celery import app
from config.queues import ServiceQueue

from celery.bootsteps import ConsumerStep

from kombu import Consumer
from kombu.transport.pyamqp import Channel
from kombu.transport.virtual.base import Message

logger = logging.getLogger('django')

# class EntryCreateConsumer(AMQPConsumer):
#     queue = ServiceQueue.Consumer.entry_create
#     callback = entry_create_callback
#     logger = logger


class EntryCreateConsumer(ConsumerStep):

    def get_consumers(self, channel: Channel) -> list[Consumer]:
        return [
            Consumer(
                channel=channel,
                queues=[
                    Queue(
                        name='dmm-LG-entry-create-c-q',
                        routing_key='dmm-LG-entry-create-c-q',
                        exchange=Exchange(
                            name='dmm-LG-c-x',
                            type='direct',
                            durable=True,
                        ),
                        queue_arguments={'x-queue-type': 'classic'},
                        durable=True,
                    )
                ],
                callbacks=[self.handle_message],
                accept=['json'],
            ),
        ]

    def handle_message(self, body: dict, message: Message) -> None:
        message.ack()
        self.logger.info(f'Consumed a `{type(self).__name__}` event.')
        # self.consume_message(body=body)

    # def consume_message(self, body: dict) -> None:
    #     self.callback(body=body)


app.steps['consumer'].add(EntryCreateConsumer)

print('--------------------', app.control.inspect().stats())
