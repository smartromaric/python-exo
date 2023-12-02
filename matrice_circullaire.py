import numpy as np


def MatCircu(chaines):
    if not len(chaines) %3 ==0:
        chaines+="0"
    print(chaines)

    j=0
    mot3=""
    # mat = np.array([])
    for i in range(2,len(chaines),2):
        j+=i
        # print(chaines[i])
        mot3 = chaines[:j+1]
        print("mot: ",mot3)
        matrice = []
        matrice2 = []
        for e,mot in enumerate(mot3):
            # print("debut enum")
            con_ascii = ord(mot)
            matrice.append(con_ascii)
        print(matrice)

        # print(matrice2)
        # matrice = []

        # print(mot,": ",ord(mot))

        # print(chaines[i-3:i])



    # for i in  range(0,len(chaines)):
    #     var += chaines[i]
    # print(ord(chaines))


# print(ord(" "))
chaine = str(input(""))
print(chaine)
MatCircu(chaine)


# mat = np.array([matrice,matrice,matrice])
# mat[2][-2],mat[2][-1] = mat[2][-1],mat[2][-2]
# mat[1][-3],mat[1][-2] = mat[1][-2],mat[1][-3]
# print("fin")
