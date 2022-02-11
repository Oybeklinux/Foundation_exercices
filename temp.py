x0 = 2
y0 = 6

while True:
    exist = False
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    if not (1 <= x1 < 9 and 1 <= y1 < 9):
        continue

    n = x1 - x0
    if n > 0:
        if x1 == x0 + n and y1 == y0 + n or x1 == x0 + n and y1 == y0 - n:
            exist = True
    elif n < 0:
        n *= -1
        if x1 == x0 - n and y1 == y0 - n or x1 == x0 - n and y1 == y0 + n:
            exist = True

    if exist:
        print("To'g'ri")
    else:
        print("Xato")

