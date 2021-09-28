import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    result = 0
    for i in range(10000000):
        result += i * i
    return result


@speed_calc_decorator
def slow_function():
    result = 0
    for i in range(100000000):
        result += i * i
    return result


fast_function()
slow_function()
