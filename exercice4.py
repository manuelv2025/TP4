import random


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


hero = Hero(input("Quel est le nom de ton héro? "))
hero.faire_attaque()
hero.recevoir_dommage(random.randint(1, 6))
hero.est_vivant()
