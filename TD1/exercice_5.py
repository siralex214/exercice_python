# 1. Créez une liste etudiants contenant les prénoms suivants : "Alice", "Bob", "Charlie", "Diane".
etudiants = ["Alice", "Bob", "Charlie", "Diane"]

# 2. Transformez cette liste en un dictionnaire où chaque clé est le prénom de l'étudiant et chaque valeur est la longueur de son prénom.
dictionnaire_etudiants = {prenom: len(prenom) for prenom in etudiants}
print("Dictionnaire des étudiants avec la longueur de leur prénom :", dictionnaire_etudiants)

# 3. Affichez le dictionnaire obtenu.
# (Déjà fait dans l'étape précédente avec print)

# 4. Convertissez uniquement les prénoms de longueur inférieure ou égale à 4 en un ensemble.
ensemble_prenoms_courts = {prenom for prenom in etudiants if len(prenom) <= 4}
print("Ensemble des prénoms de longueur inférieure ou égale à 4 :", ensemble_prenoms_courts)
