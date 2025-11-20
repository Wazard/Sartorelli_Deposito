from Appliance import Appliance
from enum import Enum

class OvenType(Enum):
    ELECTRIC = "Electric"
    GAS = "Gas"

class Oven(Appliance):
    def __init__(self, make: str, model: str, purchase_year: int, oven_type: OvenType, is_ventilated: bool, failure_description: str = ""):
        # Initialize base Appliance attributes
        super().__init__(make, model, purchase_year, failure_description)

        # Oven-specific attributes
        self.__type = oven_type
        self.__is_ventilated = is_ventilated

    # --- Getters ---
    def get_type(self) -> str:
        return self.__type.value

    def is_ventilated(self) -> bool:
        return self.__is_ventilated

    # --- Setters ---
    def set_type(self, oven_type: OvenType) -> None:
        self.__type = oven_type

    def set_is_ventilated(self, is_ventilated: bool) -> None:
        self.__is_ventilated = is_ventilated

    # --- Utility Methods ---
    def description(self) -> str:
        # Extend Appliance description with oven details.
        base_desc = super().description()
        vent_info = "Ventilated" if self.__is_ventilated else "Non-ventilated"
        return f"{base_desc} | Type: {self.__type} | {vent_info}"

    def base_cost_estimate(self) -> float:

        # Extend Appliance cost estimate with oven-specific rules:
        # - Gas ovens: 1.25x multiplier
        # - Electric ovens: 0.95x multiplier
        # - Ventilated ovens: +50

        cost = super().base_cost_estimate()

        if self.__type == OvenType.GAS:
            cost *= 1.25
        elif self.__type == OvenType.ELECTRIC:
            cost *= 0.95

        if self.__is_ventilated:
            cost += 50.0

        return round(cost, 2)