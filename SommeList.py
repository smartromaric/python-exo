def multiply(*numbers):
    prod = 1
    for number in numbers:
        prod *=number
    print(f"le produit de la liste est {prod} ")
    

multiply(1,2,3,3,4)