# 1. Créez un dictionnaire produits contenant des articles et leurs prix.
produits = {
    "lait": 1.50,
    "pain": 1.00,
    "pomme": 0.80
}

# 2. Parcourez le dictionnaire pour afficher chaque article et son prix.
print("Liste des produits et leurs prix :")
for article, prix in produits.items():
    print(f"{article} : {prix:.2f} €")

# 3. Demandez à l'utilisateur d'entrer le nom d'un article et vérifiez s'il est dans le dictionnaire.
article_recherche = input("Entrez le nom d'un article : ").strip().lower()

if article_recherche in produits:
    # Si oui, affichez le prix de l'article.
    print(f"Le prix de '{article_recherche}' est : {produits[article_recherche]:.2f} €")
else:
    # Si non, ajoutez l'article avec un prix de 2.00 par défaut.
    produits[article_recherche] = 2.00
    print(f"'{article_recherche}' a été ajouté au dictionnaire avec un prix de 2.00 €")
