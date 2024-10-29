# 1. Créez une liste contenant des nombres, incluant des doublons.
liste_nombres = [1, 2, 2, 3, 4, 4, 4, 5]

# 2. Convertis cette liste en un ensemble pour éliminer les doublons.
ensemble_nombres = set(liste_nombres)
print("Ensemble sans doublons :", ensemble_nombres)

# 3. Reconvertis cet ensemble en liste et affiche le résultat.
liste_sans_doublons = list(ensemble_nombres)
print("Liste sans doublons :", liste_sans_doublons)
