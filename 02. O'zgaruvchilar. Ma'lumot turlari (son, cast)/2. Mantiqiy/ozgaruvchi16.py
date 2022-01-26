"""
16. Yuqoridagi masalaga ozgina o'zgartirish qilamiz. Yana foydalanuvchi qavatni kiritadi dastur usha qavatda 3 honadon raqamlarini chiqarib berishi kerak

30 honadondan iborat 10 qavatli binoga hush kelibsiz
Bino qavatini kiriting: 5
5-qavatda 13, 14 va 15-honadonlar joylashgan

"""
import math

print("30 honadondan iborat 10 qavatli binoga hush kelibsiz")
qavat = int(input("Bino qavatini kiriting: "))
honadon = qavat * 3
print(str(qavat) + "-qavatda " + str(honadon - 2) + ", " + str(honadon - 1) +
      " va " + str(honadon) + "-honadonlar joylashgan")