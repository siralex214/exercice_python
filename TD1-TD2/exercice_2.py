# 1. Créez un tuple dimensions avec les valeurs (5, 10, 15).
dimensions = (5, 10, 15)

# 2. Écrivez un programme qui extrait chaque valeur de ce tuple et la multiplie par 2.
dimensions_multipliées = tuple(x * 2 for x in dimensions)
print("Dimensions multipliées par 2 :", dimensions_multipliées)

# 3. Concaténez dimensions avec un autre tuple (20, 25) et affichez le résultat.
nouveau_tuple = dimensions + (20, 25)
print("Résultat de la concaténation :", nouveau_tuple)
