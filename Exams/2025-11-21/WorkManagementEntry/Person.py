from abc import ABC, abstractmethod
from enum import Enum

class Badge(Enum):
    TIER_1 = 1
    TIER_2 = 1.2
    TIER_3 = 1.5

class Person(ABC):
    def __init__(self, name: str, surname: str, person_id: str, badge: Badge):
        self.__name = name
        self.__surname = surname
        self.__id = person_id
        self.__badge = badge

    # Getters and setters properties
    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def person_id(self) -> str:
        return self.__id

    @property
    def badge(self) -> Badge:
        return self.__badge

    # Abstract methods
    @abstractmethod
    def enter_workplace(self) -> str:
        pass
    
    @abstractmethod
    def exit_workplace(self) -> str:
        pass