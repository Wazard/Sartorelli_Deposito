from abc import ABC, abstractmethod

class Payable(ABC):
    
    def __init__(self, base_pay:float):
        self.base_pay = base_pay

    # Property for base pay
    @property
    def base_pay(self) -> float:
        return self.__base_pay

    @base_pay.setter
    def base_pay(self, value: float):
        if value <= 0:
            raise ValueError("Base pay must be positive.")
        self.__base_pay = value

    @abstractmethod
    def calculate_pay(self) -> float:
        pass

    @abstractmethod
    def worked_hours(self) -> float:
        pass