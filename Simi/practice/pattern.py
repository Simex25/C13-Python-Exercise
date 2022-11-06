for i in range(1, 10):
    print("*" * i)
for i in range(1, 11):
    print(("*" * i).center(20))
for i in range(10, 0, -1):
    print("*" * i)
for i in range(1, 10):
    print(("*" * i).rjust(20))
for i in range(10, 0, -1):
    print(("*" * i).center(20))

num = [n ** i for n,i in range(1, 10)]
print(num)
