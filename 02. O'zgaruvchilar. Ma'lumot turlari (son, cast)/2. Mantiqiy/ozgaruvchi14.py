"""
12. Hozir vaqt 14:00. 65 minutdan keyin u 15:05 bo'ladi. 70 minutdan keyin 15:10. Mana shuni dasturini yozing. Foydalanuvchi kiritgan minutdan keyin mazkur 14:00 ga nisbatan vaqtni chiqarsin

Hozir soat 14:00
Minutni kiriting: 400
400 minutdan keyin vaqt 20:40 bo'ladi

"""
hozirgi_soat = 14
print("Hozir soat " + str(hozirgi_soat) + ":00")
qiymat = int(input("Minutni kiriting: "))
soat = qiymat // 60
minut = qiymat % 60
hozirgi_soat = hozirgi_soat + soat
print(qiymat, "minutdan keyin vaqt " + str(hozirgi_soat) + ":" + str(minut) + " bo'ladi")