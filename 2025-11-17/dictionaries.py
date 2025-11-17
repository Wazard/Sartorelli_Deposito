import random
import string

my_dictionary = {}
my_list = []

def generate_random_values():
    random_bool = random.choice([True, False])
    random_number = random.randint(1, 1000)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # 8-char alphanumeric

    return random_bool, random_number, random_string

my_list += generate_random_values()
my_dictionary["tipididato"] = my_list

for key in my_dictionary:
    print(f"{key}: {my_dictionary[key]}")