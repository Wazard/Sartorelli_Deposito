from datetime import datetime
import time
from Person import Person, Badge
from Payable import Payable

class Worker(Person,Payable):
    def __init__(self, name: str, surname: str, person_id: str, badge: Badge, base_pay: float):
        Person.__init__(self, name, surname, person_id, badge)
        Payable.__init__(self, base_pay)
        self.__entry_time = None
        self.__exit_time = None
        self.enter_workplace()

    # Implement abstract methods
    def enter_workplace(self) -> str:
        self.__entry_time = datetime.now()
        self.__exit_time = None  # reset exit
        return f"Worker {self.name} {self.surname} entered at {self.__entry_time.strftime('%H:%M:%S')}."

    def exit_workplace(self) -> str:
        if self.__entry_time is None:
            return f"Worker {self.name} {self.surname} has not entered yet."
        self.__exit_time = datetime.now()
        return f"Worker {self.name} {self.surname} exited at {self.__exit_time.strftime('%H:%M:%S')}."

    # Calculate worked hours
    def worked_hours(self) -> float:
        if self.__entry_time is None or self.__exit_time is None:
            raise ValueError("Work session not completed. Must call enter() and exit().")
        delta = self.__exit_time - self.__entry_time
        return delta.total_seconds() / 3600.0  # convert seconds to hours

    # Pay calculation with overtime
    def calculate_pay(self) -> float:
        hours_worked = self.worked_hours()
        if hours_worked <= 8:
            return hours_worked * self.base_pay
        else:
            regular_pay = 8 * self.base_pay
            overtime_hours = hours_worked - 8
            overtime_pay = overtime_hours * (self.base_pay * 1.25)
            return regular_pay + overtime_pay


""" # Create a Worker with base pay of 20 €/hour
w = Worker("Luca", "Rossi", "W123", badge=Badge.TIER_2, base_pay=20.0)

print(w.enter_workplace())
time.sleep(2)  # simulate work (2 seconds)
print(w.exit_workplace())

print("Worked hours:", round(w.worked_hours(), 4))
print("Pay:", round(w.calculate_pay(), 2)) """