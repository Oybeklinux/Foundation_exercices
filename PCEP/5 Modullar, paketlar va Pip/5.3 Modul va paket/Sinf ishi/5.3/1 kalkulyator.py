def qoshish(x, y):
    return x + y

def ayirish(x, y):
    return x - y

def kopaytirish(x, y):
    return x * y

def bolish(x, y):
    return x / y

print("Amallar ro'yxati:")
print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")

tanlov = input("Amalni tanlang (1/2/3/4): ")

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if tanlov == '1':
    print(son1, "+", son2, "=", qoshish(son1, son2))
elif tanlov == '2':
    print(son1, "-", son2, "=", ayirish(son1, son2))
elif tanlov == '3':
    print(son1, "*", son2, "=", kopaytirish(son1, son2))
elif tanlov == '4':
    if son2 != 0:
        print(son1, "/", son2, "=", bolish(son1, son2))
    else:
        print("Nolga bo'lish mumkin emas!")
else:
    print("Noto'g'ri tanlov!")
