# Base product class with name, cost, and price
class Product:
    def __init__(self, name: str, production_cost: float, price: float) -> None:
        self.name: str = name
        self.production_cost: float = production_cost
        self.price: float = price

    # Calculate profit as price minus production cost
    def calculate_profit(self) -> float:
        return self.price - self.production_cost

    # String representation for display
    def __str__(self) -> str:
        return (
            f"{self.name}: Price €{self.price:.2f}, "
            f"Cost €{self.production_cost:.2f}, "
            f"Profit €{self.calculate_profit():.2f}"
        )


# Parallel class for electronic products
class ProductElectronic:
    def __init__(self, name: str, production_cost: float, price: float,
                warranty_years: int, power_usage_watts: float) -> None:
        self.name = name
        self.production_cost = production_cost
        self.price = price
        self.warranty_years = warranty_years
        self.power_usage_watts = power_usage_watts

    def calculate_profit(self) -> float:
        return self.price - self.production_cost

    def __str__(self) -> str:
        return (
            f"{self.name}: Price €{self.price:.2f}, "
            f"Cost €{self.production_cost:.2f}, "
            f"Profit €{self.calculate_profit():.2f}, "
            f"Warranty years {self.warranty_years:.2f}, "
            f"Wattage {self.power_usage_watts:.1f}W"
        )


# Parallel class for clothing products
class ProductDressing:
    def __init__(self, name: str, production_cost: float, price: float,
                size: str, material: str) -> None:
        self.name = name
        self.production_cost = production_cost
        self.price = price
        self.size = size
        self.material = material

    def calculate_profit(self) -> float:
        return self.price - self.production_cost

    def __str__(self) -> str:
        return (
            f"{self.name}: Price €{self.price:.2f}, "
            f"Cost €{self.production_cost:.2f}, "
            f"Profit €{self.calculate_profit():.2f}, "
            f"Size {self.size}, "
            f"Material {self.material}"
        )


# Factory class to manage inventory and sales
class ProductFactory:

    def __init__(self) -> None:
        self.inventory: dict[str, int] = {}  # Maps product name to quantity

    # Add product to inventory
    def add_product(self, product, quantity: int) -> None:
        if product.name in self.inventory:
            self.inventory[product.name] += quantity
        else:
            self.inventory[product.name] = quantity
        print(f"Added {quantity} units of {product.name}")

    # Sell an electronic product
    def sell_product_electronic(self, product: ProductElectronic, quantity: int) -> None:
        self._process_sale(product.name, quantity, product.price, product.calculate_profit())

    # Sell a dressing product
    def sell_product_dressing(self, product: ProductDressing, quantity: int) -> None:
        self._process_sale(product.name, quantity, product.price, product.calculate_profit())

    # Sell a generic product
    def sell_product(self, product: Product, quantity: int) -> None:
        self._process_sale(product.name, quantity, product.price, product.calculate_profit())

    # Internal sale logic
    def _process_sale(self, name: str, quantity: int, price: float, profit: float) -> None:
        if name not in self.inventory or self.inventory[name] < quantity:
            print(f"Not enough stock to sell {quantity} units of {name}")
            return
        self.inventory[name] -= quantity
        total_earnings = price * quantity
        total_profit = profit * quantity
        print(f"Sold {quantity} units of {name} for €{total_earnings} total earnings, making €{total_profit} profit")

    # Return product to inventory
    def return_product(self, product, quantity: int) -> None:
        if product.name in self.inventory:
            self.inventory[product.name] += quantity
        else:
            self.inventory[product.name] = quantity
        print(f"Returned {quantity} units of {product.name}")

    # Display current inventory
    def show_inventory(self) -> None:
        print("Current Inventory:")
        for name, qty in self.inventory.items():
            print(f" - {name}: {qty} units")


def run_tests():
    # Create products
    laptop = ProductElectronic("Laptop X200", 500.0, 899.0, 2, 65)
    shirt = ProductDressing("Cotton Shirt", 10.0, 29.99, "M", "Cotton")
    generic = Product("Generic Mug", 2.0, 5.0)

    # Create factory
    factory = ProductFactory()

    # Test: Add products
    factory.add_product(laptop, 10)
    factory.add_product(shirt, 20)
    factory.add_product(generic, 50)

    # Test: Sell products
    factory.sell_product_electronic(laptop, 3)   # Should succeed
    factory.sell_product_dressing(shirt, 2)      # Should succeed
    factory.sell_product(generic, 5)             # Should succeed

    # Test: Sell more than available
    factory.sell_product_electronic(laptop, 100) # Should fail

    # Test: Return products
    factory.return_product(shirt, 1)
    factory.return_product(generic, 2)

    # Test: Show inventory
    factory.show_inventory()

run_tests()