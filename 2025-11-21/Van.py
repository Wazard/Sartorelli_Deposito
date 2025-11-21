from TransportVehicle import TransportVehicle as Vehicle
from enum import Enum

class VanFuelType(Enum):
    ELECTRIC = "Electric"
    DIESEL = "Diesel"

class Van(Vehicle):
    def __init__(self, license_plate: str, max_cargo: int, fuel_type: VanFuelType):
        super().__init__(license_plate, max_cargo)
        self.__fuel_type = fuel_type

    # Alternative to getters and setters
    @property
    def fuel_type(self) -> VanFuelType:
        return self.__fuel_type

    # --- Implementation of abstract method ---
    def get_maintenance_cost(self) -> float:
        
        # If Diesel: 150 EUR
        # if Electric: 200 EUR

        return 150 if self.__fuel_type == VanFuelType.DIESEL else 200