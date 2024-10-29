# 1. Implémentez une pile (stack) en utilisant une liste.
pile = []

# Ajoute les éléments 10, 20, 30, et 40 dans la pile.
pile.append(10)
print("Pile après ajout de 10 :", pile)
pile.append(20)
print("Pile après ajout de 20 :", pile)
pile.append(30)
print("Pile après ajout de 30 :", pile)
pile.append(40)
print("Pile après ajout de 40 :", pile)

# Retire le dernier élément ajouté (opération de dépilement).
element_depile = pile.pop()
print("Pile après dépilement de", element_depile, ":", pile)
