# 1. Créez une fonction compter_occurrences(texte) qui prend en argument une chaîne de caractères
# et renvoie un dictionnaire comptant le nombre de fois que chaque mot apparaît dans le texte.
def compter_occurrences(texte):
    mots = texte.lower().split()  # Convertit le texte en minuscules et le divise en mots
    occurrences = {}
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1
    return occurrences

# 2. Utilisez cette fonction sur la phrase suivante.
phrase = "le chat est dans le jardin et le chien est dans la maison"
resultat = compter_occurrences(phrase)

# 3. Affichez le résultat sous forme de dictionnaire.
print("Occurrences de chaque mot dans la phrase :", resultat)
