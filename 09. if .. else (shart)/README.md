# Mavzu 9: if .. else (shart)
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
shart - natijasi True yoki False qaytadigan har qanday ifoda
else - shart bajarilmasa, else bloki ishga tushadi
elif - aks holda shart bajarilsa
```
### 1.2 O'qish uchun materiallar
- sariq dev
  - [#10 IF ELSE](https://python.sariq.dev/shartlar/10-if-else)
  - [#11 BIR NECHTA SHARTLARNI TEKSHIRISH](https://python.sariq.dev/shartlar/11-if-elif-else)
- w3schools
  - [If ... Else](https://www.w3schools.com/python/python_conditions.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Sintaksis](#21-sintaksis)
- [2.2 if ifodasi](#22-elementlardan-foydalanish)
- [2.3 Joy tashlash (Indentation)](#23-element-ozgartirish)
- [2.4 elif](#24-element-qoshish)
- [2.5 else](#25-element-ochirish)
- [2.6 Qisqacha if](#26-tsiklda-ishlatilishi)
- [2.7 Qisqacha if .. else](#27-lugatdan-nusxa-olish)
- [2.8 Qisqacha if .. elif .. else](#28-tarmoqli-lugat)
- [2.9 And](#29-metodlar)
- [2.10 Or](#29-metodlar)
- [2.11 Tarmoqli if](#29-metodlar)
- [2.11 pass](#29-metodlar)

### 2.1 Sintaksis
Python dasturlash tilida quyidagi shartlar islatiladi:
```text
a == b # a soni b soniga tengmi 
a != b # a soni b soniga teng emasmi
a < b # a soni b sonidan kichikmi
a <= b # a soni b sonidan kichik yoki tengmi
a > b # a soni b sonidan kattami
a >= b # # a soni b sonidan katta yoki tengmi
```
### 2.2 if ifodasi 
1. a = 300 va b = 200. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin
```python
a = 300 
b = 200
if a > b:
    print("a soni b sonidan katta")
```
```text
a soni b sonidan katta
```
### 2.3 Joy tashlash (Indentation)
Ahamiyat bering joy tashlash muhim:
```python
a = 300 
b = 200
if a > b:
print("a soni b sonidan katta")
```
Bu **XATO**. Chunki if blokidan so'ng komandalar surilish kerak.

### 2.4 elif
2. a = 100 va b = 100. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin. Agar a soni b soniga teng bo'lsa "a soni b soniga teng" yozuvi chiqsin
```python
a = 100 
b = 100
if a > b:
    print("a soni b sonidan katta")
elif a == b:
    print("a soni b soniga teng")
```
```text
a soni b soniga teng
```
### 2.5 else
3. a = 100 va b = 200. Agar a soni b sonidan katta bo'lsa, ekranga "a soni b sonidan katta" yozuvi chiqsin. Agar a soni b soniga teng bo'lsa "a soni b soniga teng" yozuvi chiqsin, aks holda "a soni b sonidan kichik" yozuvi chiqsin
```python
a = 100 
b = 100
if a > b:
    print("a soni b sonidan katta")
elif a == b:
    print("a soni b soniga teng")
else:
    print("a soni b sonidan kichik")
```
```text
a soni b sonidan kichik
```

### 2.6 Qisqacha if
```python
a = 100 
b = 100
if a > b:
    print("a soni b sonidan katta")
```
Yuqoridagi kodni quyidagicha yozsak ham bo'ladi
```python
a = 100 
b = 100
if a > b: print("a soni b sonidan katta")
```

### 2.7 Qisqacha if .. else
4. a soni b sonidan katta bo'lsa, "a soni b sonidan katta" habari , agar teng bo'lsa "a soni b soniga teng" habari chiqsin
```python
a = 100 
b = 100
if a == b:
    print("a soni b soniga teng")
else:
    print("a soni b soniga teng emas")
```
Yuqoridagi kodni quyidagicha yozsak ham bo'ladi
```python
a = 100 
b = 100
print("a soni b soniga teng") if a == b else print("a soni b soniga teng emas")
```

### 2.8 Qisqacha if .. elif .. else
5. Agar son manfiy bo'lsa, "manfiy", musbat bo'lsa "musbat", aks holda "0" habari chiqsin
```python
a = 100 
print("manfiy") if a < 0 else print("musbat") if a > 0 else print("0")   
```
```text
musbat
```
### 2.9 And
Bir paytda najarilishi kerakligini bildiradi.
<br>
Agar ikkalar shart True bo'lsagina, natija True bo'ladi va if bloki ishga tushadi, aks holda else bloki yoki elif blokiga o'tadi 
6. Agar son musbat va juft bo'lsa, "musbat va juft" degan habar chiqsin, aks holda "musbat va juft emas" degan habar chiqsin
```python
a = 10
if a > 0 and a % 2 == 0:
    print("musbat va juft")
else:
    print("musbat va juft emas")
```
```text
musbat va juft
```
7. Foydalanuvchi sonni kiritsin, agar son 0 dan katta va 10 dan kichik bo'lsa "son 0 va 10  oralig'ida" degan habar chiqsin, aks holda "Xato" habari chiqsin
```python
son = int(input("Son (0,10) oralig'ida son kiriting"))
if son > 0 and son < 10:
    print("son 0 va 10  oralig'ida")
else:
    print("Xato")
```
Yoki
```python
son = int(input("Son (0,10) oralig'ida son kiriting: "))
if 0 < son < 10:
    print("son 0 va 10  oralig'ida")
else:
    print("Xato")
```
```text
Son (0,10) oralig'ida son kiriting: 13
Xato
```
```text
Son (0,10) oralig'ida son kiriting: 4
son 0 va 10  oralig'ida
```
### 2.10 Or
Ikkala shartlardan kamida bittasi bajarilishi kerakligini bildiradi
<br>
Agar ikkala shartlardan biri True bo'lsa, u holda if bloki ishga tushadi.
8. Agar son1 juft bo'lsa, yoki son2 juft bo'lsa, "Sonlardan biri juft" habari chiqsin
```python
son1 = int(input("1-son:"))
son2 = int(input("2-son:"))
if son1 % 2 == 0 or son2 % 2 == 0:
    print("Sonlardan biri juft")
```
```text
1-son: 12
2-son: 13
Sonlardan biri juft
```
```text
1-son: 17
2-son: 13
```
### 2.11 Tarmoqli if
9. Avval sonni musbatlikka tekshiring. Agar son musbat bo'lsa, u holda tekshiring, agar son 50 dan kichik bo'lsa, "50 dan kichik", aks holda "50 dan katta" habari chiqsin
```python
son = int(input("Son kiriting: "))
if son > 0:
    if son > 50:
        print("50 dan katta") 
    else:
        print("50 dan kichik")
```
```text
Son kiriting: -10
```
```text
Son kiriting: 10
50 dan kichik
```
```text
Son kiriting: 60
50 dan katta
```
### 2.11 pass
pass so'zi hech narsani bildirmaydi, lekin xatolikni oldini oladi
```python
a = 10
if a > 0:
   
```
Bu XATO. Quyidagi kod esa to'g'ri
```python
a = 10
if a > 0:
   pass
```

## 3. Amaliyot. O'quvchi

1. Foydalnuvchi son kiritsin. Agar son musbat bo'lsa, 1 ga ochirilsin. 
```text
Son kiriting: 10
Natija: 11
```
```text
Son kiriting: -10
Natija: -10
```
2. Foydalnuvchi son kiritsin. Agar son musbat bo'lsa, 1 ga ochirilsin, aks holda 2 ga kamaytirilsin.
```text
Son kiriting: 10
Natija: 11
```
```text
Son kiriting: -10
Natija: -8
```
3. Foydalnuvchi son kiritsin. Agar son musbat bo'lsa, 1 ga ochirilsin, agar manfiy bo'lsa 2 ga kamaytirilsin, agar 0 ga teng bo'lsa, songa 10 ni o'zlashtiring
```text
Son kiriting: 10
Natija: 11
```
```text
Son kiriting: -10
Natija: -8
```
```text
Son kiriting: 0
Natija: 10
```
4. Foydalanuvchidan 3 marta son kiritsin. So'ng kiritilgan sonlardan qancha musbat son borligini aniqlab ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: -20
3-sonni kiriting: -30
Musbat sonlar: 1 ta
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 20
3-sonni kiriting: -30
Musbat sonlar: 2 ta
```
```text
1-sonni kiriting: 10
2-sonni kiriting: -20
3-sonni kiriting: 30
Musbat sonlar: 3 ta
```
5. Foydalanuvchidan 3 marta son kiritsin. So'ng kiritilgan sonlardan qancha musbat va manfiy son borligini aniqlab ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: -20
3-sonni kiriting: -30
Musbat sonlar: 1 ta
Manfiy sonlar: 2 ta
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 20
3-sonni kiriting: -30
Musbat sonlar: 2 ta
Manfiy sonlar: 1 ta
```
```text
1-sonni kiriting: 10
2-sonni kiriting: -20
3-sonni kiriting: 30
Musbat sonlar: 3 ta
Manfiy sonlar: 0 ta
```
6. Foydalanuvchi 2 ta son kiritsin. So'ng qaysi biri katta bo'lsa, ekranga habar bersin:
```text
1-sonni kiriting: 10
2-sonni kiriting: 20
20
```
```text
1-sonni kiriting: 100
2-sonni kiriting: 20
100
```
7. Foydalanuvchi 2 ta son kiritsin. So'ng qaysi biri katta bo'lsa, ekranga habar bersin:
```text
1-sonni kiriting: 10
2-sonni kiriting: 20
2-son katta
```
```text
1-sonni kiriting: 100
2-sonni kiriting: 20
1-son katta
```
8. Foydalanuvchi 2 ta son kiritsin. So'ng kiritilgan sonlarni o'sish tartibida ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: 20
10,20
```
```text
1-sonni kiriting: 100
2-sonni kiriting: 20
20,100
```
9. Foydalanuvchi a sonini, keyin b sonini kiritsin. So'ng a va bni qiymatlarini shunday almashtiringki, a kichik b katta bo'lsin
```text
a sonini kiriting: 5
b sonini kiriting: 10
Almashtirishlar bajarilMAdi
a=5, b=10
```
```text
a sonini kiriting: 15
b sonini kiriting: 10
Almashtirishlar bajarildi
a=10, b=15
```
10. Foydalanuvchi 2 ta son kiritsin. So'ng kiritilgan sonlar o'zaro teng bo'lmasa, a=b=a+b bo'lsin, aks holda, a=b=0 bo'lsin
```text
1-sonni kiriting: 10 
2-sonni kiriting: 15
1-son=25
2-son=25
```
```text
1-sonni kiriting: 10 
2-sonni kiriting: 10
1-son=0
2-son=0
```
11. Foydalanuvchi 2 ta son kiritsin. So'ng kiritilgan sonlar o'zaro teng bo'lmasa, ekranga katta sonni chiqaring, aks holda "Ikkalasi barobar" habarini chiqarsin:
```text
1-sonni kiriting: 10 
2-sonni kiriting: 20
Kattasi: 20
```
```text
1-sonni kiriting: 20 
2-sonni kiriting: 20
Ikkalasi barobar
```
12. Foydalanuvchi uchta son kiritsin. Kiritilgan 3 sondan kattasini ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: 15
3-sonni kiriting: 4
Kattasi: 15
```
13. Foydalanuvchi uchta son kiritsin. Kiritilgan 3 sondan o'rtasidagi son ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: 15
3-sonni kiriting: 4
O'rtasidagi son: 10
```
```text
1-sonni kiriting: -10
2-sonni kiriting: 15
3-sonni kiriting: 4
O'rtasidagi son: 4
```
14. Foydalanuvchi uchta son kiritsin. Kiritilgan sonlarni o'sish tartibida ekranga chiqaring:
```text
1-sonni kiriting: 10
2-sonni kiriting: 15
3-sonni kiriting: 4
4,10,15
```
```text
1-sonni kiriting: -10
2-sonni kiriting: 15
3-sonni kiriting: 4
-10,4,15
```
15. Foydalanuvchi uchta son kiritsin. Kiritilgan sonlarni ikkita eng kattasini yig'indisini ekranga chiqarsin:
```text
1-sonni kiriting: -10
2-sonni kiriting: 15
3-sonni kiriting: 4
Ikki katta sonlar yig'indisi: 19
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 15
3-sonni kiriting: 4
Ikki katta sonlar yig'indisi: 25
```
16. Foydalanuvchi uchta son kiritsin. Kiritilgan sonlar o'sish tartibida bo'lsa, sonlar ikkilantirilsin, ask holda ishorasi o'zgartirilsin: 
```text
1-sonni kiriting: 10
2-sonni kiriting: -15
3-sonni kiriting: 4
-10,15,-4
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 12
3-sonni kiriting: 20
20,24,40
```
```text
1-sonni kiriting: 20
2-sonni kiriting: 12
3-sonni kiriting: 10
-20,-12,-10
```
17. Foydalanuvchi uchta son kiritsin. Kiritilgan sonlar o'sish yoki kamayish tartibida bo'lsa, sonlar ikkilantirilsin, ask holda ishorasi o'zgartirilsin: 
```text
1-sonni kiriting: 10
2-sonni kiriting: -15
3-sonni kiriting: 4
-10,15,-4
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 12
3-sonni kiriting: 20
20,24,40
```
```text
1-sonni kiriting: 20
2-sonni kiriting: 12
3-sonni kiriting: 10
40,24,20
```
18. Foydalanuvchi uchta son kiritsin. Kiritilgan sonlardan ikkitasi teng. Uchinchi raqamni tartib raqamini ekranga chiqaring: 
```text
1-sonni kiriting: 20
2-sonni kiriting: 20
3-sonni kiriting: 10
3
```
```text
1-sonni kiriting: 20
2-sonni kiriting: 10
3-sonni kiriting: 10
1
```
```text
1-sonni kiriting: 20
2-sonni kiriting: 5
3-sonni kiriting: 20
2
```
19. Foydalanuvchi to'rtta son kiritsin. Kiritilgan sonlardan uchtasi teng. To'rtinchi raqamni tartib raqamini ekranga chiqaring: 
```text
1-sonni kiriting: 20
2-sonni kiriting: 20
3-sonni kiriting: 10
4-sonni kiriting: 20
3
```
```text
1-sonni kiriting: 10
2-sonni kiriting: 10
3-sonni kiriting: 10
4-sonni kiriting: 20
4
```
20. Foydalanuvchi (1,7) oraliqda son kiritsin. Son mos hafta kunlarini ekranga chiqaring:
```text
Hafta kunini son bilan kiriting: 2
Seshanba
```
```text
Hafta kunini son bilan kiriting: 4
Payshanba
```
21. Foydalanuvchi (1,5) oraliqda son kiritsin. Bu yerda: 1-yomon, 2-qoniqarsiz,3-qoniqarli,4-yaxshi,5-a'lo.
```text
Bahoni kiriting: 5
Qoniqarsiz: a'lo
```
```text
Bahoni kiriting: 2
Qoniqarsiz: qoniqarsiz
```
22. Foydalanuvchi oy raqamini kiritsin, dastur esa bu oy qaysi faslga tegishli ekani chiqsin:
```text
Oy raqamini kiriting: 1
Qish
```
```text
Oy raqamini kiriting: 4
Bahor
```
23. Foydalanuvchi oy raqamini kiritsin, dastur shu oyda necha kun borligini chiqarsin:
```text
Oy raqamini kiriting: 4
30 kun
```
```text
Oy raqamini kiriting: 12
31 kun
```
```text
Oy raqamini kiriting: 2
28 kun
```
24. Foydalnuvchi a va b sonini kiritsin. So'ng amal turini kiritsin (+,-,*,/). So'ng ko'ra a va b soni ustida usha amalni bajarib, ekranga chiqarilsin:
```text
a sonini kiriting: 10
b sonini kiriting: 20
+, -, *, / amallaridan birini yozing: *
10 * 20 = 200
```
```text
a sonini kiriting: 10
b sonini kiriting: 20
+, -, *, / amallaridan birini yozing: +
10 + 20 = 30
```
25. Foydalanuvchi o'lchamni kiritsin. So'ng uning birligini (mm,sm,dm,m,km) yozsin. <br> 
Bu yerda mm (0.001), sm (0.01), dm (0.1), m (1), km (1000). Dastur kiritilgan qiymatni metrga o'girib natijani ekranga chiqarsin:
```text
O'lcham qiymatini kiriting: 30
O'lcham birligini kiriting: sm
30 sm = 0.3 m 
```
```text
O'lcham qiymatini kiriting: 40
O'lcham birligini kiriting: km
40 km = 40000 m 
```
26. Foydalanuvchi og'irlikni kiritsin. So'ng uning birligini (mg,g,kg,t) yozsin. <br> 
Bu yerda mg (0.001), g (1), kg (1000), t (1000000). Dastur kiritilgan qiymatni kg ga o'girib natijani ekranga chiqarsin:
```text
O'lcham qiymatini kiriting: 30
O'lcham birligini kiriting: t
30 t = 3000 kg 
```
```text
O'lcham qiymatini kiriting: 40
O'lcham birligini kiriting: kg
40 kg = 40 kg 
```
27. Foydalanuvchi kun va oy ni kiritsin. Dastur 1 kundan keyin sanani chiqarib bersin
```text
Kunni kiriting: 10
Oyni kiriting: 1
1-oy 11-kun
```
```text
Kunni kiriting: 28
Oyni kiriting: 2
3-oy 1-kun
```
