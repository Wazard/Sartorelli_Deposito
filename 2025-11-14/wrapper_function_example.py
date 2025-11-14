import time

def time_calc(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"execution time: {end_time - start_time} seconds")
        return result
    return wrapper


@time_calc
def slow_calc():
    time.sleep(2)
    print("Calculation completed")

# wrapper call
slow_calc()
