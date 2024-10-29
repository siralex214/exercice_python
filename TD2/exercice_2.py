# Création de la classe de base Animal
class Animal:
    def parler(self):
        # Lève une exception pour forcer les sous-classes à implémenter cette méthode
        raise NotImplementedError("Chaque animal doit implémenter sa propre méthode parler().")

# Création de la sous-classe Chien
class Chien(Animal):
    def parler(self):
        return "Woof!"

# Création de la sous-classe Chat
class Chat(Animal):
    def parler(self):
        return "Meow!"

# Polymorphisme : Création d'une liste d'animaux
animaux = [Chien(), Chat(), Chien(), Chat()]

# Parcours de la liste et appel de la méthode parler pour chaque animal
for animal in animaux:
    print(animal.parler())
