print("welcome in phone Contact")
Dic = {}
while True :
    print("""
    1-add,2-remove,3-show all
    """)
    choice = int(input())
    print("--adding menu")
    if choice == 1:
        print("add a name")
        Dic["name"]= input()
        print("add a number")
        Dic["contact"]= input()
        print(Dic)
    elif choice == 2:
        print("name to remove")
        ans = input()
        Dic.get(ans)
    elif choice ==3:
        print(Dic)