from abc import ABC, abstractmethod

class MoyendePaiement(ABC):
    @abstractmethod
    def effectuer_paiement(self, montant: float) -> None:
        pass

class CarteBancaire(MoyendePaiement):
    nom_du_titulaire: str
    numero_de_carte: str
    date_expiration: str

    def __init__(self, nom_du_titulaire: str, numero_de_carte: str, date_expiration: str):
        self.nom_du_titulaire = nom_du_titulaire
        self.numero_de_carte = numero_de_carte
        self.date_expiration = date_expiration

    def effectuer_paiement(self, montant: float) -> None:
        print(f"Paiement de {montant} € effectué avec la carte bancaire de {self.nom_du_titulaire}.")

class Paypal(MoyendePaiement):
    email: str
    mot_de_passe: str

    def __init__(self, email: str, mot_de_passe: str):
        self.email = email
        self.mot_de_passe = mot_de_passe

    def effectuer_paiement(self, montant: float) -> None:
        print(f"Paiement de {montant} € effectué avec Paypal.")

# créer les instances de chaque classe

carte = CarteBancaire("John Doe", "1234 5678 9012 3456", "12/24")
paypal = Paypal("john.doe@gmail.com", "password123")

paypal.effectuer_paiement(100)
carte.effectuer_paiement(200)