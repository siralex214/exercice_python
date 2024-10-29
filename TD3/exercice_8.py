# Définition de l'exception personnalisée ErreurRetrait
class ErreurRetrait(Exception):
    def __init__(self, message="Le montant demandé dépasse le solde disponible."):
        self.message = message
        super().__init__(self.message)

# Classe CompteBancaire avec la gestion de l'exception ErreurRetrait
class CompteBancaire:
    def __init__(self, solde_initial=0):
        # Attribut privé pour stocker le solde
        self.__solde = solde_initial

    def deposer(self, montant):
        # Méthode pour déposer de l'argent
        if montant > 0:
            self.__solde += montant
            print(f"{montant} € déposés. Nouveau solde : {self.__solde} €")
        else:
            print("Le montant doit être positif pour un dépôt.")

    def retirer(self, montant):
        # Méthode pour retirer de l'argent avec gestion d'erreur
        if montant > 0:
            if montant <= self.__solde:
                self.__solde -= montant
                print(f"{montant} € retirés. Nouveau solde : {self.__solde} €")
            else:
                # Lève l'exception personnalisée si le montant dépasse le solde
                raise ErreurRetrait(f"Vous avez tenté de retirer {montant} €, mais le solde disponible est de {self.__solde} €.")
        else:
            print("Le montant doit être positif pour un retrait.")

    def afficher_solde(self):
        # Méthode pour afficher le solde actuel
        print(f"Solde actuel : {self.__solde} €")

# Test de la classe avec gestion de l'exception ErreurRetrait
compte = CompteBancaire(100)  # Solde initial de 100 €

# Dépôt d'argent
compte.deposer(50)

# Retrait d'argent dans la limite du solde
compte.retirer(30)

# Affichage du solde
compte.afficher_solde()

# Tentative de retrait supérieur au solde disponible
try:
    compte.retirer(200)  # Montant supérieur au solde
except ErreurRetrait as e:
    print(e)
