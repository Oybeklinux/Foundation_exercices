# Foydalanuvchidan haroratni Selsiy bo'yicha kiritishni so'rash
harorat = float(input("Haroratni Selsiy bo'yicha kiriting: "))

# Harorat diapazonlarini tekshirish
if harorat < -273.15:
    print("Harorat noto'g'ri: mutlaq noldan past")
elif harorat == -273.15:
    print("Harorat mutlaq 0")
elif -273.15 < harorat < 0:
    print("Harorat muzlash darajasidan past")
elif harorat == 0:
    print("Harorat muzlash nuqtasida")
elif 0 < harorat < 100:
    print("Harorat normal diapazonda")
elif harorat == 100:
    print("Harorat qaynash nuqtasida")
elif harorat > 100:
    print("Harorat qaynash nuqtasidan yuqori")
else:
    print("Noma'lum holat")
