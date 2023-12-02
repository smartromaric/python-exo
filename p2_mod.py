import numpy as np

# Définition de l'ensemble de matrices circulantes 2x2 modulo 3
matrices = [np.array([[a, b], [b, a]]) % 5 for a in range(5) for b in range(5)]

# Fonction pour vérifier si une matrice est un générateur
def is_generator(matrix, matrices):
    powers = set()
    for _ in range(len(matrices)):
        powers.add(tuple(matrix.ravel()))  # Ajoute la matrice actuelle à l'ensemble
        matrix = np.dot(matrix, matrix) % 3  # Effectue la multiplication matricielle et le modulo 3
    print(len(powers) == len(matrices))
    return len(powers) == len(matrices)  # Renvoie True si toutes les matrices sont uniques

# Recherche d'un générateur
generator_found = False
for matrix in matrices:
    if is_generator(matrix, matrices):  # Appelle la fonction pour vérifier si la matrice est un générateur
        generator_found = True
        print("Générateur trouvé:")
        print(matrix)
        break

if not generator_found:
    print("Aucun générateur trouvé.")


ALGORITHME TrouverElementPrimitif(m, n)
    POUR i DE 1 À n - 1 FAIRE
        élément = MatriceCirculanteUnitaire(m, n, i)
        SI EstElementPrimitif(élément, m, n) ALORS
            RETOURNER élément
        FIN SI
    FIN POUR
    RETOURNER AucunÉlémentPrimitif

ALGORITHME EstElementPrimitif(élément, m, n)
    puissances = ENSEMBLE_VIDE
    puissance = CopierMatrice(élément)
    TANT QUE taille(puissances) < n - 1 ET puissance NON DANS puissances FAIRE
        ajouter puissance à puissances
        puissance = MultiplierMatrices(puissance, élément, m, n)
    FIN TANT QUE
    RETOURNER taille(puissances) = n - 1

ALGORITHME MultiplierMatrices(matrice1, matrice2, m, n)
    matrice_résultante = MatriceNulle(m, n)
    POUR i DE 1 À m FAIRE
        POUR j DE 1 À m FAIRE
            POUR k DE 1 À m FAIRE
                matrice_résultante[i][j] = (matrice_résultante[i][j] + matrice1[i][k] * matrice2[k][j]) MOD n
            FIN POUR
        FIN POUR
    FIN POUR
    RETOURNER matrice_résultante

ALGORITHME MatriceNulle(m, n)
    matrice = MATRICE_VIDE de dimensions m x m
    POUR i DE 1 À m FAIRE
        POUR j DE 1 À m FAIRE
            matrice[i][j] = 0
        FIN POUR
    FIN POUR
    RETOURNER matrice

ALGORITHME MatriceCirculanteUnitaire(m, n, i)
    matrice = MATRICE_VIDE de dimensions m x m
    POUR j DE 1 À m FAIRE
