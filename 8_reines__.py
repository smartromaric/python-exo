import random
from copy import copy

def conflits(disposition):
    conflits = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if (
                disposition[i] == disposition[j] or
                abs(disposition[i] - disposition[j]) == abs(i - j)
            ):
                conflits += 1
    return conflits

def generer_voisinage(disposition_actuelle):
    voisins = []

    for _ in range(5):  # Limiter le nombre de voisins à 5
        voisin_ameliorant_trouve = False

        while not voisin_ameliorant_trouve:
            i, j, k, l = random.sample(range(8), 4)  # Choisir quatre positions différentes
            voisin = copy(disposition_actuelle)
            # Échanger les positions de deux éléments parmi deux éléments
            voisin[i], voisin[j], voisin[k], voisin[l] = voisin[k], voisin[l], voisin[i], voisin[j]

            if conflits(voisin) < conflits(disposition_actuelle):
                voisins.append(voisin)
                voisin_ameliorant_trouve = True

    return voisins

def afficher_solution(disposition, conflits):
    print(f"Disposition: {disposition} - Conflits: {conflits}")

def descente_simple():
    # Étape 1: Initialisation
    disposition_actuelle = [random.randint(0, 7) for _ in range(8)]
    meilleur_disposition = copy(disposition_actuelle)
    configurations_explorees = set([tuple(disposition_actuelle)])

    itération = 1

    while True:
        # Étape 2: Voisinage
        nouveaux_dispositions = generer_voisinage(disposition_actuelle)

        # Étape 3: Évaluation
        meilleure_conflits = conflits(meilleur_disposition)
        meilleure_disposition_actuelle = copy(disposition_actuelle)

        for nouvelle_disposition in nouveaux_dispositions:
            nombre_conflits = conflits(nouvelle_disposition)
            print(nouvelle_disposition,":",nombre_conflits)
            if nombre_conflits < meilleure_conflits and tuple(nouvelle_disposition) not in configurations_explorees:
                meilleure_disposition_actuelle = nouvelle_disposition
                meilleure_conflits = nombre_conflits

        # Étape 4: Mise à jour
        if meilleure_conflits < conflits(meilleur_disposition):
            meilleur_disposition = meilleure_disposition_actuelle.copy()
            print(f"Meilleure disposition mise à jour: {meilleur_disposition} - Conflits: {meilleure_conflits}")

        disposition_actuelle = copy(meilleure_disposition_actuelle)
        configurations_explorees.add(tuple(disposition_actuelle))

        # Étape 5: Répétition
        afficher_solution(meilleure_disposition_actuelle, meilleure_conflits)
        itération += 1

# Exécution de l'algorithme
descente_simple()
