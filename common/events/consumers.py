from celery.bootsteps import ConsumerStep

from kombu import Consumer
from kombu.transport.pyamqp import Channel
from kombu.transport.virtual.base import Message


class AMQPConsumer(ConsumerStep):

    def get_consumers(self, channel: Channel) -> list[Consumer]:
        return [
            Consumer(
                channel=channel,
                queues=[self.queue],
                callbacks=[self.handle_message],
                accept=['json'],
            ),
        ]

    def handle_message(self, body: dict, message: Message) -> None:
        message.ack()
        self.logger.info(f'Consumed a `{type(self).__name__}` event.')
        self.consume_message(body=body)

    def consume_message(self, body: dict) -> None:
        self.callback(body=body)
