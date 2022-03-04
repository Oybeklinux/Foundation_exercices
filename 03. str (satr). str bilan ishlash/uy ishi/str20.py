son1 = input("Birinchi sonni kiriting: ")
if not son1.isdigit():
    print("Bu son emas")
else:
    son2 = input("Ikkinchi sonni kiriting: ")
    if not son2.isdigit():
        print("Bu son emas")
    else:
        print(f"{son1} * {son2} = {int(son1) * int(son2)}")
