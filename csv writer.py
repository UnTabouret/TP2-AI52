"""

"""
# Résolution du problème du sac à dos ou KP (Knapsack Problem) à l'aide d'algorithme génétique
# import de la librairie

import numpy as np #utilisation des calculs matriciels
#import pandas as pd #générer les fichiers csv
import random as rd #génération de nombres aléatoires
from random import randint # génération des nombres aléatoires  
import matplotlib.pyplot as plt
import csv


#Chemin du fichier csv
chemin_csv = "data/pb4.csv"

#Chemin du fichier de paramètres
chemin_parameters = "data/parameters.csv"


with open(chemin_parameters, encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    params = next(csv_reader)

# Données du problème générées aléatoirement
nombre_objets = int(params['nombre_objets'])   #Le nombre d'objets
capacite_max = int(params['capacite_max'])    #La capacité du sac 

#paramètres de l'algorithme génétique
nbr_generations = int(params['nbr_generations']) # nombre de générations


ID_objets = np.arange(0, nombre_objets) #ID des objets à mettre dans le sac de 1 à 10
poids = np.random.randint(1, 15, size=nombre_objets) # Poids des objets générés aléatoirement entre 1kg et 15kg
valeur = np.random.randint(50, 350, size=nombre_objets) # Valeurs des objets générées aléatoirement entre 50€ et 350€

#affichage des objets: Une instance aléatoire du problème Knapsack
print('La liste des objet est la suivante :')
print('ID_objet   Poids   Valeur')
for i in range(ID_objets.shape[0]):
    print(f'{ID_objets[i]} \t {poids[i]} \t {valeur[i]}')
print()


with open(chemin_csv, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(ID_objets)
    writer.writerow(poids)
    writer.writerow(valeur)


