import itertools


def generate_circulant_elements(m, n):
    elements = set()
    for first_row in itertools.product(range(n), repeat=m):
        matrix = []
        for i in range(m):
            matrix.append(list(first_row))
            first_row = first_row[-1:] + first_row[:-1]  # Rotation circulaire
        elements.add(tuple(tuple(row) for row in matrix))
    return elements


def main():
    m = 2  # Ordre de la matrice circulante
    n = 3  # Modulo n
    circulant_elements = generate_circulant_elements(m, n)

    print("Les éléments de C{}(Z/{}Z) sont :".format(m, n))
    for element in circulant_elements:
        for row in element:
            print(row)
        print()
    print("le nombre d'element de  C{}(Z/{}Z) est",len(circulant_elements))

if __name__ == "__main__":
    main()





