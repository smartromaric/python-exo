import numpy as np

def generate_circulant_matrices_modulo_2():
    matrices = []
    for i in range(2):
        for j in range(2):
            matrix = np.array([[i, j], [(i + 1) % 5, (j + 1) % 5]])
            matrices.append(matrix)
    return matrices

# Afficher les matrices circulantes modulo 2
matrices_circulantes = generate_circulant_matrices_modulo_2()
for matrix in matrices_circulantes:
    print(matrix)
