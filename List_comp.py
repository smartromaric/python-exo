L1= [("apple",5),("bananas",11),("orange",15)]

# get price of all product
L_map = [item[1] for item in L1]
print(L_map)

# check if price is ge 10
L_fil = [item for item in L1 if item[1] >= 10]
print(L_fil)