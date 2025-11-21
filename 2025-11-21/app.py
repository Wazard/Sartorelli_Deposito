from Truck import Truck
from Motorbike import Motorbike
from Van import Van, VanFuelType
from FleetHandler import FleetHandler

if __name__ == "__main__":
    fleet = FleetHandler()

    truck = Truck("AB123CD", 2000, 4)
    bike = Motorbike("BIKE99", 200, year_service_amount=15)
    van = Van("VAN77", 1000, fuel_type=VanFuelType.ELECTRIC)

    fleet.add_vehicle(truck)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(van)

    print(fleet)  # Fleet contains 3 vehicles
    fleet.print_all_vehicles()
    print(f"Total Maintenance Cost: {fleet.get_total_maintenance_cost()} EUR")