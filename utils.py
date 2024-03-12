from timeit import default_timer as timer
from datetime import timedelta
from contextlib import contextmanager
import socket


@contextmanager
def time_it():
    start = timer()
    yield
    end = timer()
    print("--- %s ---" % (timedelta(seconds=end - start)))


def elapsed_timer(func):
    def inner():
        with time_it():
            func()

    return inner


def async_elapsed_timer(func):
    async def inner():
        with time_it():
            await func()

    return inner


def print_ports(req, **kwargs):
    RED = "\033[91m {}\033[00m"
    s = socket.fromfd(req.raw.fileno(), socket.AF_INET, socket.SOCK_STREAM)
    des_port = s.getpeername()[1]
    src_port = s.getsockname()[1]
    print(RED.format(src_port), des_port)
