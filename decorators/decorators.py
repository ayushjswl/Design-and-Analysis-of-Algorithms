import time
import random
import functools

def time_units(seconds):
    if seconds >= 1:
        return round(seconds, 3)   
    else:
        ms = seconds * 1e3
        return round(ms, 3)


def timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):#(*args, **kwargs) to handle all posible arguments *args is a tuple for positional arguments and kwargs is a dictionary of keyword arguments
        start_time = time.perf_counter()
        result = f(*args, **kwargs)
        stop_time = time.perf_counter()
        elapsed_time = time_units(stop_time - start_time) 
        print(f"Time Taken : {elapsed_time}")
        return [elapsed_time, result]
    return wrapper


def random_array(min = 0, max = 999):
    def decorator(func):
        def wrapper(*sizes, **kwargs):
            results = []
            for size in sizes:
                arr = [random.randint(min, max) for _ in range(size)]
                res = func(arr, **kwargs)
                results.append(res)
            return results
        return wrapper
    return decorator