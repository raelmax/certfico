from rq import Worker, Queue, Connection

from certifico import redis_connection

def main():
    with Connection(redis_connection):
        worker = Worker(Queue('default'))
        worker.work()
