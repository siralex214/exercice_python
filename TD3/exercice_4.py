from abc import ABC, abstractmethod

# Définition de la classe abstraite MoyendePaiement
class MoyendePaiement(ABC):
    # Méthode abstraite que toutes les sous-classes doivent implémenter
    @abstractmethod
    def effectuer_paiement(self, montant: float) -> None:
        pass

# Définition de la classe CarteBancaire qui hérite de MoyendePaiement
class CarteBancaire(MoyendePaiement):
    nom_du_titulaire: str
    numero_de_carte: str
    date_expiration: str

    # Constructeur de la classe CarteBancaire
    def __init__(self, nom_du_titulaire: str, numero_de_carte: str, date_expiration: str):
        self.nom_du_titulaire = nom_du_titulaire
        self.numero_de_carte = numero_de_carte
        self.date_expiration = date_expiration

    # Implémentation de la méthode abstraite effectuer_paiement
    def effectuer_paiement(self, montant: float) -> None:
        print(f"Paiement de {montant} € effectué avec la carte bancaire de {self.nom_du_titulaire}.")

# Définition de la classe Paypal qui hérite de MoyendePaiement
class Paypal(MoyendePaiement):
    email: str
    mot_de_passe: str

    # Constructeur de la classe Paypal
    def __init__(self, email: str, mot_de_passe: str):
        self.email = email
        self.mot_de_passe = mot_de_passe

    # Implémentation de la méthode abstraite effectuer_paiement
    def effectuer_paiement(self, montant: float) -> None:
        print(f"Paiement de {montant} € effectué avec Paypal.")

# Création des instances de chaque classe
carte = CarteBancaire("John Doe", "1234 5678 9012 3456", "12/24")
paypal = Paypal("john.doe@gmail.com", "password123")

# Appel des méthodes effectuer_paiement pour chaque instance
paypal.effectuer_paiement(100)
carte.effectuer_paiement(200)