from adapters.rabbitmq import RabbitMQ

def prueba():
    rabbit = RabbitMQ()
    rabbit.connect("William", "Molina")

if __name__ == '__main__':
    prueba()