import time

def exec_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1000  # convert to ms
        return f"execution time: {round(elapsed_ms, 3)} ms", result
    return wrapper

def function_printer(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(result)
        return result
    return wrapper