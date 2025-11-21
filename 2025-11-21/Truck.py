from TransportVehicle import TransportVehicle

class Truck(TransportVehicle):
    def __init__(self, license_plate: str, max_cargo: int, axels_number: int):
        super().__init__(license_plate, max_cargo)
        self.__axels_number = axels_number

    # Alternative to getters and setters
    @property
    def axels_number(self) -> int:
        return self.__axels_number

    # --- Implementation of abstract method ---
    def get_maintenance_cost(self) -> float:

        # Maintenance cost formula:
        # 100 EUR per axle + 1 EUR per max kg capacity
    
        return (100 * self.__axels_number) + (1 * self.max_cargo)