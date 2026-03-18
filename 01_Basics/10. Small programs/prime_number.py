n = int(input("introduceti nr: "))

div = 0

for i in range(1, n + 1):
    if n % i == 0:
        div = div + 1

if div == 2:
    print("este prim")
else:
    print("nu este prim")