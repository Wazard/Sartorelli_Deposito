from TransportVehicle import TransportVehicle as Vehicle

class Motorbike(Vehicle):
    def __init__(self, license_plate: str, max_cargo: int, year_service_amount: int):
        super().__init__(license_plate, max_cargo)
        self.__year_service = year_service_amount

    # Alternative to getters and setters
    @property
    def year_service_amount(self) -> int:
        return self.__year_service

    # --- Implementation of abstract method ---
    def get_maintenance_cost(self) -> float:

        # Maintenance cost formula:
        # 50 EUR per year of service
    
        return 50*self.__year_service