from sys import getsizeof
values = (i for i in range(10000000000))
print(getsizeof(values))
for i  in values:
    print(i)