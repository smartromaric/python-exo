try:
    open("convert.py")
    print("entry a number")
    nbr = int(input())
    print(nbr/10)
except (ValueError,ZeroDivisionError):
    print("value entry is not a number")
