# list -1
# r1 = []
# r2 = [1,2,3,4,5]
# r3 = ['olma', 'anor', 'banan', 'uzum', 'nok']
# r4 = [True, False, True, True, False]
# print(f"Birinchi ro'yxat: {r1}. Uning uzunligi: {len(r1)}")
# print(f"Birinchi ro'yxat: {r2}. Uning uzunligi: {len(r2)}")
# print(f"Birinchi ro'yxat: {r3}. Uning uzunligi: {len(r3)}")
# print(f"Birinchi ro'yxat: {r4}. Uning uzunligi: {len(r4)}")
# list 2
# r1 = []
# r2 = [1,2,3,4,5]
# r3 = ['olma', 'anor', 'banan', 'uzum', 'nok']
# r4 = [True, False, True, True, False]
# print(f"Birinchi ro'yxat turi: {type(r1)}. ")
# print(f"Birinchi ro'yxat turi: {type(r2)}. Qiymatining turi: {type(r2[0])}")
# print(f"Birinchi ro'yxat turi: {type(r3)}. Qiymatining turi: {type(r3[0])}")
# print(f"Birinchi ro'yxat turi: {type(r4)}. Qiymatining turi: {type(r4[0])}")
# list 3
# royxat = ['olma', True, 3.14, 3_000, [1,2,3,4]]
# print(f"Ro'yxat: {royxat}. Uning toifasi: {type(royxat)}")
# print(f"Birinchi element: {royxat[0]}. Uning toifasi: {type(royxat[0])}")
# print(f"Birinchi element: {royxat[1]}. Uning toifasi: {type(royxat[1])}")
# print(f"Birinchi element: {royxat[2]}. Uning toifasi: {type(royxat[2])}")
# print(f"Birinchi element: {royxat[3]}. Uning toifasi: {type(royxat[3])}")
# print(f"Birinchi element: {royxat[4]}. Uning toifasi: {type(royxat[4])}")
# list 4
# bozorlik = ['anor', 'banan', 'kartoshka', 'sabzi', 'qulupnay',
#             'sholg\'om', 'balg\'ari', 'baliq', 'mol go\'shti', 'qaymoq']
# print(f"Birinchisi: {bozorlik[0]}")
# print(f"Ohiridagisi: {bozorlik[-1]}")
# print(f"2,3,4 o'rindagi mahsulotlar: {bozorlik[1:4]}")
# print(f"Boshidan 5 tasi: {bozorlik[:5]}")
# print(f"Ohiridan 5 tasi: {bozorlik[-5:]}")
# list 5
# satr = input(f"qulupnay:sabzi:anor ko'rinishida kamida 4 mahsulot kiriting: ")
# royxat = satr.split()
# print(f"boshidagi 2 mahsulot: {royxat[0:2]}")
#list 6
# satr = input(f"qulupnay-sabzi-anor ko'rinishida kamida 4 mahsulot kiriting: ")
# royxat = satr.split("-")
# print(len(royxat) >= 4)
# list 10
# mahsulotlar = input("kamida 5 mahsulotlarni ',' bilan yozing: ")#
# print(f"Ro'yxat: {mahsulotlar}")
# mahsulotlar = mahsulotlar.split(",")
# qiymat = input("2 va 3 mahsulotlar o'rniga nima(lar) olasiz? ") #karam
# qiymat = qiymat.split(",")
# mahsulotlar[1:3] = qiymat
# print(f"O'zgargan ro'yxat: {mahsulotlar}")
# olma,nok,anor,bodring,sabzi,uzum
# go'sht,tovuq,bodom,yer-yong'oq
# list 11
# sonlar = [1,2,3,4]
# print(f"Ro'yxat: {sonlar}")
# son = int(input("Son kiriting: "))
# sonlar.append(son)
# print(f"O'zgargan ro'yxat: {sonlar}")
# list 14
# bozorlik = ['olma', 'nok']
# print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
# meva = input("Bitta muhim bo'lmagan mahsulot yozing: ")
# bozorlik.append(meva)
# print(f"O'zgargan ro'yxat: {bozorlik}")
# meva = input("Endi bitta muhim mahsulot yozing: ")
# bozorlik.insert(1, meva)
# print(f"O'zgargan ro'yxat: {bozorlik}")
# meva = input("Endi bir nechta muhim bo'lmagan mahsulotlarni ',' bilan yozing: ")
# bozorlik.extend(meva.split(","))
# print(f"O'zgargan ro'yxat: {bozorlik}")
sonlar = [1,2,3,4,5]
print(f"Boshlang'ich holat: {sonlar}")
sonlar.clear()
print(f"O'zgargan holat: {sonlar}")








# x0 = 2
# y0 = 6
#
# while True:
#     exist = False
#     x1 = int(input("x1 = "))
#     y1 = int(input("y1 = "))
#     if not (1 <= x1 < 9 and 1 <= y1 < 9):
#         continue
#
#     n = x1 - x0
#     if n > 0:
#         if x1 == x0 + n and y1 == y0 + n or x1 == x0 + n and y1 == y0 - n:
#             exist = True
#     elif n < 0:
#         n *= -1
#         if x1 == x0 - n and y1 == y0 - n or x1 == x0 - n and y1 == y0 + n:
#             exist = True
#
#     if exist:
#         print("To'g'ri")
#     else:
#         print("Xato")
#

# from datetime import date
# import locale
# locale.setlocale(locale.LC_TIME, 'uz_Uz.UTF-8')
#
# sana = date(2020, 2, 14)
# print(sana)
# print(sana.strftime("""
# Sana:
#     %x (mahalliy format bo'yicha)
# Hafta kuni:
#     %a (qisqa nomi)
#     %A (to'liq nom)
#     %w (tartib raqami)
# Oy kuni:
#     %d (tartib raqami)
# Oy:
#     %b (qisqa nomi)
#     %B (to'liq nomi)
#     %m (tartib raqami)
# Yil:
#     %y (2 raqamli)
#     %Y (4 raqamli)
# """))
                          # "Vaqt:
                          # "%H (soat)
                          # "%I (soat)
                          # "%M (daqiqa)
                          # "%S (soniya)
                          # "Sana va vaqt:
                          # "%c(o'zbek tili formatida sana va vaqt)
                          # "%x(o'zbek tili formatida sana)
                          # %% (belgi)"


                          # ))
# 1. Mahsulot haqidagi ma'lumotni foydalanuvchidan so'rang, so'ng shu ma'lumotlarni json faylga kiriting. Mahsulot nomi, soni, narxi, oluvchi va sotib olgan vaqtni faylga kiritamiz
# ```text
# Siz qaysi mahsulotni sotib oldingiz? Olma
# Nechta? 10
# Qanchadan? 5000
# Ismingiz? Otabek
# ```
# from datetime import date
# import json
#
# mahsulot = {
#     "nomi": 'olma',
#     'soni': 10,
#     'narxi': 5000,
#     'sanasi': date.today(),
#     'oluvchi': 'Otabek'
# }
# with open('mahsulotlar', 'w') as file:
#     json.dump(mahsulot)
