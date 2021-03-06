# Mavzu 1: Print, input, izoh, xatoliklar, terminlar
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
qiymat         - 0,1,2, "abc", 'abc', 5.6, """Matn""",True, False
o'zgaruvchi    - son, soz1, _gap, guruh, Alfavit
qiymat turi    - bool(mantiqiy qiymat: True, False). Qiymatlar ma'nosi: True - haqiqat, False - yolg'on 
                 int(butun sonlar): -4, -2, 1, 5, 7 ..
                 float(haqiqiy sonlar): -4.5, 0, 6.6, 9,6 ..
                 str(matn, satr): 'soz', "soz", """soz"""
funksiya       - kodlarni qisqartirish uchun, ma'lum vazifani bajaradigan kodlarni ajratish uchun
print          - qiymatni ekranga chiqaradigan funksiya
input          - foydalanuvchidan qiymat o'qiydigan funksiya
parametr       - def summa(a, b): return a+b. Bu yerda a va b parametr 
argument       - print("Otabek"). Bu yerda "Otabek" argument  
debug          - dasturni xatolikka tekshirish
```
### 1.2 O'qish uchun materiallar
- sariq dev
  - [02 hello world](https://python.sariq.dev/ilk-qadamlar/hello-world)
  - [#03 print, sintaksis va arifmetik amallar](https://python.sariq.dev/ilk-qadamlar/03-print)
- w3schools
  - [Python syntax](https://www.w3schools.com/python/python_syntax.asp)
  - [Python comments](https://www.w3schools.com/python/python_comments.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**

- [2.1 Print](#21-print)
  - [2.1.1 Turlicha ishlatilishi](#211-turlicha-ishlatilishi)
  - [2.1.2 Misollar](#212-misollar)
- [2.2 Arifmetika](#22-arifmetika)
- [2.3 Izoh](#23-izoh)
- [2.4 Xatoliklar bilan ishlash](#24-xatoliklar-bilan-ishlash) 
- [2.5 Input](#25-input)
  - [2.5.1 Turlicha ishlatilishi](#251-turlicha-ishlatilishi)
  - [2.5.2 Misollar](#252-misollar)

### 2.1 Print
#### 2.1.1 Turlicha ishlatilishi
```python
print(1)
print(1,2)
print(1+4)
print('bir' + ' ikki')
print('bir', ' ikki')
print("PC")
print("""Ko'p qatorli 
matn""")
print("\" - qo'shtirnoq")
print('" - qo\'shtirnoq')
print("' - birtirnoq")
print('\' - birtirnoq')
print('Birinchi qator\nIkkinchi qator')
print('Birinchi ustun\t\tIkkinchi ustun')
```
#### 2.1.2 Misollar
1. Ekranga qiymatni(son, matn) chiqarish:

```python
print("Assalom alaykum")
```
```text
Assalom alaykum
```
yoki
```python    
print('Assalom alaykum')
```
```textmate
Assalom alaykum
```
2. Ekranga ' va " belgisi bilan chiqarish
```python  
print('Mening ismim "Otabek"')
```
```text
Mening ismim "Otabek"
```
yoki
```python  
print("Mening ismim 'Otabek'")
```
```text
Mening ismim 'Otabek'
```
yoki
```python  
print('Mening ismim \'Otabek\'')
```
```text
Mening ismim 'Otabek'
```
yoki
```python  
print("Mening ismim \"Otabek\"")
```
```text
Mening ismim "Otabek"
```
3. Ko'p qatorli matnni chiqarish
```python
print("""Bu mening birinchi darsim
Birinchi darsda print ni o'rgandik""")
```
```text
Bu mening birinchi darsim
Birinchi darsda print ni o'rgandik
```
4. Bir nechta qiymat berish
```python  
print("Ismim: ", "Otabek", "Yoshim:", 34)
```
```text
Ismim:  Otabek Yoshim: 34
```
yoki
```python  
print("To'rtburchak eni 4, bo'yi 5. \nTo'rtburchak yuzi: ", 4 * 5)
```
```text
To'rtburchak eni 4, bo'yi 5. 
To'rtburchak yuzi:  20
```
5. Maxsus belgilar ishlatish
```python  
print("Ismim:\tOtabek\nYoshim:\t34")
```
```text
Ismim:	Otabek
Yoshim:	34
```
### 2.2 Arifmetika

1. Bo'lish
```python
print(10 / 6)
```
```text
1.6666666666666667
```
```python
print(10 / 5)
```
```text
2.0
```
```python
print(10 - 5)
```
```text
5
```
```python
print(10 + 5)
```
```text    
15
```
2. Butun qismini olish
```python
print(10 // 3)
```
```text
3
```
3. Qoldig'ini olish
```python
print(10 % 3)
```
```text
1
```
4. Darajaga oshirish
```python
print(3 ** 4)
```
```text
81
```
5. Murakkab misollar
```python
print((2 ** 3 + 10/5) // 5)
```
```text
2.0
```
### 2.3 Izoh
1. Bir qatorli izoh
 ```python
#aylana yuzi
print(2 * 3.14 * 5 ** 2)
```
2. Ko'p qatorli izoh:
```python
"""
    aylana yuzi
    pi=3.14
    R=5
"""
pi=3.14
R=5
print(2 * pi * R ** 2)
```
### 2.4 Xatoliklar bilan ishlash
Quyidagi kodlarni ishga tushiring. Konsolga chiqarilgan xatoliklarni tushunishga va yodlashga harakat qiling, bu sizni keyinchalik shu xatolik chiqqanda tez to'g'irlashingizga olib keladi
1. "Dasturning nega o'rganmoqchi?" Bilaman nima deb yozilganini tushunmadingiz, chunki grammatikada xatolik bor. Huddi shunday dasturda xam xatolik bo'lsa kompyuter uni tushunmaydi. Masalan quyidagi kodda + tushib qolgan
```python
print(1 3)
```
Bu xato, aslida bunday bo'lishi kerak
```python
print(1 + 3)
```
2. Qiymat bilan o'zgaruvchini farqi bor
```python
print(son)
```
bu xatolik, chunki son hali e'lon qilinmadi, aslida bunday bo'lishi kerak
```python
son = 3
print(son)
```
3. Siz Program so'zini chiqarmoqchisiz, lekin ' yoki " ni esdan chiqardingiz:
```python
print(Program)
```
Bu xato kompyuter uni o'zgaruvchi deb o'ylaydi va bundan avvalgi kodlarda shu o'zgaruvchini e'lon qilinganligini tekshiradi, agar topmasa xatolik beradi, aslida
```python
print("Program")
```
yoki
```python
print('Program')
```
4. Sonlar bilan satrni qo'shib bo'lmaydi
```python    
print(5 + "5")
```
Bu xato, aslida bunday bo'lishi kerak
```python
print(5 + 5)
```
5. print funksiyasi umuman hamma funksiyalar nomidan so'ng albatta () belgisi bo'ladi.
```python
print "Ismim" + " Otabek"
```
Bu xato , aslida bunday bo'lishi kerak edi
```python
print("Ismim" + " Otabek")
```
yoki
```python
print("Ismim Otabek")
```
6. Kodlar bir tekis yozilishi kerak
```python
print('Birinchi dars')
   print('Python')
print('Dasturlash asoslari')
```
Bu xato , aslida bunday bo'lishi kerak edi
```python
print('Birinchi dars')
print('Python')
print('Dasturlash asoslari')
```
### 2.5 Input
#### 2.5.1 Turlicha ishlatilishi
```python
input("") # bu foydalanuvchiga umuman tushunarsiz
input("So'z kiriting") #kiritilgan qiymat matnga yopishib qoladi
input("So'z kiriting: ") #shunisi qulay
```
#### 2.5.2 Misollar
1. Foydalanuvchidan qiymat o'qish uchun input ishlatiladi
```python
input("So'z kiriting: ")
```
```text
So'z kiriting:
```
2. Kiritilgan soz yordamida boshqa jumla yasab ekranga chiqarish
```python
print("Assalomu alaykum " + input("Ism kiriting: "))
```
```text
Ism kiriting: Otabek
Assalomu alaykum Otabek
```
3. Foydalanuvchi kiritgan soz uzunligini chiqararamiz:
```python
print("So'z uzunligi: ", len(input("So'z kiriting: ")), " ta belgidan iborat")
```

## 3. Amaliyot. O'quvchi
- [3.1 Print](#31-print)
  
- [3.2 Arifmetika](#32-arifmetika)
  
- [3.3 Izoh](#33-izoh)
  
- [3.4 Xatoliklar bilan ishlash](#34-xatoliklar-bilan-ishlash)
  
- [3.5 Input](#35-input)
  


### 3.1 Print

1. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print1.py))
```text
Men dasturchiman
```
2. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print2.py))
```text
Men 'mohir' dasturchiman
```
3. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print3.py))
```text
Birinchi kunim juda ajoyib o'tdi.
Chunki zo'r "motivatsiya" bilan borgandim.
Keyin esa motivatsiyam yo'qolib qoldi.
Keyin tushundimki insonga motivatsiya emas, mas'uliyatni his qilish, javobgarlikni olish, muntazamlilik, tartib-intizom muhim ekan
```
4. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print4.py))
```text
***********
*********
*******
*****
***
*
```
5. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print5.py))
```text
     *
    ***
   *****
  *******
 *********
***********
```
6. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print6.py))
```text
 ______________
|              |
|              |
|              |
|              |
|______________|
```
7. Ekranga quyidagini chiqaring ([Yechim](1.%20Sintaksis/print7.py))
```text
     /\
    /  \    
   /    \
  /      \  
 /        \ 
/__________\
```
### 3.2 Arifmetika
8. 10 + 20 natijasini ekranga chiqaring ([Yechim](1.%20Sintaksis/arifmetika1.py))
```text   
30
```
9. 365 // 7 (Yilda hafta soni) natijasini ekranga chiqaring ([Yechim](1.%20Sintaksis/arifmetika2.py))
```text
52
```
10. 200 kunda necha hafta borligini hisoblab ekranga chiqaring ([Yechim](1.%20Sintaksis/arifmetika3.py))
```text
200 kunda 28 ta hafta bor
```
11. 2022 - 30 (yoshiga qarab yilini aniqlash) natijasini ekranga quyidagi formatda chiqaring ([Yechim](1.%20Sintaksis/arifmetika4.py))
```text
Siz 1992 yilsiz
```
12. 35 ni 8 bo'lib, qoldig'ni chiqaring ([Yechim](1.%20Sintaksis/arifmetika5.py))
```text
35 ni 8 bo'lganda 3 qoldiq qoladi
```
13. 35 ni 8 bo'lib, butun qismini ekranga chiqaring ([Yechim](1.%20Sintaksis/arifmetika6.py))
```text    
35 ni 8 bo'lib butun qismini olsa 4 bo'ladi
```
### 3.3 Izoh

14. Yuqoridagi misolni qayta yozing, so'ng unga izoh yozing 

### 3.4 Xatoliklar bilan ishlash
15. Quyida xatoni topib to'g'irlang ([Yechim](1.%20Sintaksis/xatolik1.py)):
```python
print("Assalomu alaykum)
```
16. Quyida xatoni topib to'g'irlang ([Yechim](1.%20Sintaksis/xatolik2.py)):
```python
print("Assalomu alaykum"
```
17. Quyida xatoni topib to'g'irlang ([Yechim](1.%20Sintaksis/xatolik3.py):
```python
print_("Assalomu alaykum")
```
18. Quyidagi kodda xatoliklar bor. Topib to'g'irlang ([Yechim](1.%20Sintaksis/xatolik4.py))
```python
print(Birinchi dars n")
print(" "+" belgisi ikki sonni qo'shish uchun ishlatiladi.")
print(('print funksiyasi: print("Assalomu " + "alaykum")')
    print("Shuningdek + belgisi ikki satrni qo'shish uchun ham ishlatiladi")
```
Ekranga quyidagi habar chiqishi kerak
```text
Birinchi dars 

"+" belgisi ikki sonni qo'shish uchun ishlatiladi.
print funksiyasi: print("Assalomu " + "alaykum")
Shuningdek '+' belgisi ikki satrni qo'shish uchun ham ishlatiladi
```
### 3.5 Input
19. Quyidagi ko'rinishga ega dastur tuzing ([Yechim](1.%20Sintaksis/input1.py))
```text
Daftarlar sonini kiriting: 12 
12 daftar bor ekan
```
20. Foydalanuvchi ismini kiritsin, chiqishda esa tizimga kirganligi  haqida habar bering ([Yechim](1.%20Sintaksis/input2.py))
```text
Ismingiz nima: Otabek
Otabek, siz tizimga muvaffaqiyatli kirdingiz
```
21. Quyidagi ko'rinishga ega dastur tuzing ([Yechim](1.%20Sintaksis/input3.py))
```text
Belgi kiriting: @@@
Agar kiritilgan belgini 3 martaga ko'paytirsak  @@@@@@@@@ hosil bo'ladi
```