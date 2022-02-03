soz = input("So'z kiriting: ")
if len(soz) % 2 == 0:
    print("Bu so'zda o'rta harf yo'q")
else:
    orta_indeks = len(soz) // 2
    print(f"Bu so'zda o'rta harf: {soz[orta_indeks]}")

