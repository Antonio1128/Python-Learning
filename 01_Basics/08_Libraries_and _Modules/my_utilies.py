def hello(name):
    return f"Hello, {name}!"    

def add(a, b):
    return a + b

def divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

