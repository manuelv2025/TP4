from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = float(rayon)
        self.aire = 0
        self.circonference = 0

    def calcul_aire(self):
        self.aire = pi * self.rayon * self.rayon
        return self.aire

    def calcul_circonference(self):
        self.circonference = 2.0 * pi * self.rayon
        return self.circonference


cercle = Cercle(input("Quel est le rayon du cercle? "))
print(f"L'aire du cercle est {cercle.calcul_aire()}")
print(f"La circonference du cercle est {cercle.calcul_circonference()}")
