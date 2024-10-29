# Création de la classe Produit
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

# Création de la classe Commande
class Commande:
    def __init__(self):
        # Liste pour stocker les produits
        self.produits = []

    def ajouter_produit(self, produit):
        # Ajoute un produit à la commande
        self.produits.append(produit)
        print(f"Produit {produit.nom} ajouté à la commande.")

    def retirer_produit(self, produit):
        # Retire un produit de la commande s'il est présent
        if produit in self.produits:
            self.produits.remove(produit)
            print(f"Produit {produit.nom} retiré de la commande.")
        else:
            print(f"Produit {produit.nom} non trouvé dans la commande.")

    def calculer_total(self):
        # Calcule le coût total de la commande
        total = sum(produit.prix for produit in self.produits)
        return total

# Test du système de gestion de commandes
# Création de quelques produits
produit1 = Produit("Laptop", 1200.00)
produit2 = Produit("Souris", 25.00)
produit3 = Produit("Clavier", 75.00)

# Création d'une commande
commande = Commande()

# Ajout de produits à la commande
commande.ajouter_produit(produit1)
commande.ajouter_produit(produit2)
commande.ajouter_produit(produit3)

# Calcul et affichage du total
print("Total de la commande :", commande.calculer_total(), "€")

# Retrait d'un produit de la commande
commande.retirer_produit(produit2)

# Nouveau calcul et affichage du total
print("Total de la commande après retrait :", commande.calculer_total(), "€")
