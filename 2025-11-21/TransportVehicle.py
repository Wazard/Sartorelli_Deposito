from abc import ABC, abstractmethod

class TransportVehicle(ABC):
    def __init__(self, license_plate: str, max_cargo: int):
        self.__license_plate = license_plate
        self.__max_cargo = max_cargo
        self.__current_cargo = 0

    # Alternative to getters and setters
    @property
    def license_plate(self) -> str:
        return self.__license_plate

    @property
    def max_cargo(self) -> int:
        return self.__max_cargo

    @property
    def current_cargo(self) -> int:
        return self.__current_cargo

    # --- Concrete methods ---
    def load(self, amount: int) -> bool:
        # Attempt to load cargo. Returns True if successful, False if exceeds capacity.
        if amount < 0:
            raise ValueError("Cannot load a negative amount of cargo.")
        if self.__current_cargo + amount <= self.__max_cargo:
            self.__current_cargo += amount
            return True
        return False

    def unload(self, amount: int) -> bool:
        # Attempt to unload cargo. Returns True if successful, False if not enough cargo.
        if amount < 0:
            raise ValueError("Cannot unload a negative amount of cargo.")
        if amount <= self.__current_cargo:
            self.__current_cargo -= amount
            return True
        return False
    
    def description(self) -> str:
        return f"License Plate: {self.__license_plate}, Max Cargo: {self.__max_cargo} kg, Current Cargo: {self.__current_cargo} kg, Maintenance Cost: {self.get_maintenance_cost()} EUR"

    # --- Abstract method ---
    @abstractmethod
    def get_maintenance_cost(self) -> float:
        # Return the maintenance cost for this vehicle.
        pass