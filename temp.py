def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def exp(x, n):
    summa = 0
    j = 0
    for i in range(0, n, 1):
        j += 1
        summa += ((-1) ** i) * x ** (2*i) / (factorial(2*i))
        print(f"qadam-{j}: {x ** (2*i) / (factorial(2*i))}")
    print(f"Yig'indisi: {summa}")
    return summa


x = int(input("x: "))
n = int(input("Daraja n: "))
natija = exp(x, n)
