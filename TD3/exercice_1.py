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
        # Méthode pour retirer de l'argent
        if montant > 0:
            if montant <= self.__solde:
                self.__solde -= montant
                print(f"{montant} € retirés. Nouveau solde : {self.__solde} €")
            else:
                print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            print("Le montant doit être positif pour un retrait.")

    def afficher_solde(self):
        # Méthode pour afficher le solde actuel
        print(f"Solde actuel : {self.__solde} €")

# Test de la classe
compte = CompteBancaire(100)  # Solde initial de 100 €

# Dépôt d'argent
compte.deposer(50)

# Retrait d'argent
compte.retirer(30)

# Affichage du solde
compte.afficher_solde()

# Tentative d'accès direct à l'attribut privé (ne fonctionnera pas)
try:
    print(compte.__solde)
except AttributeError:
    print("Impossible d'accéder directement à l'attribut privé __solde.")
