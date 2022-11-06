a = int(input("Enter first number"))
b = int(input("Enter second number"))

print(a + b)
print(a - b)
print(a * b)

n = int(input("Enter number").strip())
if 1 <= n <= 100:
    if n % 2 != 0:
        print("Weird")
if 1 <= n <= 100:
    if n % 2 == 0:
        print("Not Weird")
n = int(input())
for num in range(1, n + 1):
    print(num, end='')
