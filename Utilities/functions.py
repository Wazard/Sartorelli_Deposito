import random

# Generate a list of 10 random integers between 1 and 100
def generate_random_integers() -> list[int]:
    return [random.randint(1, 100) for _ in range(10)]

# Calculate the average of a list of numbers
def get_average(my_list: list[int]) -> float:
    return sum(my_list) / len(my_list) if my_list else 0.0