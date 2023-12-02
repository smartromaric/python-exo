import numpy as np

# Fonction pour créer une matrice circulante à partir d'une liste
def circulant_matrix(lst):
    # n = 3
    n = len(lst)
    return np.array([[lst[(i-j)%n] for j in range(n)] for i in range(n)])

# Fonction pour convertir une chaîne de caractères en une liste de codes ASCII
def convert_to_ascii(text):
    return [ord(char) for char in text]

# Demande à l'utilisateur d'entrer une chaîne de caractères
user_input = input("Entrez une chaîne de caractères : ")

# Convertit la chaîne de caractères en une liste de codes ASCII
ascii_list = convert_to_ascii(user_input)

# Remplit la liste avec des zéros si sa longueur n'est pas un multiple de 3
while len(ascii_list) % 8 != 0:
    ascii_list.append(ord(str(0)))

# Crée la matrice circulante avec les codes ASCII
matrix = circulant_matrix(ascii_list)

# Affiche la matrice circulante
print("Matrice circulante :")
print(matrix)
