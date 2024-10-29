# Création de la classe Rectangle
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur < 0:
            raise ValueError("La largeur doit être positive.")
        self._largeur = valeur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        if valeur < 0:
            raise ValueError("La hauteur doit être positive.")
        self._hauteur = valeur

    @property
    def surface(self):
        # Calcul de la surface
        return self.largeur * self.hauteur

# Test de la classe Rectangle
rectangle = Rectangle(5, 10)
print("Surface initiale :", rectangle.surface)

# Modification de la largeur et test de la surface
rectangle.largeur = 7
print("Surface après modification de la largeur :", rectangle.surface)

# Modification de la hauteur et test de la surface
rectangle.hauteur = 3
print("Surface après modification de la hauteur :", rectangle.surface)

# Test de validation en essayant d'assigner une valeur négative
try:
    rectangle.largeur = -4
except ValueError as e:
    print(e)

try:
    rectangle.hauteur = -2
except ValueError as e:
    print(e)
