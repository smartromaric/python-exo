import random
import math
from numpy import  exp2
from copy import copy

N = 8
MAX_ITERATIONS = 10000
TAILLE_LISTE_TABOU = 3  # Taille arbitraire de la liste tabou

def main():
    solution_courante = generer_solution_aleatoire()
    resoudre(solution_courante)

def resoudre(solution_courante):
    conflits_courants = compter_conflits(solution_courante)
    temperature = 1000.0
    taux_refroidissement = 0.95
    iterations = 1
    liste_tabou = []

    while conflits_courants != 0 and iterations < MAX_ITERATIONS:
        voisin = generer_voisin_ameliorant(solution_courante, liste_tabou)
        conflits_voisin = compter_conflits(voisin)

        probabilite = probabilite_acceptation(conflits_courants, conflits_voisin, temperature)

        if random.random() < probabilite:
            solution_courante = voisin
            conflits_courants = conflits_voisin
            liste_tabou.append(copy(solution_courante))

            # Limitez la taille de la liste tabou
            if len(liste_tabou) > TAILLE_LISTE_TABOU:
                liste_tabou.pop(0)

            afficher_iteration(iterations, solution_courante, conflits_courants,liste_tabou)

            if conflits_courants == 0:
                break

        temperature *= taux_refroidissement
        iterations += 1

    afficher_solution_finale(iterations, solution_courante)

def generer_solution_aleatoire():
    solution = list(range(1, N + 1))
    random.shuffle(solution)
    return solution

def generer_voisin_ameliorant(disposition_actuelle, liste_tabou):
    voisins = []

    for _ in range(5):
        i, j, k, l = random.sample(range(N), 4)
        voisin = copy(disposition_actuelle)
        voisin[i], voisin[j], voisin[k], voisin[l] = voisin[k], voisin[l], voisin[i], voisin[j]
        voisins.append(voisin)

    # Exclure les voisins qui sont dans la liste tabou
    voisins_non_tabous = [voisin for voisin in voisins if voisin not in liste_tabou]

    # Choisir aléatoirement parmi les voisins non tabous
    if voisins_non_tabous:
        index_aleatoire = random.randint(0, len(voisins_non_tabous) - 1)
        voisin_aleatoire = voisins_non_tabous[index_aleatoire]
        return voisin_aleatoire
    else:
        # Si tous les voisins sont dans la liste tabou, choisir un voisin aléatoire
        index_aleatoire = random.randint(0, 4)
        voisin_aleatoire = voisins[index_aleatoire]
        return voisin_aleatoire

def compter_conflits(disposition):
    conflits = 0
    for i in range(N):
        for j in range(i + 1, N):
            if disposition[i] == disposition[j] or abs(disposition[i] - disposition[j]) == abs(i - j):
                conflits += 2
    return conflits

def probabilite_acceptation(conflits_courants, conflits_voisin, temperature):
    return exp2((conflits_courants - conflits_voisin) / temperature) if temperature != 0 else 0

def afficher_iteration(iterations, solution, conflits,list_tabou):
    print(f"Iteration n° {iterations}")
    print(f" Nouvelle solution : {solution}")
    print(f" Il y a {conflits} Conflits\n")
    print(f"La liste TABOU est {list_tabou} \n")

def afficher_solution_finale(iterations, solution):
    print(f"Solution finale trouvée en {iterations} itérations avec 0 conflits:")
    print(solution)



if __name__ == "__main__":
    main()

