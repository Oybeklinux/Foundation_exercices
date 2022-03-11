"""
13. Yuqoridagi dasturni universallashtiramiz. Endi mazkur vaqtni ham qo'shiladigan minutni ham foydalanuvchi kiritsin.

Hozirgi vaqt soatini kiriting: 13
Hozirgi vaqt minutini kiriting: 20
Qancha minutdan keyin vaqtni bilmoqchisiz? 100
100 minutdan keyin vaqt 15:00 bo'ladi

"""
h_soat = hozirgi_soat = int(input("Hozirgi vaqt soatini kiriting: "))
h_minut = hozirgi_minut = int(input("Hozirgi vaqt minutini kiriting: "))
qiymat = int(input("Qancha minutdan keyin vaqtni bilmoqchisiz? "))

umumiy_minut = hozirgi_minut + qiymat
hozirgi_soat = hozirgi_soat + umumiy_minut // 60
hozirgi_minut = umumiy_minut % 60

print(str(h_soat) + ":"+str(h_minut) + " ga " + str(qiymat) + " minut qo'shilsa,  vaqt " + str(hozirgi_soat) + ":" + str(hozirgi_minut) + " bo'ladi")