# 1. Créez une liste nombres contenant les nombres de 1 à 10.
nombres = list(range(1, 11))

# 2. Remplacez les valeurs paires par le mot "pair".
nombres_modifiés = ["pair" if x % 2 == 0 else x for x in nombres]
print("Liste avec les nombres pairs remplacés :", nombres_modifiés)

# 3. Affichez uniquement les valeurs impaires de la liste sans modifier la liste originale.
valeurs_impaires = [x for x in nombres if x % 2 != 0]
print("Valeurs impaires de la liste :", valeurs_impaires)

# 4. Trouvez et affichez l'indice du nombre 5 dans la liste.
indice_5 = nombres.index(5)
print("Indice du nombre 5 dans la liste :", indice_5)
