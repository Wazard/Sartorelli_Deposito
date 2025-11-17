class Contatore:
    numero_istanze = 0  # Class attribute

    def __init__(self):
        Contatore.numero_istanze += 1 # same as Static parameter in C#

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

    @staticmethod
    def conta(a, b):
        print(a + b)

# Creating some instances
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
# Output: Sono state create 2 istanze.
Contatore.conta(1,2)
# Output: 3