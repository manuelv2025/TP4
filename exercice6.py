import random
from dataclasses import dataclass


@dataclass
class Personnage:
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class Hero:
    def __init__(self, nom):
        self.nb_point_vie = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.nom_hero = nom
        self.qte_dommage = 0

    def faire_attaque(self):
        return self.force_attaque + random.randint(1, 6)

    def recevoir_dommage(self, qte_dommage):
        self.qte_dommage = qte_dommage
        self.nb_point_vie -= self.qte_dommage - self.force_defense

    def est_vivant(self):
        return self.nb_point_vie > 0
