#es 4:

my_list = ["lista","lista"] # ordinata, mutabile, permette duplicati
my_tuple = ("a","tuple") # ordinata, immutabile, permette duplicati
my_set = set(my_list) # {"lista"} solo mutabile
my_dictionary = {"dict":"dizionario"} # ordinato da 3.7 (nel mio caso no xd), mutabile, permette duplicati ma con chiave univoca

#es 9

#Astrazione: Il processo di nascondere i dettagli complessi dietro un'interfaccia semplificata.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def maintenance_cost(self):
        pass

#Polimorfismo: la capacita` di dare gli stessi nomi ai metodi in classi diverse
class Car:
    def move(self): return "Car go road!"

class CargoCar:
    def move(self): return "Car-go space!"

def print_move(vehicle):
    print(vehicle.move())

print_move(Car())
print_move(CargoCar())

#Incapsulamento:capacita` di nascondere dei dati ed impedirne l'accesso dll'esterno
class Account:
    def __init__(self, saldo):
        self.__saldo = saldo   # privato

    def deposita(self, amount):
        if amount > 0:
            self.__saldo += amount