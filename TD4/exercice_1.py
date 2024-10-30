import numpy as np

# Créez un tableau NumPy contenant les nombres de 1 à 20
tableau = np.arange(1, 21)

# Calcul de la somme, de la moyenne et de l'écart-type
somme = np.sum(tableau)
moyenne = np.mean(tableau)
ecart_type = np.std(tableau)

# Affichage des résultats
print("Tableau :", tableau)
print("Somme :", somme)
print("Moyenne :", moyenne)
print("Écart-type :", ecart_type)
