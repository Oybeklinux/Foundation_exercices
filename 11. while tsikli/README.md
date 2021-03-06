# Mavzu 11: while tsikli
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
while - qaytarishlar uchun ishlatiladigan ifoda
break - for dan chiqish
continue - for da keyingi qadama o'tish
```
### 1.2 O'qish uchun materiallar
- sariq dev
  - [#17 WHILE TSIKLI](https://python.sariq.dev/while/17-while-loop)
  - [#18 WHILE, RO'YXATLAR VA LUG'ATLAR](https://python.sariq.dev/while/18-while-lists)
- w3schools
  - [While loops](https://www.w3schools.com/python/python_while_loops.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Sintaksis](#21-sintaksis)
- [2.2 Cheksiz takrorlanish](#22-cheksiz-takrorlanish)
- [2.3 break ifodasi](#23-break-ifodasi)
- [2.4 continue ifodasi](#24-continue-ifodasi)
- [2.5 while .. else](#26-while--else)


### 2.1 Sintaksis
while ifodasi toki shart bajarilar ekan takrorlanaveradi
```python
i = 10
while i > 0:
    print(i)
    i -= 1
```
```text
10
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
### 2.2 Cheksiz takrorlanish
Cheksiz takrorlanishdan ehtiyot bo'ling. Quyidagilar cheksiz takrorlanishlarga misol bo'ladi
- str. Agar bo'sh bo'lsa, False, aks holda True qaytadi
1. Kiritilgan so'zni ekranga harflar sonicha va har gal bitta harf kamaygan holda chiqaring.
```python
soz = input("So'z kiriting: ")
while soz: 
    print(soz)
```
```text
So'z kiriting: dastur
dastur
dastur
dastur
...
```
Yuqoridagi misol XATO<br>
Quyidagi esa TO'G'RI
```python
soz = input("So'z kiriting: ")
while soz: 
    print(soz)
    soz = soz[:len(soz)-1]
```
```text
So'z kiriting: dastur
dastur
dastu
dast
das
da
d
```
- int

2. Kiritilgan sonni kamayish tartibida ekranga chiqaring:
```python
son = int(input("Son kiriting: "))
while son:
    print(son-1)
```
```text
Son kiriting:  4
3
3
3
...
```
Yuqoridagi misol XATO<br>
Quyidagi esa TO'G'RI
```python
son = int(input("Son kiriting: "))
while son:    
    print(son)
    son -= 1
```
```text
Son kiriting: 3
3
2
1
```
- bool
3. Toki foydalanuvchi menyuni to'g'ri yozmagunicha takrorlanaversin:
```python
while True:
    menu = int(input("""Bittasini tanlang:
    1. Olma
    2. Nok
    3. Banan
"""))
    print("Menyu tanlandi")
```
```text
Bittasini tanlang:
    1. Olma
    2. Nok
    3. Banan
4
Menyu tanlandi
Bittasini tanlang:
    1. Olma
    2. Nok
    3. Banan
2
...
```
Yuqoridagi misol XATO<br>
Quyidagi esa TO'G'RI

```python
while True:
    menu = int(input("""Bittasini tanlang:
    1. Olma
    2. Nok
    3. Banan
"""))
    print("Menyu tanlandi")
    if menu in [1,4]:
        break
    else:
        print("Xato qayto tering")
```
```text
Bittasini tanlang:
    1. Olma
    2. Nok
    3. Banan
1
Menyu tanlandi
```

### 2.3 break ifodasi
break - takrorlanishdan chiqish uchun ishlatiladi

4. son=0 berilgan. Har gal *son*ga 5ni qo'shib, ekranga chiqaring. Takrorlanish 20 gacha davom etsin:
```python
son = 0 
while True:
    print(son)
    son += 5
    if son > 20:
        break
```
```text
0
5
10
15
20
```
   
### 2.4 continue ifodasi
5. son = 99 berilgan. *son*dan har gal 18ni ayirib, 45 va 27 dan tashaqari hammasini ekranga chiqaring
```python
son = 99
while son - 18 > 0:
    son -= 18
    if son == 45 or son == 27:
        continue
    print(son)
```
```text
81
63
9
```

### 2.5 while .. else
Qachonki shart bajarilmasa, ya'ni takrorlanishdan chiqib ketganda else bloki ishga tushadi
6. 1-5 oraliqdagi sonlarni ekranga chiqaring:
```python
son = 1
while son <= 5:
    print(son)
    son += 1
else:
    print("Takrorlanish tugadi")
```
```text
1
2
3
4
5
Takrorlanish tugadi
```
break bilan while takrorlanish blokidan chiqib ketsa, else bloki ishga tushmaydi:
7. 1-100 oraliqda hamma sonlarni ekranga chiqaring, agar son juft va 5 ga qoldiqsiz bo'linsa, u holda takrorlanishdan chiqib ketsin:
```python
son = 1
while son < 100:
    if son % 2 == 0 and son % 5 == 0:
        break
    print(son)
    son += 1
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
7
8
9
```
### Qo'shimcha misollar
8. Foydalanuvchi kiritgan satrni hamma belgilarini alohida qatorda chiqaring:
```python
satr = input("Biron yozuv kiriting: ")
i = 0
while i < len(satr):
    print(satr[i])
    i += 1
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
9. 1 dan 10 gacha sonlarni hosil qiling
```python
son = 1
while son <= 10:
    print(son)
    son += 1
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
10. 9,8,7,6,5,4,3,2,1 sonlarini hosil qiling
```python
son = 9
while son > 0:
    print(son)
    son -= 1
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
11. 15,25,35,45,55 sonlarini hosil qiling
```python
son = 15
while son <= 55:
    print(son)
    son += 10
```
```text
15
25
35
45
55
```
12. 15,25,35,45,55, … ohiri sonlarini hosil qiling. *ohiri* sonini foydalanuvchi kiritsin
```python
son = 15
oxiri = int(input("Chegarani kiriting: "))
while son <= oxiri:
    print(son)
    son += 10
```
```text
15
25
35
45
55
```
13. 1 dan 10 gacha sonlarni yig’indisini ekranga chiqaring
```python
son = 1
yigindi = 0
while son <= 10:
    yigindi += son
    son += 1
print(f"Yig'indi: {yigindi}")
```
```text
Yig'indi: 55
```
14. 2,4,6,8,10 sonlarini ko’paytmasini va yig’indisini ekranga chiqaring
```text
Sonlar yig'indisi: 30
Sonlar ko'paytmasi: 3840
```
```python
summa = 0
kopaytma = 1
son = 2
qadam = 2
ohiri = 10
while son <= ohiri:
   
   summa = summa + son
   kopaytma = kopaytma * son
   son += qadam
print(f"Sonlar yig'indisi: {summa}")
print(f"Sonlar ko'paytmasi: {kopaytma}")
```

## 3. Amaliyot. O'quvchi
1. 1,3,5,7,9 sonlarini hosil qiling:
```text
1
3
5
7
9
```
2. 2,4,6,8,10 sonlarini hosil qiling: 
```text
2
4
6
8
10
```
3. 10,20,30,40,50 sonlarini hosil qiling:
```text
10
20
30
40
50
```
4. 10,8,6,4,2,0 sonlarini hosil qiling:
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
Sonlar ko’paytmasi: 3840
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
i = 1
ohiri = 11
qadam = 1
while i < ohiri:
    daraja = 2 ** i
    print(i, daraja)
    i += qadam
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
14. 2,4,8,16,32,...,1024 sonlarini hosil qiling
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
3 ni 1-darajasi = 3
3 ni 2-darajasi = 9
3 ni 3-darajasi = 27
3 ni 4-darajasi = 81
3 ni 5-darajasi = 243
```
18. A = 90 va B = 25 kesma berilgan. A soni B sonidan katta. A kesmada B kesmadan nechta joylashtirish mumkin. Ko'paytirish va bo'lish amalisiz toping:
```text
A kesma: 90
B kesma: 25
A kesmada B kesmadan 3 ta joylashadi
```
19. A = 90 va B = 25 kesma berilgan. A soni B sonidan katta. A kesmada B kesmadan maksimal joylashtirilganda qancha bo'sh joy qolib ketadi. Ko'paytirish va bo'lish amalisiz toping:
```text
A kesma: 90
B kesma: 25
A kesmada B kesmadan to'liq joylashtirilganda 15 kesma joy qolib ketadi
```
20. a va b qiymatni foydalanuvchi kiritsin. a ni b ga bo'lganda qancha qiymat chiqadi, a ni b ga bo'lganda qancha qoldiq chiqadi. Ko'paytirish va bo'lish amalisiz toping:
```text
a sonini kiriting: 80
a sonini kiriting: 30
a / b = 2
a % b = 20
```
21. Kiritilgan son 3 ning darajasi yoki darajasi emasligini toping. Ko'paytirish va bo'lish amalisiz toping
```text
Son kiriting: 9
3 ning darajasi
```
```text
Son kiriting: 12
3 ning darajasi emas
```
22. 2 sonining darajasini aniqlovchi dastur yozing:
```text
2 ning darajasi bo'lgan son kiriting: 16
Natija:
2^4=16
```
```text
2 ning darajasi bo'lgan son kiriting: 32
Natija:
2^5=16
```

23. sonlar = [2,4,5,6,7] ro’yxatni ekranga chiqaring.  
```text
2
4
5
6
7
```
24. Ro’yxatni teskari usulda ekranga chiqaring. 
sonlar = [2,4,5,6,7]
```text
7
6
5
4
2
```
25. Ikkita ro’yxatni ekranga chiqaring. 
- sonlar1 = [2,4,5,6,7]
- sonlar1 = [20,40,50,60,70]
```text
2, 20
4, 40
5, 50
6, 60
7, 70
```
26. Ro’yxatni qo’shish
- royxat1 = ["Me", "is", "Ota"]
- royxat2 = ["ning", "mim", "bek"]
```text
['Mening', 'ismim', 'Otabek']
```
27. royxat = [1,3,6,8,10] ro’yxatning har bir elementini kvadratga oshirish
```text
[1,9,36,64,100]
```
28. Uzunligi bir hil bo’lgan ikki ro’yxatni birini tartib bo’yicha ikkinchisini teskari tartib bo’yisha chiqaring
- royxat1 = [10,20,30,40,50]
- royxat2 = [100,200,300,400,500]
```text
10 500
20 400
30 300
40 200
50 100
```
29. sonlar = [10,20,30,40,50] ro’yxat elementlari yig’indisini toping
```text
150
```
30. sonlar = [1,2,3,4,5] ro’yxat elementlari ko’paytmasini toping
```text
120
```
