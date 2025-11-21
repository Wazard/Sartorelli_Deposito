from datetime import datetime, time
from Person import Person, Badge

class Visitor(Person):
    def __init__(self, name: str, surname: str, person_id: str, badge: Badge):
        super().__init__(name, surname, person_id, badge)
        self.__entry_time = None

    # Allowed entry windows
    __morning_start = time(10, 0)
    __morning_end   = time(12, 0)
    __afternoon_start = time(16, 0)
    __afternoon_end   = time(18, 0)

    def __is_allowed_entry(self, current_time: time) -> bool:
        return ((self.__morning_start <= current_time <= self.__morning_end) or
                (self.__afternoon_start <= current_time <= self.__afternoon_end))

    # Implement abstract methods
    def enter_workplace(self) -> str:
        now = datetime.now()
        if self.__is_allowed_entry(now.time()):
            self.__entry_time = now
            return f"Visitor {self.name} {self.surname} entered at {now.strftime('%H:%M:%S')}."
        else:
            return f"Visitor {self.name} {self.surname} denied entry at {now.strftime('%H:%M:%S')} (outside allowed hours)."

    def exit_workplace(self) -> str:
        if self.__entry_time is None:
            return f"Visitor {self.name} {self.surname} has not entered yet."
        now = datetime.now()

        # Check if exit is too late
        if not self.__is_allowed_entry(self.__entry_time.time()):
            return f"Visitor {self.name} {self.surname} exited at {now.strftime('%H:%M:%S')}."
        if (self.__entry_time.time() <= self.__morning_end and now.time() > self.__morning_end) or (self.__entry_time.time() >= self.__afternoon_start and now.time() > self.__afternoon_end):
            print(f"Visitor {self.name} {self.surname} exited too late at {now.strftime('%H:%M:%S')}.")
        return f"Visitor {self.name} {self.surname} exited at {now.strftime('%H:%M:%S')}."


v = Visitor("Mario", "Conti", "V001", Badge.TIER_1)

print(v.enter_workplace())   # Will only succeed if current time is 10–12 or 16–18
import time; time.sleep(2)  # simulate short visit
print(v.exit_workplace())    # If exit is after allowed window, prints warning