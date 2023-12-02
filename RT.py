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

    for _ in range(5):
        voisin_ameliorant_trouve = False

        while not voisin_ameliorant_trouve:
            i, j, k, l = random.sample(range(8), 4)
            voisin = copy(disposition_actuelle)
            voisin[i], voisin[j], voisin[k], voisin[l] = voisin[k], voisin[l], voisin[i], voisin[j]

            if conflits(voisin) < conflits(disposition_actuelle):
                voisins.append(voisin)
                voisin_ameliorant_trouve = True

    return voisins


def afficher_solution(disposition, conflits):
    print(f"Disposition: {disposition} - Conflits: {conflits}")


def descente_avec_tabou():
    disposition_actuelle = [random.randint(0, 7) for _ in range(8)]
    meilleur_disposition = copy(disposition_actuelle)
    configurations_explorees = set([tuple(disposition_actuelle)])
    liste_tabou = []

    itération = 1

    while True:
        nouveaux_dispositions = generer_voisinage(disposition_actuelle)

        meilleure_conflits = conflits(meilleur_disposition)
        meilleure_disposition_actuelle = copy(disposition_actuelle)

        for nouvelle_disposition in nouveaux_dispositions:
            nombre_conflits = conflits(nouvelle_disposition)

            if (
                    nombre_conflits < meilleure_conflits and
                    tuple(nouvelle_disposition) not in configurations_explorees and
                    nouvelle_disposition not in liste_tabou
            ):
                meilleure_disposition_actuelle = nouvelle_disposition
                meilleure_conflits = nombre_conflits

        if meilleure_conflits < conflits(meilleur_disposition):
            meilleur_disposition = meilleure_disposition_actuelle.copy()
            print(f"Meilleure disposition mise à jour: {meilleur_disposition} - Conflits: {meilleure_conflits}")

            # Mettre à jour la liste tabou avec la disposition actuelle
            liste_tabou.append(disposition_actuelle.copy())

        disposition_actuelle = copy(meilleure_disposition_actuelle)
        configurations_explorees.add(tuple(disposition_actuelle))

        # Limiter la taille de la liste tabou
        if len(liste_tabou) > 5:
            liste_tabou.pop(0)

        afficher_solution(meilleure_disposition_actuelle, meilleure_conflits)
        itération += 1


# Exécution de l'algorithme avec la Recherche Tabou
descente_avec_tabou()
