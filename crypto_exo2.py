import numpy as np


# Fonction pour créer une matrice circulante aléatoire de taille donnée
def random_circulant_matrix(size):
    # Génère une liste de nombres aléatoires entre 0 et 255 (valeurs ASCII)
    random_ascii = np.random.randint(0, 256, size)

    # Crée la matrice circulante avec les nombres aléatoires
    matrix = np.array([[random_ascii[(i - j) % size] for j in range(size)] for i in range(size)])

    return matrix


# Demande à l'utilisateur de spécifier la taille de la matrice circulante
size = int(input("Entrez la taille de la matrice circulante : "))

# Crée une matrice circulante aléatoire de la taille spécifiée
circulant_matrix = random_circulant_matrix(size)

# Affiche la matrice circulante
print("Matrice circulante aléatoire :")
print(circulant_matrix)
