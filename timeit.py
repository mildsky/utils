import time
from functools import wraps
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.6f} seconds = {total_time * 1e6:.3f} us')
        return result
    return timeit_wrapper

def main():
    @timeit
    def slow_function():
        s = 0
        for i in range(1000):
            s += i
        return s
    
    print(slow_function())

if __name__=="__main__":
    main()
