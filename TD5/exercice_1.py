import asyncio

# 1. Fonction asynchrone fetch_data
async def fetch_data():
    print("Récupération des données en cours...")
    await asyncio.sleep(2)  # Simule un délai de 2 secondes
    return "Données récupérées"

# 2. Fonction principale main
async def main():
    result = await fetch_data()  # Appel de fetch_data et attente du résultat
    print(result)  # Affiche le résultat

# 3. Exécution de la fonction main
asyncio.run(main())
