print("entry the endpoind please")
end = int(input())
cpte = 0
for i in range(1,end):
    if i%2 == 0:
        print (i)
        cpte +=1
print(f"whe have {cpte} even numbers")