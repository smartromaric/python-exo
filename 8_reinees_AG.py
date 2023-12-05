import random

def initialiser_population(taille_population):
    return [random.choices(range(7),k=8) for _ in range(8) for _ in range(taille_population)]

def evaluer(solution):
    attaques = 0
    for i in range(7):
        for j in range(i + 1, 8):
            if solution[i] == solution[j] or abs(i - j) == abs(solution[i] - solution[j]):
                attaques += 2
    return attaques

def croisement(parent1, parent2):
    point_croisement = random.randint(1, 6)
    enfant1 = parent1[:point_croisement] + parent2[point_croisement:]
    enfant2 = parent2[:point_croisement] + parent1[point_croisement:]
    return enfant1, enfant2

def mutation(solution, taux_mutation):
    for i in range(8):
        if random.random() < taux_mutation:
            solution[i] = random.randint(0, 7)
    return solution

def selection(population, scores, n_selection):
    indices_selectionnes = sorted(range(len(scores)), key=lambda k: scores[k])[:n_selection]
    return [population[i] for i in indices_selectionnes]

def algorithme_genetique(taille_population, generations, taux_mutation):
    population = initialiser_population(taille_population)

    for _ in range(generations):
        scores = [evaluer(solution) for solution in population]
        print(population)

        # Vérification de la solution optimale
        if 0 in scores:
            indice_optimal = scores.index(0)
            print("Solution optimale trouvée :", population[indice_optimal])
            print("nous somme a l'iteration N°",_)
            return population[indice_optimal]
            

        parents = selection(population, scores, taille_population // 2)

        nouvelle_generation = []
        for _ in range(taille_population // 2):
            parent1, parent2 = random.sample(parents, 2)
            enfant1, enfant2 = croisement(parent1, parent2)
            enfant1 = mutation(enfant1, taux_mutation)
            enfant2 = mutation(enfant2, taux_mutation)
            nouvelle_generation.append(enfant1)
            nouvelle_generation.append(enfant2)

        population = nouvelle_generation

    print("Aucune solution optimale trouvée.")
    return None

# Exemple d'utilisation
algorithme_genetique(taille_population=500, generations=1000, taux_mutation=0.6)
# print(evaluer([6, 0, 2, 7, 5, 3, 1, 4]))
# si le nombre la taille de la populatione est de 10 il nous faut en moyenne 4000 iterations
# pour une population de 500 individu on a environs 300 iteration en moyenne
#50 iterations en moyenne pour une population de 5000 individus
