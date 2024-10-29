# Création de la classe Voiture
class Voiture:
    # Attribut de classe pour compter le nombre de voitures
    nombre_de_voitures = 0

    def __init__(self):
        # Incrémente le compteur à chaque création d'une instance
        Voiture.nombre_de_voitures += 1

    @classmethod
    def compter_voitures(cls):
        # Retourne le nombre d'instances créées
        return cls.nombre_de_voitures

    @staticmethod
    def calculer_distance(temps, vitesse):
        # Calcule et retourne la distance
        return temps * vitesse

# Instanciation de plusieurs objets Voiture
voiture1 = Voiture()
voiture2 = Voiture()
voiture3 = Voiture()

# Appel de la méthode de classe pour vérifier le nombre de voitures créées
print("Nombre de voitures créées :", Voiture.compter_voitures())

# Test de la méthode statique sans créer d'instance de Voiture
distance = Voiture.calculer_distance(2, 60)  # Par exemple, temps = 2 heures, vitesse = 60 km/h
print("Distance calculée :", distance, "km")
