from timeit import timeit
# print("entry a first number")
# one = int(input())
# two = int(input())
# if one.__ne__(0):
#     print(one/two)
# else:
#     raise ValueError("value two  entry is not a number")
code1 = """
def checkAge(age):
    if age.__lt__(0):
        raise ValueError("age must be gt 0")
    return 10/age

checkAge(7)
"""

code2 = """
def checkAge2(age):
    if age.__ne__(0):
        return None
    return 10/age
checkAge2(7)
"""

print(f"code1 {timeit(code1,number=1000)}")
print(f"code2 {timeit(code2,number=1000)}")

