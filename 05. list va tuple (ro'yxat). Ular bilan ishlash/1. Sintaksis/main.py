def fibonacci(n):
    son1 = 0
    son2 = 1
    for i in range(n):
        if i == 0:
            print(son1)
        elif i == 1:
            print(son2)
        else:
            son1, son2 = son2, son1 + son2
            print(son2)


def fibonacci2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


n = 10
fibonacci(n)
print("\n")
for i in range(n):
    print(fibonacci2(i))