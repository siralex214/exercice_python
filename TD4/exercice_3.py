import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def afficher_graphique():
    df_ventes = pd.read_csv('ventes_mensuelles.csv')

plt.show()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Analyse des ventes")

# Création d'un bouton pour afficher le graphique
btn_afficher = ttk.Button(root, text="Afficher le graphique", command=afficher_graphique)
btn_afficher.pack(pady=20)

root.mainloop()