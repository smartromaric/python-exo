import random

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

    for i in range(8):
        for j in range(8):
            if j != disposition_actuelle[i]:
                voisin = disposition_actuelle.copy()
                voisin[i] = j
                voisins.append(voisin)

    return voisins

def descente_simple():
    # Étape 1: Initialisation
    disposition_actuelle = [random.randint(0, 7) for _ in range(8)]
    meilleur_disposition = disposition_actuelle.copy()

    itération = 1

    while True:
        # Étape 2: Voisinage
        nouveaux_dispositions = generer_voisinage(disposition_actuelle)

        # Étape 3: Évaluation
        meilleure_conflits = conflits(meilleur_disposition)
        for nouvelle_disposition in nouveaux_dispositions:
            nombre_conflits = conflits(nouvelle_disposition)
            if nombre_conflits < meilleure_conflits:
                meilleur_disposition = nouvelle_disposition
                meilleure_conflits = nombre_conflits

        # Étape 4: Mise à jour
        if meilleure_conflits == 0:
            print(f"Solution optimale trouvée: {meilleur_disposition}")
            break

        disposition_actuelle = meilleur_disposition.copy()

        # Étape 5: Répétition
        print(f"Itération {itération}: {meilleur_disposition} - Conflits: {meilleure_conflits}")
        itération += 1

# Exécution de l'algorithme
descente_simple()
