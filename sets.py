# L = [1,2,3,4]
# print(set(L)|{1,8,9})
# print(set(L)&{1,8,9})
# L_set_diff=set(L)-{1,8,9}
# if 2 in L_set_diff:
#     print("yes , exist")

print("Entrer les valeur de L1")
L1 = set(input())
L2 = set(input())
L3 = list(L1-L2)
print(L3)
print(L3[0])