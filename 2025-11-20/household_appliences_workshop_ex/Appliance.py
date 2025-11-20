class Appliance:
    base_cost = 100.0  # baseline
    def __init__(self, make: str, model: str, purchase_year: int, failure_description: str = ""):
        self.__make = make
        self.__model = model
        self.__purchase_year = purchase_year
        self.__failure_description = failure_description

    # --- Getters ---
    def get_make(self) -> str:
        return self.__make

    def get_model(self) -> str:
        return self.__model

    def get_purchase_year(self) -> int:
        return self.__purchase_year

    def get_failure_description(self) -> str:
        return self.__failure_description
    
    def get_name(self) -> str:
        return self.__class__.__name__

    # --- Setters ---
    def set_make(self, make: str) -> None:
        self.__make = make

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_purchase_year(self, purchase_year: int) -> None:
        self.__purchase_year = purchase_year

    def set_failure_description(self, failure_description: str) -> None:
        self.__failure_description = failure_description

    # --- Utility Methods ---
    def description(self) -> str:
        # Return a human-readable description of the appliance.
        desc = f"{self.__make} {self.__model} (Purchased: {self.__purchase_year})"
        if self.__failure_description:
            desc += f" | Failure: {self.__failure_description}"
        return desc

    def base_cost_estimate(self) -> float:
        
        # Estimate base repair/replacement cost.
        # Example heuristic: older appliances cost more to repair.

        age = 2025 - self.__purchase_year
        # Add age factor
        cost = self.base_cost + (age * 20)
        return cost