"""
15. 10 qavatli bitta podyezddan iborat binoda 30 honadon bor. Foydalanuvchi kiritgan honadon raqamiga qarab uni nechanchi qavatda ekanligini chiqaring
Masalani yechishdan avval math.ceil bilan tanishib chiqing.

30 honadondan iborat 10 qavatli binoga hush kelibsiz
Honadon raqamini kiriting: 6
6-honadon 2-qavatda joylashgan

"""
import math

print("30 honadondan iborat 10 qavatli binoga hush kelibsiz")
honadon = int(input("Honadon raqamini kiriting: "))
qavat = math.ceil(honadon / 3)
print(str(honadon) + "-honadon " + str(qavat) + "-qavatda joylashgan")