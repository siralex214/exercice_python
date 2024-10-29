# 1. Créez une file (queue) en utilisant une liste.
file = []

# Ajoute les éléments 1, 2, 3, et 4 dans la file.
file.append(1)
print("File après ajout de 1 :", file)
file.append(2)
print("File après ajout de 2 :", file)
file.append(3)
print("File après ajout de 3 :", file)
file.append(4)
print("File après ajout de 4 :", file)

# Retire le premier élément ajouté (opération de défilement).
element_defile = file.pop(0)
print("File après défilement de", element_defile, ":", file)
