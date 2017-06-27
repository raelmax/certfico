import os
import redis

from rq import Worker, Queue, Connection

from certifico import redis_connection

if __name__ == '__main__':
    with Connection(redis_connection):
        worker = Worker(Queue('default'))
        worker.work()
