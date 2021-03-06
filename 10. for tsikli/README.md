# Mavzu 10: for tsikli
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
for - qaytarishlar uchun ishlatiladigan ifoda
break - for dan chiqish
continue - for da keyingi qadama o'tish
```
### 1.2 O'qish uchun materiallar
- sariq dev
  - [#09 FOR TAKRORLASH OPERATORI](https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/09-for-loop)
- w3schools
  - [For loops](https://www.w3schools.com/python/python_for_loops.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Sintaksis](#21-sintaksis)
- [2.2 Satrni takrorlash](#22-satrni-takrorlash)
- [2.3 break ifodasi](#23-break-ifodasi)
- [2.4 continue ifodasi](#24-continue-ifodasi)
- [2.5 range funksiyasi](#25-range-funksiyasi)
- [2.6 for .. else](#26-for--else)
- [2.7 Tarmoqli for](#27-tarmoqli-for)
- [2.8 pass ifodasi](#28-pass-ifodasi)

### 2.1 Sintaksis
Python dasturlash tilida ikkita tsikl bor:
- for
- while

<br>
Tsikl bu takrorlanishlardir. For ifodasi ketma-ketlikka (tuple, list, set, dict, str, va hak) takroriy murojaat qilib har bir elementini o'qish uchun ishlatiladi
<br><br>

1. To'g'ridan to'g'ri massivni berish:
```python
sonlar = [1,2,3]
for son in sonlar:
    print(son)
```
2. Index bilan murojaat qilish:
```python
sonlar = [1,2,3]
for index in range(len(sonlar)):
    print(sonlar[index])
```
### 2.2 Satrni takrorlash
1. Foydalanuvchi kiritgan satrni hamma belgilarini alohida qatorda chiqaring:
```python
satr = input("Biron yozuv kiriting: ")
for belgi in satr:
    print(belgi)
```
```text
Biron yozuv kiriting: python
p
y
t
h
o
n
```
### 2.3 break ifodasi
2. sonlar = [1,3,5,7,9,11,13,15] ro'yxati berilgan. Shulardan 11 gacha hammasini ekranga chiqaring:
```python
sonlar = [1,3,5,7,9,11,13,15]
for son in sonlar:
    if son == 11:        
        break
    print(son)
```
```text
1
3
5
7
9
```
*break* kalitidan keyin keluvchi for blokida joylashgan kodlar ishga tushmaydi   
3. Foydalnuvchi ',' bilan sonlar kiritsin. Toki toq son uchramaguncha sonlarni ekranga chiqarsin.
```python
sonlar = input("',' bilan sonlar kiriting: ").split(",")
for son in sonlar:
    if int(son.strip()) % 2 == 1:
        break
        print(son)
print("Dastur tugadi")
```
```text
',' bilan sonlar kiriting: 2,4,6,8,9,10,12,14
Dastur tugadi
```
### 2.4 continue ifodasi
4. bozorlik = ['olma', 'nok', 'banan', 'qulupnay', 'bodring'] berilgan. Qulupnaydan tashqari hammasini ekranga chiqarsin
```python
bozorlik = ['olma', 'nok', 'banan', 'qulupnay', 'bodring']
for mahsulot in bozorlik:
    if mahsulot == 'qulupnay':
        continue
    print(mahsulot)
```
```text
olma
nok
banan
bodring
```
### 2.5 range funksiyasi
![](images/range1.png)
<br>
![](images/range2.png)
5. 1 dan 10 gacha sonlarni hosil qiling
```python
for i in range(1,11):
    print(i)
```
```text
1
2
3
4
5
6
7
8
9
10
```
6. 9,8,7,6,5,4,3,2,1 sonlarini hosil qiling
```python
for i in range(9,0,-1):
    print(i)
```
```text
9
8
7
6
5
4
3
2
1
```
7. 15,25,35,45,55 sonlarini hosil qiling
```python
for i in range(15, 56, 10):
    print(i)
```
```text
15
25
35
45
55
```
8. 15,25,35,45,55, … ohiri sonlarini hosil qiling. *ohiri* sonini foydalanuvchi kiritsin
```python
ohiri = int(input("Ohirgi chegarani kiriting: "))
for i in range(15, ohiri + 1, 10):
    print(i)
```
```text
Ohirgi chegarani kiriting: 95
15
25
35
45
55
65
75
85
95
```
9. 1 dan 10 gacha sonlarni yig’indisini ekranga chiqaring
```python
summa = 0
for i in range(0, 10):
   summa = summa + i
print(f"Sonlar yig'indisi: {summa}")
```
```text
Sonlar yig'indisi: 55
```
### 2.6 for .. else
for tsiklida ishlatiluvchi *else* kalit so'zi, hamma elementlarni o'qib chiqqandagina ishga tushadi
<br>
10. [1,2,3,4,5,6] sonlardan hammasini ekranga chiqarib, ohirida "Hamma elementlar ekranga chiqarildi" habari chiqsin
```python
sonlar = [1,2,3,4,5,6]
for son in sonlar:
    print(son)
else:
    print("Hamma elementlar ekranga chiqarildi")
```
```text
1
2
3
4
5
6
Hamma elementlar ekranga chiqarildi
```
11. Agar hamma elementlar chiqmasa else bloki ichga tushmaydi:

```python
sonlar = [1,2,3,4,5,6]
for son in sonlar:
    print(son)
    if son == 4:
        break
else:
    print("Hamma elementlar ekranga chiqarildi")
```
```text
1
2
3
4
```

Tsikl umuman takrorlanmasa ham else bloki ishga tushadi:
```python
sonlar = []
for son in sonlar:
    print(son)
else:
    if len(sonlar) == 0:
        print("Ro'yxatda hech qanday element mavjud emas")
    else:
        print("Hamma elementlar ekranga chiqarildi")
```
```text
Ro'yxatda hech qanday element mavjud emas
```
### 2.7 Tarmoqli for
12. Bizda ranglar = ['oq', 'qizil', 'qora'] va ulovlar = ['nexia', 'spark', 'captiva'] rang va ulovlar berilgan. Hamma ulovlarni hamma rangda ekranga chiqaring:
```python
ranglar = ['oq', 'qizil', 'qora']
ulovlar = ['nexia', 'spark', 'captiva']
for rang in ranglar:
    for ulov in ulovlar:
        print(rang, ulov)
```
```text
oq nexia
oq spark
oq captiva
qizil nexia
qizil spark
qizil captiva
qora nexia
qora spark
qora captiva
```
13. Bozorda bozor_mahsulotlari = ['olma', 'nok', 'bodring', 'sabzi'] bor. Sizda ro'yxat bor. Ro'yxatda royxat = ['olma', 'nok', 'banan'] bor. Bozorda sizning ro'yxatingizda bor bo'lgan mahsulotlarni ekranga chiqaring:
```python
bozor_mahsulotlari = ['olma', 'nok', 'bodring', 'sabzi']
royxat = ['olma', 'nok', 'banan']
for bmahsulot in bozor_mahsulotlari:
    for mahsulot in royxat:
        if bmahsulot == mahsulot:
            print(f"{mahsulot} bor")
```
yoki
```python
bozor_mahsulotlari = ['olma', 'nok', 'bodring', 'sabzi']
royxat = ['olma', 'nok', 'banan']
for bmahsulot in bozor_mahsulotlari:    
    if bmahsulot in royxat:
        print(f"{bmahsulot} bor")
```
### 2.8 pass ifodasi
for bloki if bloki kabi bo'sh bo'la olmaydi. Lekin ba'zi sabablarga ko'ra for blokini kechroq yozmoqchi bo'lsangiz, u holda pass kalitini ishlatish kerak
```python
bozor_mahsulotlari = ['olma', 'nok', 'bodring', 'sabzi']
royxat = ['olma', 'nok', 'banan']
for mahsulot in bozor_mahsulotlari:    
    pass
```
14. 2,4,6,8,10 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 30
Sonlar ko'paytmasi: 3840
```
```python
summa = 0
kopaytma = 1
for i in range(2, 11, 2):
   summa = summa + i
   kopaytma = kopaytma * i
print(f"Sonlar yig'indisi: {summa}")
print(f"Sonlar ko'paytmasi: {kopaytma}")
```
15. Quyidagi ro’yxatlar berilgan
- sonlar = [2,3,4,5,6,5,7,3]
- qidir_sonlar = [2, 5]
- qidir_sonlar_summa = [0, 0]
<br>
Bu yerda qidir_sonlar necha marta takrorlanishini hisoblash kerak bo’lgan sonlar va qidir_sonlar_summa takrorlanadigan sonlar sonidan iborat. Endi siz 2 va 5 soni sonlar ro’yxatida  necha marta takrorlanishini hisoblaydigan dastur tuzing

```python
sonlar = [2,3,4,5,6,5,7,3]
qidir_sonlar = [2, 5]
qidir_sonlar_summa = [0, 0]
for son in sonlar:
   for i in range(len(qidir_sonlar)):
       if qidir_sonlar[i] == son:
           qidir_sonlar_summa[i] += 1
for i in range(len(qidir_sonlar)):
   print(f"{qidir_sonlar[i]} soni {qidir_sonlar_summa[i]} marta takrorlangan")
```

## 3. Amaliyot. O'quvchi
1. 1,3,5,7,9 sonlarini hosil qiling. (range bilan)
```text
1
3
5
7
9
```
2. 2,4,6,8,10 sonlarini hosil qiling. (range bilan). 
```text
2
4
6
8
10
```
3. 10,20,30,40,50 sonlarini hosil qiling.
```text
10
20
30
40
50
```
4. 10,8,6,4,2,0 sonlarini hosil qiling
```text
10
8
6
4
2
0
```
5. boshi,…25,35,45,55, …. ohiri  sonlarini hosil qiling. *boshi* va *ohiri* ni foydalanuvchi kiritsin
```text
Boshlang’ich chegarani kiriting: 12
Ohirgi chegarani kiriting: 50
12
22
32
42
```
6. Endi foydalanuvchi boshi va ohiri ni kiritishdan tashqari qadam ni ham kiritsin
```text
Boshlang’ich chegarani kiriting: 12
Ohirgi chegarani kiriting: 50
Qadamni kiriting: 6
12
18
24
30
36
42
48
```
7. 1,3,5,7,9 sonlarini yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 25
```
8. 2,4,6,8,10 sonlarini ko’paytmasini ekranga chiqaring. 
```text
Sonlar yig'indisi: 30
```
9. 9,8,7,6,5,4,3,2,1 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 45
Sonlar ko'paytmasi: 362880
```
10. 10,8,6,4,2 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 30
Sonlar ko'paytmasi: 3840
```
11. 10,8,6,4,2,0 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 30
Sonlar ko'paytmasi: 0
```
12. 15,25,35,45,55 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 175
Sonlar ko'paytmasi: 32484375
```
13. 1 dan 10 gacha sonlarni hosil qiling va shu bilan birga hosil bo’lgan sonni 2ni darajasiga oshiring. Ikkala sonni ekranga chiqaring
```python
for i in range(1,11,1):
   daraja = 2 ** i
   print(i, daraja)
```
```text
1 2
2 4
3 8
4 16
5 32
6 64
7 128
8 256
9 512
10 1024
```
14. 2,4,8,16,32,,,1024 sonlarini hosil qiling
```text
2
4
8
16
32
64
128
256
512
1024
```
15. 2,4,8,16 sonlarini hosil qiling
```text
2
4
8
16
```
16. 3,9,27 sonlarini hosil qiling. (3ni darajasi)
```text
3
9
27
```
17. 3ni darajasini hosil qiladigan dastur tuzing. Bu holda bosh va ohirgi darajani foydalanuvchi kiritsin
```text
Boshlang’ich chegarani kiriting: 1
Ohirgi chegarani kiriting: 5
3 ni 1-darajasi = 1
3 ni 2-darajasi = 8
3 ni 3-darajasi = 27
3 ni 4-darajasi = 64
3 ni 5-darajasi = 125
```
### Ro'yxat bilan ishlash
Ro’yxatni range bilan ekranga chiqaring. Berilgan 
```python
sonlar = [2,4,5,6,7]
for index in range(0, len(sonlar)):
  print(sonlar[index])
```
```text
2
4
5
6
7
```
18. Ro’yxatni range bilan teskari usulda ekranga chiqaring. 
sonlar = [2,4,5,6,7]
```text
7
6
5
4
2
```
19. Ikkita ro’yxatni range bilan ekranga chiqaring. 
- sonlar1 = [2,4,5,6,7]
- sonlar1 = [20,40,50,60,70]
```text
2, 20
4, 40
5, 50
6, 60
7, 70
```
20. Ro’yxatni qo’shish
- royxat1 = ["Me", "is", "Ota"]
- royxat2 = ["ning", "mim", "bek"]
```text
['Mening', 'ismim', 'Otabek']
```
21. royxat = [1,3,6,8,10] ro’yxatning har bir elementini kvadratga oshirish
```text
[1,9,36,64,100]
```
22. Ro’yxatni bir-biriga qo’shish
- royxat1 = ["Ismim", "Qaysi"]
- royxat2 = ["Otabek", "Bekzod"]
```text
['Ismim Otabek', 'Ismim Bekzod', 'Qaysi Otabek', 'Qaysi Bekzod']
```
23. Uzunligi bir hil bo’lgan ikki ro’yxatni birini tartib bo’yicha ikkinchisini teskari tartib bo’yisha chiqaring
- royxat1 = [10,20,30,40,50]
- royxat2 = [100,200,300,400,500]

```text
10 500
20 400
30 300
40 200
50 100
```
24. sonlar = [10,20,30,40,50] ro’yxat elementlari yig’indisini toping

```text
150
```
25. sonlar = [1,2,3,4,5] ro’yxat elementlari ko’paytmasini toping
```text
120
```
26. Foydalanuvchidan n sonini kiritishni so’rasin. Keyin n marta son kiritsin. Keyin usha sonlar yig’indisi va ko’paytmasini chiqarsin
```text
Nechta son kiritasiz: 3
1-sonni kiriting: 3
2-sonni kiriting: 3
3-sonni kiriting: 3
Yig'indi: 9	Ko'paytma: 27
```
27. Quyidagi ro’yxat berilgan sonlar = [2,3,4,5,6,5,7,3]. Qidiriladigan sonni foydalanuvchi kiritsin. So’ng usha son necha marta uchraydigan dastur tuzing
```text
Qidiriladigan sonni kiriting: 3 
3 raqami 2 marta qaytarilgan
```
28. Quyidagi ro’yxat berilgan sonlar = [2,3,4,5,6,5,7,3]. Yuqoridagi ro’yxatdan elementlari qaytarilmaydigan yangi ro’yxat hosil qiling
```text
Hosil bo'lgan yangi ro'yxat: [2, 3, 4, 5, 6, 7]
```
29. Quyidagi ro’yxatlar berilgan
- sonlar = [2,3,4,5,6,5,7,3]
- qidir_sonlar = [2,3,4,5,6,7]
- qidir_sonlar_summa = [0, 0, 0, 0, 0, 0, 0, 0]
<br>
Endi qidir_sonlar elementlari sonlar ro’yxatida  necha marta takrorlanishini hisoblaydigan dastur tuzing

```text
2 soni 1 marta takrorlangan
3 soni 2 marta takrorlangan
4 soni 1 marta takrorlangan
5 soni 2 marta takrorlangan
6 soni 1 marta takrorlangan
5 soni 2 marta takrorlangan
7 soni 1 marta takrorlangan
3 soni 2 marta takrorlangan
```
