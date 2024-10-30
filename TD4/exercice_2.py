import pandas as pd

# Charger le fichier CSV
# Remplacez 'fichier_produits.csv' par le nom réel du fichier CSV
df = pd.read_csv('produits.csv')

# Filtrer les produits ayant un prix supérieur à 50
produits_sup_50 = df[df['Prix'] > 50]

# Afficher les cinq premiers produits ayant un prix supérieur à 50
print("Cinq premiers produits avec un prix supérieur à 50 :")
print(produits_sup_50.head(5))

# Calculer la moyenne des prix
moyenne_prix = df['Prix'].mean()
print("Moyenne des prix :", moyenne_prix)
