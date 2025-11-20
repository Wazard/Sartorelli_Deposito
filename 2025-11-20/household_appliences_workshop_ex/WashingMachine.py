from Appliance import Appliance

class WashingMachine(Appliance):
    def __init__(self, make: str, model: str, purchase_year: int,load_capacity: float, spin_speed: int,failure_description: str = ""):
        # Initialize base Appliance attributes
        super().__init__(make, model, purchase_year, failure_description)
        # WashingMachine-specific attributes
        self.__load_capacity = load_capacity      # in kilograms
        self.__spin_speed = spin_speed            # in RPM

    # --- Getters ---
    def get_load_capacity(self) -> float:
        return self.__load_capacity

    def get_spin_speed(self) -> int:
        return self.__spin_speed

    # --- Setters ---
    def set_load_capacity(self, load_capacity: float) -> None:
        self.__load_capacity = load_capacity

    def set_spin_speed(self, spin_speed: int) -> None:
        self.__spin_speed = spin_speed

    # --- Utility Methods ---
    def description(self) -> str:
        # Extend Appliance description with washing machine details.
        base_desc = super().description()
        return f"{base_desc} | Capacity: {self.__load_capacity}kg | Spin: {self.__spin_speed} RPM"

    def base_cost_estimate(self) -> float:

        # Extend Appliance cost estimate with washing machine-specific factors.
        # Larger capacity and higher spin speed may increase repair complexity.

        cost = super().base_cost_estimate()
        # Add small factor for capacity and spin speed
        cost += (self.__load_capacity * 5)
        cost += (self.__spin_speed / 100.0)
        return round(cost, 2)