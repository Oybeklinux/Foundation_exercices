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
1. Mahsulot haqidagi ma'lumotni foydalanuvchidan so'rang, so'ng shu ma'lumotlarni json faylga kiriting. Mahsulot nomi, soni, narxi, oluvchi va sotib olgan vaqtni faylga kiritamiz
```text
Siz qaysi mahsulotni sotib oldingiz? Olma
Nechta? 10
Qanchadan? 5000
Ismingiz? Otabek
```


