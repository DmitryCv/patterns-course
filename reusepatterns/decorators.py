import time
import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        val = func(*args, **kwargs)
        end_time = time.perf_counter()
        interval = end_time - start_time
        print(f'Function name: {func.__name__}, execution time: {interval:.5f} sec.')
        return val
    return wrapper
