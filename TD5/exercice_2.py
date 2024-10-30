import asyncio
import random

# 1. Fonction asynchrone download_file
async def download_file(nom_fichier):
    delay = random.randint(1, 5)  # Délai aléatoire entre 1 et 5 secondes
    print(f"Téléchargement de {nom_fichier} en cours...")
    await asyncio.sleep(delay)  # Simule le téléchargement
    return f"Fichier {nom_fichier} téléchargé"

# 2. Fonction principale main
async def main():
    # Liste des fichiers à télécharger
    fichiers = ["fichier1.txt", "fichier2.txt", "fichier3.txt"]

    # Exécute les téléchargements en parallèle
    resultats = await asyncio.gather(*(download_file(f) for f in fichiers))

    # 3. Affiche les résultats des téléchargements
    for resultat in resultats:
        print(resultat)

# Exécution de la fonction main
asyncio.run(main())
