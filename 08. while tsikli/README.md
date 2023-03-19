# 08. while tsikli

**Reja:**
<!-- TOC -->
 * [2.1 Sintaksis](#21-sintaksis)
 * [2.2 Cheksiz takrorlanish](#22-cheksiz-takrorlanish)
 * [2.3 break ifodasi](#23-break-ifodasi)
 * [2.4 continue ifodasi](#24-continue-ifodasi)
 * [2.5 while .. else](#25-while--else)
 * [Qo'shimcha misollar](#qoshimcha-misollar)
<!-- TOC -->

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
Misollar:
```python

# 1-misol
soni = 0
while soni < 3:
    soni = soni + 1
    print(soni, "- tsikl")


# 2-misol
hammasi = 0

son = int(input('Son kiriting: '))

# son musbat bo'lsa, davom et
while son > 0:
    hammasi += son
    son = int(input('Son kiriting: '))

print('Yig\'indi =', hammasi)

# 3-misol
soni = 0
while soni < 3: soni += 1; print(soni, "- tsikli"); print(soni, "- tsikli")

4-misol
sonlar = [1, 2, 3, 4]

while sonlar: # sonlar != []
    print(sonlar.pop(), sonlar)

# 5-misol
soz = "while operatori"

while soz: # sonlar != ""
    soz = soz[:-1]
    print(soz)

# 6-misol
hammasi = 0

son = int(input('Son kiriting: '))

while son: #son != 0
    hammasi += son
    son = int(input('Son kiriting: '))

print('Yig\'indi =', hammasi)

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

Misollar:
```python
# 1-misol
while True:
    print("Cheksiz takrorlanish")

# 2-misol
timer = 0
while 1: # 1 != 0
    print(timer)
    timer += 1

# 3-misol
sonlar = [2,3,4]
while [2,3,4]: # [2,3,4] != []
    print("sonlar")

# 4-misol
soni = 0
while soni <= 10:
    print("Cheksiz tsikl: soni =", soni)
    # soni o'zgaruvchisini oshirib bormayapmiz

# 5-misol
while True:
    tomoni = int(input("Kvadrat tomoni: "))
    print(f"Kvadrat yuzi:", tomoni ** 2)

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
Misollar:
```python
# 1-misol
i = 0
while i < 10:
    i += 1
    if i == 5 or i == 7:
        continue
    print(i)


# 2-misol
mevalar = ['olma', 'banan', 'nok', 'kivi', 'qulupnay']
while mevalar:
    meva = mevalar.pop()
    if meva in ['banan', 'kivi']:
        continue
    print(meva)

# 3-misol
i = 0
while i < 100:
    i += 1
    if i % 10 == 0:
        continue
    print(i)

# 4-misol
son = 100
while son:
    son -= 1
    if son % 2 == 1:
        continue
    print(son)
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
