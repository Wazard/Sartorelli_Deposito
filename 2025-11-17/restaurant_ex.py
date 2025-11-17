# Define a class to represent a dish with a name and price
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # String representation for easy printing
    def __str__(self):
        return f"{self.name} - €{self.price:.2f}"


# Define a class to represent a restaurant
class Restaurant:
    def __init__(self, name, kitchen_type, menu=None, open_state=False):
        self.name = name
        self.kitchen_type = kitchen_type
        # Use an empty dictionary if no menu is provided
        self.menu: dict = menu if menu is not None else {}
        self.open_state = open_state

    # Return a description of the restaurant
    def description(self):
        return f"This is {self.name} restaurant, it makes {self.kitchen_type} cuisine and it's currently {'opened' if self.open_state else 'closed'}"

    # Return whether the restaurant is open
    def get_open_state(self):
        return self.open_state

    # Set the open/closed state and print a message
    def set_open_state(self, new_open_state):
        self.open_state = new_open_state
        print(f"Restaurant has been {'opened' if new_open_state else 'closed'}")

    # Add a dish to the menu if it's not already there
    def add_dish_to_menu(self, dish: Dish):
        if dish.name in self.menu.keys():
            print(f"{dish.name} already on menu")
            return
        self.menu[dish.name] = dish.price

    # Remove a dish from the menu by name
    def remove_dish_from_menu(self, dish: Dish):
        self.menu.pop(dish.name)

    # Return a list of string representations of the dishes on the menu
    def get_menu(self):
        return [Dish(name, price).__str__() for name, price in self.menu.items()]


# --- Testing the classes ---

# Create some Dish instances
pizza = Dish("Pizza Margherita", 8.5)
pasta = Dish("Spaghetti Carbonara", 9.0)
salad = Dish("Insalata Mista", 6.0)

# Create a Restaurant instance
r = Restaurant("Trattoria Mirko", "Italian")

# Print restaurant description
print(r.description())  # → This is Trattoria Mirko restaurant, it makes Italian cuisine

# Check and toggle open state
print(r.get_open_state())  # → False
r.set_open_state(True)     # → Restaurant has been opened
print(r.get_open_state())  # → True
r.set_open_state(False)    # → Restaurant has been closed

# Add dishes to the menu
r.add_dish_to_menu(pizza)  # Adds Pizza
r.add_dish_to_menu(pasta)  # Adds Pasta
r.add_dish_to_menu(pizza)  # → Pizza Margherita already on menu

# View current menu
print(r.get_menu())        # → ['Pizza Margherita - €8.50', 'Spaghetti Carbonara - €9.00']

# Remove a dish and view updated menu
r.remove_dish_from_menu(pizza)
print(r.get_menu())        # → ['Spaghetti Carbonara - €9.00']

# Add another dish and view final menu
r.add_dish_to_menu(salad)
print(r.get_menu())        # → ['Spaghetti Carbonara - €9.00', 'Insalata Mista - €6.00']


def restaurant_to_dictionary(dictionary:dict, restaurant:Restaurant):
    dictionary["name"] = restaurant.name
    dictionary["kitchen type"] = restaurant.kitchen_type
    dictionary["menu"] = restaurant.menu
    dictionary["open state"] = restaurant.get_open_state()

