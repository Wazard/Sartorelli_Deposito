import random

# Generate a list of 10 random integers between 1 and 100
def generate_random_integers() -> list[int]:
    return [random.randint(1, 100) for _ in range(10)]

# Calculate the average of a list of numbers
def get_average(my_list: list[int]) -> float:
    return sum(my_list) / len(my_list) if my_list else 0.0

def at_least_one_present(**kwargs):
    provided = [k for k, v in kwargs.items() if v is not None]
    if len(provided) < 1:
        return False
    return True