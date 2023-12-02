# script de calcule de dsicriminent
import math

print("---Calculateur de Diecriment degree 2---")
print("entre la valeur de aX^2 ")
a = int(input())
print("entre la valeur de bX ")
b = int(input())
print("entre la valeur de c ")
c = int(input())
disc = ((b ^ 2) - (4 * a * c))
print(disc)
if disc.__gt__(0):
    x1 = (math.sqrt(disc) - b)/2*a
    x2 = -(math.sqrt(disc) - b)/2*a
    print(f"X1 = {x1} and X2 = {x2} ")
else :
    print("the polynom dont have root")