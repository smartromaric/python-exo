import numpy as np

def est_inversible(matrix, p):
    try:
        determinant = int(np.linalg.det(matrix) % p)
        return determinant != 0
    except np.linalg.LinAlgError:
        return False

def elements_inversibles(m, p):
    # Génère une liste de toutes les matrices carrées circulantes 2x2 modulo p
    matrices = []
    
    for i in range(p):
        for j in range(p):
            # Assurez-vous que les éléments sont disposés de manière circulante
            a = i
            b = j
            c = (i + 1) % p
            d = (j + 1) % p
            matrices.append(np.array([[a, b], [c, d]]))

    inversibles = []

    for matrix in matrices:
        if est_inversible(matrix, p):
            inversibles.append(matrix)

    return inversibles

# Exemple d'utilisation :
m = 2  # Nombre de lignes et de colonnes
p = 2  # Modulo p
resultat = elements_inversibles(m, p)
print("Matrices carrées circulantes inversibles modulo", p, "dans 𝒞" + str(m) + "(ℤ ∕ " + str(p) + "ℤ) :")
for matrice in resultat:
    print(matrice)
