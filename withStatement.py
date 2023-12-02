try:
    with open("student.txt") as Student:
        print("votre nom je vous prie")
        name = input()
        old = input()
        Student.write()
except:
    print("file cant open!!")