from timeit import default_timer as timer
from datetime import timedelta
from contextlib import contextmanager

@contextmanager
def timit():
    start = timer()
    yield
    end = timer()
    print("--- %s ---" % (timedelta(seconds=end-start)))

def elapsed_timer(func):
    def inner():
        with timit():
            func()
    return inner

def async_elapsed_timer(func):
    async def inner():
        with timit():
            await func()
    return inner