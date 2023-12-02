# import random
# from itertools import permutations
#
# def conflits(disposition):
#     conflits = 0
#     for i in range(8):
#         for j in range(i + 1, 8):
#             if (
#                 disposition[i] == disposition[j] or
#                 abs(disposition[i] - disposition[j]) == abs(i - j)
#             ):
#                 conflits += 1
#     return conflits
#
# # def generer_voisinage(disposition_actuelle):
# #     voisins = []
# #     # Utilisation de permutations pour générer des voisins différents
# #     for permutation in permutations(disposition_actuelle):
# #         voisin = list(permutation)
# #         voisins.append(voisin)
# #     return voisins
# def generer_voisinage(disposition_actuelle):
#     voisins = []
#
#     for i in range(1, 7):
#         for j in range(8 - i):
#             voisin = disposition_actuelle.copy()
#             # Diviser la liste en deux et inverser les moitiés
#             voisin[j:j+i], voisin[j+i:j+2*i] = voisin[j+i:j+2*i], voisin[j:j+i]
#             voisins.append(voisin)
#
#     return voisins
#
#
#
# def afficher_solution(disposition, conflits):
#     print(f"Disposition: {disposition} - Conflits: {conflits}")
#
# def descente_simple():
#     # Étape 1: Initialisation
#     disposition_actuelle = [random.randint(0, 7) for _ in range(8)]
#     meilleur_disposition = disposition_actuelle.copy()
#     configurations_explorees = set([tuple(disposition_actuelle)])
#
#     itération = 1
#
#     while True:
#         # Étape 2: Voisinage
#         nouveaux_dispositions = generer_voisinage(disposition_actuelle)
#
#         # Étape 3: Évaluation
#         meilleure_conflits = conflits(meilleur_disposition)
#         meilleure_disposition_actuelle = disposition_actuelle.copy()
#
#         for nouvelle_disposition in nouveaux_dispositions:
#             nombre_conflits = conflits(nouvelle_disposition)
#             if nombre_conflits < meilleure_conflits and tuple(nouvelle_disposition) not in configurations_explorees:
#                 meilleure_disposition_actuelle = nouvelle_disposition
#                 meilleure_conflits = nombre_conflits
#
#         # Étape 4: Mise à jour
#         if meilleure_conflits == 0:
#             print(f"Solution optimale trouvée: {meilleure_disposition_actuelle}")
#             break
#
#         disposition_actuelle = meilleure_disposition_actuelle.copy()
#         configurations_explorees.add(tuple(disposition_actuelle))
#
#         # Étape 5: Répétition
#         afficher_solution(meilleure_disposition_actuelle, meilleure_conflits)
#         itération += 1
#
# # Exécution de l'algorithme
# descente_simple()
import random

from copy import copy
def generer_voisinage(disposition_actuelle):
    voisins = []

    for _ in range(5):  # Limiter le nombre de voisins à 5
        i, j, k, l = random.sample(range(8), 4)  # Choisir quatre positions différentes
        voisin = copy(disposition_actuelle)
        # Échanger les positions de deux éléments parmi deux éléments
        voisin[i], voisin[j], voisin[k], voisin[l] = voisin[k], voisin[l], voisin[i], voisin[j]
        voisins.append(voisin)

    return voisins

print(generer_voisinage([2, 1, 1, 3, 1, 4, 4, 6]))
