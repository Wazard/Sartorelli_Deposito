from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, surname: str, base_RAL: float):
        self._name = name
        self._surname = surname
        self._RAL = base_RAL
    
    @abstractmethod
    def calculate_salary(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass


class PermanentEmployee(Employee):
    def __init__(self, name: str, surname: str, base_RAL: float, bonus_rate: float = 0.1):
        super().__init__(name, surname, base_RAL)
        self._bonus_rate = bonus_rate
    
    def calculate_salary(self) -> float:
        # Permanent employees get base RAL plus a bonus
        return self._RAL + (self._RAL * self._bonus_rate)
    
    def description(self) -> str:
        return f"Permanent Employee: {self._name} {self._surname}, Base RAL: €{self._RAL}, Bonus Rate: {self._bonus_rate*100:.0f}%"


class CommissionEmployee(Employee):
    def __init__(self, name: str, surname: str, base_RAL: float, sales_amount: float, commission_rate: float):
        super().__init__(name, surname, base_RAL)
        self._sales_amount = sales_amount
        self._commission_rate = commission_rate
    
    def calculate_salary(self) -> float:
        # Commission employees get base RAL plus commission on sales
        return self._RAL + (self._sales_amount * self._commission_rate)
    
    def description(self) -> str:
        return (f"Commission Employee: {self._name} {self._surname}, "
                f"Base RAL: €{self._RAL}, Sales: €{self._sales_amount}, "
                f"Commission Rate: {self._commission_rate*100:.0f}%")


emp1 = PermanentEmployee("Alice", "Rossi", 30000, bonus_rate=0.2)
print(emp1.description())
print("Annual Salary:", emp1.calculate_salary())

emp2 = CommissionEmployee("Bob", "Bianchi", 20000, sales_amount=150000, commission_rate=0.15)
print(emp2.description())
print("Annual Salary:", emp2.calculate_salary())