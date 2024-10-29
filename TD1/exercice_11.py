# 1. Créez un dictionnaire pour stocker les notes de 3 étudiants en différentes matières.
notes_etudiants = {
    "Alice": [15, 18, 20],
    "Bob": [10, 12, 14],
    "Charlie": [13, 16, 19]
}

# 2. Créez un nouveau dictionnaire moyennes qui retourne la moyenne de chaque étudiant et affichez-le.
moyennes = {etudiant: sum(notes) / len(notes) for etudiant, notes in notes_etudiants.items()}
print("Moyennes des étudiants :", moyennes)
