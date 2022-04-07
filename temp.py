def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def exp(x, n):
    summa = 0
    for i in range(n):
        summa += x ** i / (factorial(i))
        print(f"qadam-{i + 1}: {x ** i / (factorial(i))}")
    print(f"Yig'indisi: {exp(5, 3)}")
    return summa


print(f"Yig'indisi: {exp(5, 3)}")