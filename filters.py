L1= [("apple",5),("bananas",11),("orange",15)]

# check if "e" in list
L1_F_e = list(filter(lambda item: "e" in item[0],L1))
# product that price is ge 10
L1_F = list(filter(lambda item: item[1]>=10,L1))
print(L1_F_e)
print(L1_F)
