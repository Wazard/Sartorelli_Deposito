class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year
        self._turns_on = False

    # --- Getters ---
    def get_make(self) -> str:
        return self._make

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_turns_on(self) -> bool:
        return self._turns_on

    # --- Actions ---
    def turn_on(self) -> None:
        self._turns_on = True

    def turn_off(self) -> None:
        self._turns_on = False


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, door_number: int):
        super().__init__(make, model, year)
        self._door_number = door_number

    # Getter
    def get_door_number(self) -> int:
        return self._door_number

    # Action
    def honk(self) -> str:
        return "Honk!"


class Van(Vehicle):
    def __init__(self, make: str, model: str, year: int, load_capacity: int):
        super().__init__(make, model, year)
        self._load_capacity = load_capacity
        self._current_load = 0

    # Getter / Setter
    def get_load_capacity(self) -> int:
        return self._load_capacity

    def set_load_capacity(self, load_capacity: int) -> None:
        self._load_capacity = load_capacity

    def get_current_load(self) -> int:
        return self._current_load

    # Actions
    def load(self, amount: int):
        if self._current_load + amount <= self._load_capacity:
            self._current_load += amount
            return True,f"Loaded {amount}. Current load: {self._current_load}"
        else:
            return False,f"Cannot load {amount}: capacity exceeded."

    def unload(self, amount: int):
        if amount <= self._current_load:
            self._current_load -= amount
            return True,f"Unloaded {amount}. Current load: {self._current_load}"
        else:
            return False,f"Cannot unload {amount}: not enough load."


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, type_: str):
        super().__init__(make, model, year)
        self._type = type_

    # Getter
    def get_type(self) -> str:
        return self._type

    # Action
    def do_a_wheelie(self):
        if self.get_turns_on():
            return True,"The motorcycle pops a wheelie!"
        else:
            return False;"Can't do a wheelie: the motorcycle is off."


class ParkingLot:
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    # Getter 
    def get_vehicles(self) -> list[Vehicle]:
        return self._vehicles

    # Actions 
    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)

    def print_vehicles(self) -> None:
        if not self._vehicles:
            print("Parking lot is empty.")
        else:
            for v in self._vehicles:
                print(f"{v.get_year()} {v.get_make()} {v.get_model()}")


# --- Example Usage of All Functions ---

# Create base Vehicle
v = Vehicle("Generic", "ModelX", 2000)
print(v.get_make())       # Generic
print(v.get_model())      # ModelX
print(v.get_year())       # 2000
print(v.get_turns_on())   # False

v.turn_off()
print(v.get_turns_on())   # False
v.turn_on()
print(v.get_turns_on())   # True


# --- Car ---
car = Car("Toyota", "Corolla", 2020, 4)
print(car.get_door_number())   # 4
print(car.honk())              # Beep beep!


# --- Van ---
van = Van("Ford", "Transit", 2019, 1000)
print(van.get_load_capacity())   # 1000
van.set_load_capacity(1200)
print(van.get_load_capacity())   # 1200
print(van.get_current_load())    # 0
print(van.load(500))             # Loaded 500. Current load: 500
print(van.load(800))             # Cannot load: capacity exceeded.
print(van.unload(200))           # Unloaded 200. Current load: 300
print(van.unload(400))           # Cannot unload: not enough load.


# --- Motorcycle ---
bike = Motorcycle("Yamaha", "MT-07", 2021, "Sport")
print(bike.get_type())           # Sport
print(bike.do_a_wheelie())       # Can't do a wheelie: the motorcycle is off.
bike.turn_on()
print(bike.do_a_wheelie())       # The motorcycle pops a wheelie!


# --- ParkingLot ---
lot = ParkingLot()
lot.add_vehicle(car)
lot.add_vehicle(van)
lot.add_vehicle(bike)
lot.add_vehicle(v)

print("\nVehicles in lot:")
lot.print_vehicles()
# Output:
# 2020 Toyota Corolla
# 2019 Ford Transit
# 2021 Yamaha MT-07
# 2021 UpdatedMake UpdatedModel

lot.remove_vehicle(van)
print("\nVehicles after removing van:")
lot.print_vehicles()