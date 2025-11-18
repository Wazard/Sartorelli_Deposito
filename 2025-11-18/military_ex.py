import __init__
from Utilities import classes
import random as r

# Base Unit class with common attributes and actions
class Unit:
    def __init__(self, name: str, soldier_amount: int): # Requires respectively string, int
        self.name = name
        self.soldier_amount = soldier_amount

    # Movement action
    def move(self, destination: classes.Vector3): # Requires a classes.Vector3 destination
        return f"{self.name} unit with {self.soldier_amount} soldiers is moving to {destination}."

    # Attack action
    def attack(self, target: "Unit"): # Requires a Unit type as target
        if not isinstance(target, Unit):
            raise TypeError("target must be a Unit instance")
        return f"{self.name} unit with {self.soldier_amount} soldiers is attacking {target}!"

    # Retreat action
    def retreat(self, location: classes.Vector3): # Requires a classes.Vector3 destination
        return f"{self.name} unit with {self.soldier_amount} soldiers is retreating to {location}."

    # String representation
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', soldier_amount={self.soldier_amount})"


# Infantry specialization
class InfantryUnit(Unit):
    def build_trench(self, location: classes.Vector3): # Requires a classes.Vector3 destination
        return f"{self.name} infantry unit is building a trench at {location}."


# Artillery specialization with precision attribute
class ArtilleryUnit(Unit):
    def __init__(self, name: str, soldier_amount: int, precision: float = 0.5): # Requires respectively string, int, float
        super().__init__(name, soldier_amount)
        self.precision = min(1.0, precision)  # value between 0 and 1

    # Increase precision slightly, capped at 1.0
    def calibrate(self):
        self.precision = min(1.0, self.precision + 0.15)
        return f"{self.name} artillery unit calibrated. Precision now {self.precision:.2f}."
    
    # String representation includes precision
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', soldier_amount={self.soldier_amount}, precision={self.precision})"


# Cavalry specialization with speed attribute
class CavalryUnit(Unit):
    def __init__(self, name: str, soldier_amount: int, speed: float): # Requires respectively string, int, float
        super().__init__(name, soldier_amount)
        self.speed = speed  # e.g., km/h

    # Exploration action
    def explore_location(self, location: classes.Vector3): # Requires a classes.Vector3 destination
        return f"{self.name} cavalry unit is exploring {location.position()} at speed {self.speed} km/h."

    # String representation includes speed
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', soldier_amount={self.soldier_amount}, speed={self.speed})"


# Logistics specialization
class LogisticUnit(Unit):
    def replenish_unit(self, target: Unit): # Requires a Unit
        return f"{self.name} logistic unit is replenishing {target.name} unit."


# Recognition specialization
class RecognitionUnit(Unit):
    def start_recognition(self, location: classes.Vector3): # Requires a classes.Vector3 destination
        return f"{self.name} recognition unit is scouting {location.position()}."


# MilitaryController inherits from all specialized units
class MilitaryController(InfantryUnit, ArtilleryUnit, CavalryUnit, LogisticUnit, RecognitionUnit):
    def __init__(self, name: str, soldier_amount: int, precision: float = 0.5, speed: float = 30): # Requires respectively string, int, float, float
        # Initialize base Unit once
        Unit.__init__(self, name, soldier_amount)
        # Attributes from artillery and cavalry
        self.precision = min(1.0, precision)
        self.speed = speed

        # Registry of managed units
        self.registered_units = {}

    # Register a unit by name
    def register_unit(self, unit: Unit): # Requires a Unit
        self.registered_units[unit.name] = unit
        return f"{unit.__class__.__name__} '{unit.name}' registered."

    # Show all registered units
    def show_units(self):
        if not self.registered_units:
            return "No units registered."
        return "\n".join(str(unit) for unit in self.registered_units.values())

    # Show details of a specific unit
    def unit_details(self, name: str):
        unit = self.registered_units.get(name)
        if unit is None:
            return f"No unit found with name '{name}'."
        return repr(unit)

    # String representation of controller
    def __repr__(self):
        return f"Controller(name='{self.name}', soldiers={self.soldier_amount}, precision={self.precision}, speed={self.speed})"


# Example usage

# Create specialized units
infantry = InfantryUnit("Alpha", 100)
artillery = ArtilleryUnit("Bravo", 50, precision=0.6)
cavalry = CavalryUnit("Charlie", 30, speed=40)
logistics = LogisticUnit("Delta", 20)
recon = RecognitionUnit("Echo", 15)

# Create the controller
Mcontroller = MilitaryController("Omega", 200, precision=r.random(), speed=50)

# Show all registered units (empty at first)
print("\nRegistered units:")
print(Mcontroller.show_units(), '\n')

# Register units
print(Mcontroller.register_unit(infantry))
print(Mcontroller.register_unit(artillery))
print(Mcontroller.register_unit(cavalry))
print(Mcontroller.register_unit(logistics))
print(Mcontroller.register_unit(recon))

# Show all registered units after registration
print("\nRegistered units:")
print(Mcontroller.show_units())

# Get details of specific units
print("\nDetails of 'Bravo', 'Charlie' and 'Echo':")
print(Mcontroller.unit_details("Bravo"))
print(Mcontroller.unit_details("Charlie"))
print(Mcontroller.unit_details("Echo"))

# Demonstrate inherited capabilities
print("\nController actions:")
print(Mcontroller.move(classes.Vector3(10, 0, 5)))
print(Mcontroller.build_trench(classes.Vector3(5, 5, 0)))
print(Mcontroller.calibrate())
print(Mcontroller.explore_location(classes.Vector3(2, 2, 2)))
print(Mcontroller.replenish_unit(infantry))
print(Mcontroller.start_recognition(classes.Vector3(9, 1, 3)))