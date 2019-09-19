from util.util import my_print

class RabbitMQ(object):

    @classmethod
    def connect(cls, user, password):
        my_print(user, password)