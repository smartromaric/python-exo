import random
# import math
from numpy import exp
from copy import copy

N = 8
MAX_ITERATIONS = 10000

def main():
    solution_courante = generer_solution_aleatoire()
    resoudre(solution_courante)

def resoudre(solution_courante):
    conflits_courants = compter_conflits(solution_courante)
    temperature = 1000.0
    taux_refroidissement = 0.95
    iterations = 0

    while conflits_courants != 0 and iterations < MAX_ITERATIONS:
        voisin = generer_voisin_ameliorant(solution_courante)
        conflits_voisin = compter_conflits(voisin)

        probabilite = probabilite_acceptation(conflits_courants, conflits_voisin, temperature)

        if random.random() < probabilite:
            solution_courante = voisin
            conflits_courants = conflits_voisin

            afficher_iteration(iterations, solution_courante, conflits_courants)

            if conflits_courants == 0:
                break

        temperature *= taux_refroidissement
        iterations += 1

    afficher_solution_finale(iterations, solution_courante)

def generer_solution_aleatoire():
    solution = list(range(1, N + 1))
    random.shuffle(solution)
    return solution

def generer_voisin_ameliorant(disposition_actuelle):
    voisins = []

    for _ in range(5):
        i, j, k, l = random.sample(range(N), 4)
        voisin = copy(disposition_actuelle)
        voisin[i], voisin[j], voisin[k], voisin[l] = voisin[k], voisin[l], voisin[i], voisin[j]
        voisins.append(voisin)

    indexe = random.randint(0, 4)
    voisin_aleatoire = voisins[indexe]

    return voisin_aleatoire

def compter_conflits(disposition):
    conflits = 0
    for i in range(N):
        for j in range(i + 1, N):
            if disposition[i] == disposition[j] or abs(disposition[i] - disposition[j]) == abs(i - j):
                conflits += 2
    return conflits

def probabilite_acceptation(conflits_courants, conflits_voisin, temperature):
    return exp((conflits_courants - conflits_voisin) / temperature) if temperature != 0 else 0

def afficher_iteration(iterations, solution, conflits):
    print(f"Iteration n° {iterations}")
    print(f" Nouvelle solution : {solution}")
    print(f" Il y a {conflits} Conflits\n")

def afficher_solution_finale(iterations, solution):
    print(f"Solution finale trouvée en {iterations} itérations avec 0 conflits:")
    print(solution)

if __name__ == "__main__":
    main()