class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.aire = 0

    def calcul_aire(self):
        self.aire = int(self.largeur) * int(self.longueur)

    def afficher_infos(self):
        print(f"largeur = {self.largeur}, longueur = {self.longueur}, aire = {self.aire}")


rectangle = Rectangle(input("Quelle est la largeur du rectangle "), input("Quelle est la longueur du rectangle "))
rectangle.calcul_aire()
rectangle.afficher_infos()
