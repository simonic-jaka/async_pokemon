from timeit import default_timer as timer
from datetime import timedelta
from contextlib import contextmanager
import socket

@contextmanager
def time_it():
    start = timer()
    yield
    end = timer()
    print("--- %s ---" % (timedelta(seconds=end-start)))

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
    s = socket.fromfd(req.raw.fileno(), socket.AF_INET, socket.SOCK_STREAM)
    des_ip, des_port, *_ = s.getpeername()
    src_ip, src_port, *_ = s.getsockname()
    print(src_port, des_port)
