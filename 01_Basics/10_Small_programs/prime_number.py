n = int(input("add number: "))

div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div = div + 1

if div == 2:
    print("prime")
else:
    print("not prime")