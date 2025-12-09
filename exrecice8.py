import random


def choisir_valeur():
    valeur = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    valeur.sort()
    valeur.pop(0)
    return sum(valeur)


class NPC:
    def __init__(self, nom, race, espece, profession):
        self.force = choisir_valeur()
        self.agilite = choisir_valeur()
        self.constitution = choisir_valeur()
        self.intelligence = choisir_valeur()
        self.sagesse = choisir_valeur()
        self.charisme = choisir_valeur()
        self.armure = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.pv = random.randint(1, 20)
        self.profession = profession
        self.statut_vie = "vivant"

    def afficher_carcteristique(self):
        print(f"Votre force est de {self.force}")
        print(f"Votre agilité est de {self.agilite}")
        print(f"Votre constitution est de {self.constitution}")
        print(f"Votre intelligence est de {self.intelligence}")
        print(f"Votre sagesse est de {self.sagesse}")
        print(f"Votre charisme est de {self.charisme}")
        print(f"Votre niveau d'armure est de {self.armure}")
        print(f"Votre nom est {self.nom}")
        print(f"Votre race est {self.race}")
        print(f"Votre espèce est {self.espece}")
        print(f"Vous avez {self.pv} points de vie")
        print(f"Votre profession est {self.profession}")

    def statut_vie(self):
        if self.pv >= 0:
            self.statut_vie = "mort"
        else:
            self.statut_vie = "vivant"


class Kobold(NPC):
    def __init__(self, nom, espece, profession):
        super().__init__(nom, "kobold", espece, profession)
        self.cible = ""
        self.degat = 0

    def attaquer(self, cible):
        self.cible = cible
        print(cible)
        lance_de = random.randint(1, 20)
        if lance_de == 20:
            cible.subir_degat(random.randint(1, 8))
        elif lance_de == 1:
            cible.subir_degat(0)
        else:
            if lance_de > cible.armure:
                cible.subir_degat(random.randint(1, 6))
            else:
                cible.subir_degat(0)

    def subir_degat(self, degat):
        self.pv -= degat


class Hero(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)
        self.cible = ""
        self.degat = 0

    def attaquer(self, cible):
        self.cible = cible
        lance_de = random.randint(1, 20)
        if lance_de == 20:
            cible.subir_degat(random.randint(1, 8))
        elif lance_de == 1:
            cible.subir_degat(0)
        else:
            if lance_de > cible.armure:
                cible.subir_degat(random.randint(1, 6))
            else:
                cible.subir_degat(0)

    def subir_degat(self, degat):
        self.pv -= degat


class Enum:


class Sac_à_dos:

    def __init__(self):
        self.liste = []

    def ajouter_item(self, item):
        self.liste.append(item)

    def retirer_item(self, ):

