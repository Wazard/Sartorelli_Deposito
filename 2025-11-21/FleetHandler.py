from typing import List
from TransportVehicle import TransportVehicle as Vehicle

class FleetHandler:
    def __init__(self):
        # Private list to store vehicles
        self.__vehicle_list: List[Vehicle] = []

    @property
    def vehicle_list(self) -> List[Vehicle]:
        # Read-only access to the fleet list.
        return self.__vehicle_list

    def add_vehicle(self, vehicle: Vehicle) -> None:

        # Add a vehicle to the fleet.
        # Ensures only TransportVehicle subclasses are accepted.

        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only TransportVehicle instances can be added to the fleet.")
        self.__vehicle_list.append(vehicle)

    def get_total_maintenance_cost(self) -> float:
        # Calculate the total maintenance cost of all vehicles in the fleet.
        return sum(vehicle.get_maintenance_cost() for vehicle in self.__vehicle_list)

    def print_all_vehicles(self) -> None:
        # Print details of all vehicles in the fleet.
        if not self.__vehicle_list:
            print("Fleet is empty.")
            return

        for vehicle in self.__vehicle_list:
            print(vehicle.description())

    def __str__(self) -> str:
        # Return a summary of the fleet.
        return f"Fleet contains {len(self.__vehicle_list)} vehicles."
