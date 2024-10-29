# 1. Créez une liste contenant les nombres de 1 à 20.
nombres = list(range(1, 21))

# 2. Utilise une compréhension de liste pour créer une nouvelle liste contenant uniquement les nombres pairs.
nombres_pairs = [x for x in nombres if x % 2 == 0]
print("Liste des nombres pairs :", nombres_pairs)

# 3. Utilise une autre compréhension de liste pour créer une liste contenant le carré de chaque nombre impair de la liste initiale.
carrés_impairs = [x ** 2 for x in nombres if x % 2 != 0]
print("Liste des carrés des nombres impairs :", carrés_impairs)
