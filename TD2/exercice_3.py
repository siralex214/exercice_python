# Création de la classe GPS
class GPS:
    def localiser(self):
        print("Localisation en cours : votre position est 48.8566 N, 2.3522 E.")

# Création de la classe Radio
class Radio:
    def jouer_musique(self):
        print("La musique est en cours de lecture.")

# Création de la classe VoitureConnectee qui hérite de GPS et Radio
class VoitureConnectee(GPS, Radio):
    def demarrer(self):
        print("La voiture démarre.")

# Instanciation d'un objet VoitureConnectee
voiture = VoitureConnectee()

# Test des méthodes héritées de GPS et Radio
voiture.localiser()         # Appel de la méthode localiser de GPS
voiture.jouer_musique()      # Appel de la méthode jouer_musique de Radio
voiture.demarrer()           # Appel de la méthode propre à VoitureConnectee
