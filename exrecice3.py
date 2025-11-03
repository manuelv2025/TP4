from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = float(rayon)
        self.aire = 0
        self.circonference = 0

    def calcul_aire(self):
        self.aire = pi * self.rayon * self.rayon
        print(f"L'aire du cercle est {self.aire}")

    def calcul_circonference(self):
        self.circonference = 2.0 * pi * self.rayon
        print(f"La circonference du cercle est {self.circonference}")


cercle = Cercle(input("Quel est le rayon du cercle? "))
cercle.calcul_aire()
cercle.calcul_circonference()