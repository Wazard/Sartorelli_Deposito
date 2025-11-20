from Appliance import Appliance

class Refrigerator(Appliance):
    def __init__(self, make: str, model: str, purchase_year: int, load_capacity: float, has_freezer: bool, failure_description: str = ""):
        # Initialize base Appliance attributes
        super().__init__(make, model, purchase_year, failure_description)
        # Refrigeration-specific attributes
        self.__load_capacity = load_capacity   # in liters
        self.__has_freezer = has_freezer       # boolean

    # --- Getters ---
    def get_load_capacity(self) -> float:
        return self.__load_capacity

    def has_freezer(self) -> bool:
        return self.__has_freezer

    # --- Setters ---
    def set_load_capacity(self, load_capacity: float) -> None:
        self.__load_capacity = load_capacity

    def set_has_freezer(self, has_freezer: bool) -> None:
        self.__has_freezer = has_freezer

    # --- Utility Methods ---
    def description(self) -> str:
        #Extend Appliance description with refrigeration details.
        base_desc = super().description()
        freezer_info = "with Freezer" if self.__has_freezer else "no Freezer"
        return f"{base_desc} | Capacity: {self.__load_capacity}L | {freezer_info}"

    def base_cost_estimate(self) -> float:

        # Extend Appliance cost estimate with refrigeration-specific factors.
        # - Add cost if freezer is present.
        # - Add cost if capacity > 59L.
    
        cost = super().base_cost_estimate()

        if self.__has_freezer:
            cost += 75.0  # freezer adds complexity

        if self.__load_capacity > 59.0:
            cost += 40.0  # larger units cost more to repair

        return round(cost, 2)