from timeit import default_timer as timer
from datetime import timedelta

def elapsed_timer(func):
    def inner():
        start = timer()
        func()
        end = timer()
        print("--- %s seconds ---" % (timedelta(seconds=end-start)))
    return inner