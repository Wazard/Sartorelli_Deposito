from datetime import datetime
import time
from Person import Person, Badge
from Payable import Payable

class Manager(Person,Payable):
    def __init__(self, name: str, surname: str, person_id: str, badge: Badge, base_pay: float):
        Person.__init__(self, name, surname, person_id, badge)
        Payable.__init__(self, base_pay)
        self.__entry_time = None
        self.__exit_time = None
        self.enter_workplace()

    # Implement abstract methods
    def enter_workplace(self) -> str:
        self.__entry_time = datetime.now()
        self.__exit_time = None
        return f"Manager {self.name} {self.surname} entered at {self.__entry_time.strftime('%H:%M:%S')}."

    def exit_workplace(self) -> str:
        if self.__entry_time is None:
            return f"Manager {self.name} {self.surname} has not entered yet."
        self.__exit_time = datetime.now()
        return f"Manager {self.name} {self.surname} exited at {self.__exit_time.strftime('%H:%M:%S')}."

    # Calculate worked hours
    def worked_hours(self) -> float:
        if self.__entry_time is None or self.__exit_time is None:
            raise ValueError("Work session not completed. Must call enter() and exit().")
        delta = self.__exit_time - self.__entry_time
        return delta.total_seconds() / 3600.0

    # Pay calculation (multiplied by badge value)
    def calculate_pay(self) -> float:
        hours_worked = self.worked_hours()
        return hours_worked * self.base_pay * self.badge.value
    
""" 
# Create a Manager with base pay of 30 €/hour and Tier 3 badge
m = Manager("Anna", "Bianchi", "M456", badge=Badge.TIER_3, base_pay=30.0)

print(m.enter_workplace())
time.sleep(2)  # simulate work
print(m.exit_workplace())

print("Worked hours:", round(m.worked_hours(), 4))
print("Pay:", round(m.calculate_pay(), 2)) """