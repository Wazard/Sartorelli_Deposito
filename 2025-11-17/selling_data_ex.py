import random

# Prompt user to input 10 valid integers
def user_input() -> list[int]:
    tmp_list = []
    count = 0
    while count < 10:
        user_input = input("Insert a number: ")
        if user_input.isdigit():
            tmp_list.append(int(user_input))
            count += 1
        else:
            print("NaN")  # Not a number
    return tmp_list

# Generate a list of 10 random integers between 1 and 100
def generate_random_integers() -> list[int]:
    return [random.randint(1, 100) for _ in range(10)]

# Calculate the average of a list of numbers
def get_average(my_list: list[int]) -> float:
    return sum(my_list) / len(my_list) if my_list else 0.0

# Find the day with the highest average sales
def best_selling_day(dictionary: dict[int, list[int]]) -> tuple[int, float]:
    maximum = 0.0
    max_day = None
    for d, v in dictionary.items():
        curr_average = get_average(v)
        if curr_average >= maximum:
            maximum = curr_average
            max_day = d
    return max_day, maximum

def run_tests():

    # Test: get_average
    avg1 = get_average(generate_random_integers())
    avg2 = get_average([])

    print(avg1)
    print(avg2) # output 0.0

    # Test: best_selling_day
    sales_data = {
        1: [100, 200, 150],
        2: [80, 90, 100],
        3: [300, 250, 400]
    }
    best_day, best_avg = best_selling_day(sales_data)

    print(f"day {best_day} was the best selling day, with an average of €{best_avg:.2f}") # day 3 was the best selling day, with an average of €316.67

run_tests()