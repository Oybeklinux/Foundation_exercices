# Mavzu 13: Lambda
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
```

### 1.2 O'qish uchun materiallar
- sariq dev
  - [#24 FUNKSIYALAR. SON'GSO'Z.](https://python.sariq.dev/function/24-lambda#lambda-yohud-nomsiz-funksiya)
- w3schools
  - [Lambda](https://www.w3schools.com/python/python_lambda.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Sintaksis](#21-sintaksis)
- [2.2 map funksiyasi](#22-map-funksiyasi)
- [2.3 filter funksiyasi](#23-filter-funksiyasi)


### 2.1 Sintaksis
lambda *bir necha argument* : *bitta ifoda*
<br><br>
Lambda funksiya bu nomsiz funksiya bo'lib, har qancha argument qabul qilishi mumkin, lekin ifoda bitta bo'ladi. Ya'ni qisqa kodli nomsiz funksiyadir
<br><br>
Lambda funksiya qachon kerak bo'ladi? O'zgaruvchan funksiya kerak bo'lganda.
<br>
*O'zgaruvchan funksiya* nima? Funksiya qiymat sifatida boshqa funksiyani qaytaradi. Natijani olish uhcun ikkinchi qaytgan funksiyani yana chaqirish kerak bo'ladi

```python
x = lambda a : a + 10
print(x(5))
```
```text
15
```
Bu yerda: 
1. x - funksiya nomi kabi ishlatiladi, lekin funksiya nomi emas, balki funksiyani o'zida saqlovchi o'zgaruvchidir
2. a - argumentdir
3. a + 10 - natijasi qaytarib yuboriladigan ifoda. Funksiyada natijani qaytarish uchun **return** ishlariladi. Lambda funksiyada esa return siz natija qaytariladi 
4. lambda - kalit so'z

### argument sifatida oddiy qiymat berish

1. Sonni ikkiga, uchga, to'rtga, beshga ko'paytiruvchi funksiya yozing:
```python
def kopaytir_2(son):
    return son * 2

def kopaytir_3(son):
    return son * 3

def kopaytir_4(son):
    return son * 4

def kopaytir_5(son):
    return son * 5

print(kopaytir_2(20))
print(kopaytir_3(20))
print(kopaytir_4(20))
print(kopaytir_5(20))
```
```text
40
60
80
100
```
Yuqoridagi beshta funksiyani masalani lambda yordamida bitta funksiya qilib yozsak bo'ladi:
```python
def kopaytir_n(n):
    # n - ko'paytiriladigan son. Yuqoridagi 1,2,3,4,5 qiymatlari o'rnida ishlatiladi  
    return lambda a: a * n

kopaytir_2 = kopaytir_n(2)
print(f" 5 * 2 = {kopaytir_2(5)}")
print(f" 15 * 2 = {kopaytir_2(15)}")
kopaytir_3 = kopaytir_n(3)
print(f" 5 * 3 = {kopaytir_3(5)}")
print(f" 15 * 3 = {kopaytir_3(15)}")
```
```text
 5 * 2 = 10
 15 * 2 = 30
 5 * 3 = 15
 15 * 3 = 45
```
Bu yerda kopaytir_n - o'zgaruvchan funksiya yoki funksiya hosil qilib beradigan funksiya. Hosil bo'lgan funksiyadan foydalanib qiymat olamiz. Bizning holatda kopaytir_n funksiyasi kopaytir_2 va kopaytir_3 funksiyalarini (aslida ular funksiya nomi emas funksiyani saqlovchi o'zgaruvchi deyiladi) hosil qildi. Hosil bo'lgan kopaytir_2 vazifasi sonni ikkiga ko'paytirish, kopaytir_3 vazifasi sonni uchga ko'paytirish. Shu usul bilan kopaytir_n dan kerakli funksiyalarni hosil qilsa bo'ladi

2. Kvadrat, to'rtburchak, uchburchak, aylana yuzasini topuvchi alohida funksiyalar yozing. So'ng ularni lambda yordamida bitta funksiyada jamlang:
```python
import math

def kvadrat_yuzi(a):
    return a ** 2

def tortburchak_yuzi(a, b):
    return a * b

def uchburchak_yuzi(asos, balandlik):
    return asos * balandlik

def aylana_yuzi(r):    
    return math.pi * r ** 2

print(f"Kvadrat yuzi: {kvadrat_yuzi(4)}")
print(f"To'rtburchak yuzi: {tortburchak_yuzi(4, 6)}")
print(f"Uchburchak yuzi: {uchburchak_yuzi(4, 10)}")
print(f"Aylana yuzi: {aylana_yuzi(7)}")
```
Lambda bilan
```python
from math import pi

KVADRAT = 1
TORTBURCHAK = 2
UCHBURCHAK = 3
AYLANA = 4

def yuzi(turi):
    if turi == KVADRAT:
        return lambda a: a ** 2
    elif turi == TORTBURCHAK:
        return lambda a, b: a * b
    elif turi == UCHBURCHAK:
        return lambda a, h: a * h
    elif turi == AYLANA:
        return lambda r: pi * r ** 2 

kvadrat_yuzi = yuzi(KVADRAT)
print(f"Kvadrat yuzi: {kvadrat_yuzi(4)}")
# Endi qisqa yozish yo'lini ko'ramiz
print(f"To'rtburchak yuzi: {yuzi(TORTBURCHAK)(4, 6)}")
print(f"Uchburchak yuzi: {yuzi(UCHBURCHAK)(4, 10)}")
print(f"Aylana yuzi: {yuzi(AYLANA)(7)}")
```
```text
Kvadrat yuzi: 16
To'rtburchak yuzi: 24
Uchburchak yuzi: 40
Aylana yuzi: 153.93804002589985
```
### argument sifatida lambda berish 
Biz aytdikki, funksiya funksiyani qaytarishi mumkin, huddi shunday funksiyaga argument sifatid boshqa funksiya berish mumkin. Aynan shu argument sifatida lambda funksiyalar ko'p qo'llaniladi:

3. Kvadrat, to'rtburchak, uchburchak, aylana yuzasini topuvchi funksiyada yozing. Ya'ni yuqoridagi masalani o'zi, shuni boshqacha usul bilan yechamiz:

```python
from math import pi

def yuzi(func):
     return func

kvadrat_yuzi = yuzi(lambda a: a ** 2)
print(f"Kvadrat yuzi: {kvadrat_yuzi(4)}")
# Endi qisqa yozish yo'lini ko'ramiz
print(f"To'rtburchak yuzi: {yuzi(lambda a, b: a * b)(4, 6)}")
print(f"Uchburchak yuzi: {yuzi(lambda a, h: a * h)(4, 10)}")
print(f"Aylana yuzi: {yuzi(lambda r: pi * r ** 2)(7)}")
```
```text
Kvadrat yuzi: 16
To'rtburchak yuzi: 24
Uchburchak yuzi: 40
Aylana yuzi: 153.93804002589985
```
4. Ikkita argument qabul qilib, qo'shish, ayirish, kopaytirish, bo'lish amallarini bajaradigan funksiya yozing:
```python
def amal(func):
    return func

natija = amal(lambda a, b: a + b)(10, 20)
print(f"Yig'indi: {natija}")
natija = amal(lambda a, b: a * b)(4, 5)
print(f"Ko'paytma: {natija}")
natija = amal(lambda a, b: a / b)(20, 5)
print(f"Bo'lish: {natija}")
natija = amal(lambda a, b: a - b)(4, 15)
print(f"Ayirma: {natija}")
```
```text
Yig'indi: 30
Ko'paytma: 20
Bo'lish: 4.0
Ayirma: -11
```
### argument sifatida lambda va ro'yxat berish
5. Ro'yxatni elementlarini yig'indisi yoki ko'paytmasini hisoblaydigan funksiya yozing:
```python
def jami(func, lst):
    summa = lst[0]
    for son in lst[1:]:
        summa = func(summa, son)
    return summa

sonlar = [1,2,3,4]
natija = jami(lambda a, b: a + b, sonlar)
print(f"Yig'indi: {natija}")
natija = jami(lambda a, b: a * b, sonlar)
print(f"Ko'paytma: {natija}")
```
```text
Yig'indi: 10
Ko'paytma: 24
```
Ro'yxatning sort() metodini bilamiz, u qiymatlarni tartiblab beradi. 
```python
print(sorted([3,4,15,6]))
```
Agar ro'yxatdagi element toifasi murakkab bo'lsachi:
```python
print(sorted([[5,6],[14,4],[3,15],[6,8]]))
```
```text
[[3, 15], [5, 6], [6, 8], [14, 4]]
```
Yana bir misol. Bizda meva va uning narxlari bor. Agar narxi bo'yicha tartiblamoqchi bo'lsak quyidagicha yozami:
```python
print(sorted({"olma":6000,"nok":14000,"banan":20000,"o'rik": 10000}.items()))
```
```text
[('banan', 20000), ('nok', 14000), ("o'rik", 10000), ('olma', 6000)]
```
Agar meva nomi bo'yicha tartiblamoqchi bo'lsak, qanday tartiblash kerakligini biz funksiya yordamida ko'rsatishimiz kerak bo'ladi
```python
def harf_tartibla(key): #tuple bo'ladi    
    return key[0]

mevalar = {"olma":16000,"nok":6000,"banan":20000,"o'rik": 10000}
print(sorted(mevalar.items(), key=harf_tartibla))
```
Lambda funksiya bilan
```python
mevalar = {"olma":16000,"nok":6000,"banan":20000,"o'rik": 10000}
print(sorted(mevalar.items(), key=lambda x: x[0]))
```
```text
[('banan', 20000), ('nok', 6000), ("o'rik", 10000), ('olma', 16000)]
```
6. Ro'yxatdagi elementlarni avval juftlarini so'ng toqlarini chiqarsin
```python
royxat = [13,4,15,16,7,18,19,10]
print(sorted(royxat, key=lambda x: x % 2 == 1))
```
7. Ro'yxatdagi elementlarni avval 10 ga qoldiqsiz bo'linadiganlarini  chiqarsin
```text
royxat = [13,4,150,16,7,18,190,10]
print(sorted(royxat, key=lambda x: x % 10 != 0 ))
```
```text
[150, 190, 10, 13, 4, 16, 7, 18]
```
8. [(20,40,10), (1,4,100), (40,80,6)] ro'yxatning har bir elementi 3 sondan iborat. 1, 2 va 3-son bo'yicha alohida tartiblab chiqaring
```python
royxat = [(20,40,10), (1,4,100), (40,80,6)]
print(f"1-son bo'yicha: {sorted(royxat, key=lambda a: a[0])}")
print(f"2-son bo'yicha: {sorted(royxat, key=lambda a: a[1])}")
print(f"3-son bo'yicha: {sorted(royxat, key=lambda a: a[2])}")
```
```text
1-son bo'yicha: [(1, 4, 100), (20, 40, 10), (40, 80, 6)]
2-son bo'yicha: [(1, 4, 100), (20, 40, 10), (40, 80, 6)]
3-son bo'yicha: [(40, 80, 6), (20, 40, 10), (1, 4, 100)]
```
9. [{'nomi': 'Nokia', 'model': 216, 'rang': 'Qora'}, {'nomi': 'Mi Max', 'model': '2', 'rang': 'Tilla'}, {'nomi': 'Samsung', 'model': 7, 'rang': 'Qizil'}]  ro'yxatini nomi, modeli va rangi bo'yicha tartiblang:
```python
royxat = [{'nomi': 'Nokia', 'model': 216, 'rang': 'Qora'}, {'nomi': 'Mi Max', 'model': '2', 'rang': 'Tilla'}, {'nomi': 'Samsung', 'model': 7, 'rang': 'Qizil'}]
print(f"Nomi bo'yicha: {sorted(royxat, key=lambda a: a['nomi'][0])}")
print(f"Modeli bo'yicha: {sorted(royxat, key=lambda a: int(a['model']))}")
print(f"Rangi bo'yicha: {sorted(royxat, key=lambda a: a['rang'])}")
```
```text
Nomi bo'yicha: [{'nomi': 'Mi Max', 'model': '2', 'rang': 'Tilla'}, {'nomi': 'Nokia', 'model': 216, 'rang': 'Qora'}, {'nomi': 'Samsung', 'model': 7, 'rang': 'Qizil'}]
Modeli bo'yicha: [{'nomi': 'Mi Max', 'model': '2', 'rang': 'Tilla'}, {'nomi': 'Samsung', 'model': 7, 'rang': 'Qizil'}, {'nomi': 'Nokia', 'model': 216, 'rang': 'Qora'}]
Rangi bo'yicha: [{'nomi': 'Samsung', 'model': 7, 'rang': 'Qizil'}, {'nomi': 'Nokia', 'model': 216, 'rang': 'Qora'}, {'nomi': 'Mi Max', 'model': '2', 'rang': 'Tilla'}]
```
### 2.2 map funksiyasi
Sintaksisi: map(funksiya, iterator)<br>

map() funksiyasi ikkita paramterni qabul qiladi:
- funksiya - a function that perform some action to each element of an iterable
- iterator - set, list, tuple kabi iteratorlar
qaytgan qiymat map classiga tegishli bo'lib, uni list(), set() ga o'girib natijani olamiz

10. Ro'yxatdagi har bir elementni kvadratga oshiring:

```python
def kvadrat(n):
    return n*n

sonlar = (1, 2, 3, 4)
natija = map(kvadrat, sonlar)
print(natija)

# map obyektini list ga o'girish
royxat = list(natija)
print(royxat)
```
yoki
```python
sonlar = (1, 2, 3, 4)
natija = map(lambda a: a*a, sonlar)
print(natija)

# map obyektini list ga o'girish
royxat = list(natija)
print(royxat)
```

```text
<map object at 0x000001C063900D90>
[1, 4, 9, 16]
```
11. map() funksiyasidan foydalanib [1,2,3,4,5] va [100,200,300,400,500] sonlarini mos elementlarini yig'indisidan hosil bo'lgan ro'yxatni ekranga chiqaring:

```python
royxat1 = [1,2,3,4,5]
royxat2 = [100,200,300,400,500]
natija = map(lambda a,b: a + b, royxat1, royxat2)
print(f"Natijaviy ro'yxat: {list(natija)}")
```
```text
Natijaviy ro'yxat: [101, 202, 303, 404, 505]
```

### 2.3 filter funksiyasi
Bu funksiya ham argument sifatida ro'yxat va boshqa funskiyani qabul qilib oladi va berilgan ro'yxat elementlarini berilgan funksiya yordamida saralaydi. Bunda argument sifatida uzatilgan funksiya mantiqiy qiymat qaytarishi kerak (True yoki False).

12. [1,2 ..., 30] ro'yxatdagi juft elementlaridan hosil bo'lgan ro'yxatni ekranga chiqaring:

```python
sonlar = range(1,31)
natija = filter(lambda a: a % 2 == 0, sonlar)
print(list(natija))
```
```text
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
```
13. filter funksiyasidan foydalanib ["Anvar", "Bekzod", "Ulug'bek", "Axmad"] ismlar ro'yxatidan bosh harfi "A" bo'lganlarigin ekranga chiqaring:
```python
ismlar = ["Anvar", "Bekzod", "Ulug'bek", "Axmad"]
natija = filter(lambda a: a[0].upper() == "A", ismlar)
print(list(natija))
```
```text
['Anvar', 'Axmad']
```
14. filter(), list(), lower() funksiyalaridan foydalanib berilgan matndan hamma undosh harlarni ekranga chiqaring
```python
matn = "Men mohir dasturchi bo'laman"
natija = filter(lambda a: a.lower() not in "euioa", list(matn))
print(list(natija))
```
```text
['M', 'n', ' ', 'm', 'h', 'r', ' ', 'd', 's', 't', 'r', 'c', 'h', ' ', 'b', "'", 'l', 'm', 'n']
```

## 3. Amaliyot. O'quvchi
1. Shunday lambda funksiya yozingki, u har qanday songa 100 ni qo'shib qaytarsin:
```text
45 -> 145
35 -> 135
```
2. 2,3,4,5 darajalarga oshiruvchi alohida funksiyalar yozing, so'ng lambda yordamida hammasini bitta funksiyaga jamlang:
```text
5 sonining 2 darajasi: 25
5 sonining 3 darajasi: 125
5 sonining 8 darajasi: 390625
```
3. Ikkita argument qabul qilib, qoldiqli bo'lish, darajaga oshirish, ildiz amallarini bajaradigan funksiya yozing:
```text
10 ni 3 ga qoldiqli bo'lganda: 1
4 ning 3 darajasi: 64
81 ning ildizi: 9
```
4. Har bir elementini kavdati, ikkilantirilgani, ildizini hisoblovchi funksiya yozing. Argument sifatida lambda va ro'yxat ishlating
```text
10 ning kvadrati: 100
4 ikkilangani: 8
81 ning ildizi: 9
```
5. Ro'yxatda elementlarini katta yoki kichik harflarga o'girib beradigan funksiya yozing. <br>
**Sharti:** Funskiyaga argument sifatida funksiya va ro'yxat berish kerak.
```text
['a', 'b', 'c'] ni katta harfga o'girganda ['A', 'B', 'C']
['Anvar', 'Alisher'] ni kichik harfga o'girganda ['anvar', 'alisher']
```

6. [18,24,7,16,36,11,190,10] ro'yxatdagi elementlarni avval 6 ga qoldiqsiz bo'linadiganlarini  chiqarsin
```text
[18,24,36,16,7,11,190,10]
```
7. [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] fanlarni bali bo'yicha tartiblab chiqarsin
```text
[('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]
```
8. [("Anvar", 180, 80), ("Bekzod", 190, 90), ("Jasur", 175, 75)] ro'yxatda ismi, bo'yi va og'irligi bo'yicha teskari tartiblab chiqaring:
```text
Ismi bo'yicha: [('Jasur', 175, 75), ('Bekzod', 190, 90), ('Anvar', 180, 80)]
Bo'yi bo'yicha: [('Bekzod', 190, 90), ('Anvar', 180, 80), ('Jasur', 175, 75)]
Og'irligi bo'yicha: [('Bekzod', 190, 90), ('Anvar', 180, 80), ('Jasur', 175, 75)]
```
9. Ro'yxatdagi har bir elementni map yordamida ildizini chiqaring:
```text
[4,9,16,25]
Ildizi: [2,3,4,5]
```
10. map() funksiyasidan foydalanib [2,3,4,5,6] va [10,12,13,14,15] sonlarini mos elementlarini ko'paytmasidan hosil bo'lgan ro'yxatni ekranga chiqaring:

```text
Natijaviy ro'yxat: [20, 36, 52, 70, 90]
```
11. map yordamida 3 ta ro'yxat elementlarini yig'indisidan hosil bo'lgan ro'yxatni ekranga chiqaring:
```text
1-ro'yxat: [1,2,3,4,5]
2-ro'yxat: [6,7,8,9,10]
3-ro'yxat: [3,4,5,6,7]
Yig'indi ro'yxat: [10,13,16,19,22]
```
12. map funksiyasidan foydalanib ["Anvar", "Bekzod", "Ulug'bek", "Axmad"] ismlarini hammasini katta harfda chiqaring
```text
["Anvar", "Bekzod", "Ulug'bek", "Axmad"]
Natija: 
['ANVAR', 'BEKZOD', "ULUG'BEK", 'AXMAD']
```
13. filter funksiyasidan foydalanib ["Anvar", "BEKZOD", "Ulug'bek", "AXMAD"] ismlar ro'yxatidan katta harflar bilan yozilganlarigina qoldiring:
```text
["Anvar", "BEKZOD", "Ulug'bek", "AXMAD"]
Natija: ["BEKZOD", "AXMAD"]
```
14. filter yordamida [12, -1, 9, 8, -0.5, -0.2, -100] ro'yxatidan faqat musbat sonlar qoldirilsin:
```text
[12, -1, 9, 8, -0.5, -0.2, -100]
Natija: [12, 9, 8]
```
15. Ro'yxatdan faqat toq sonlar qolsin:
```python
sonlar=[22, 100, 19, 13, 11, 1, 4, 66]
```
```text
Sonlar: [22, 100, 19, 13, 11, 1, 4, 66]
Toq sonlar: [19, 13, 11, 1]
```
16. filter(), list(), lower() funksiyalaridan foydalanib "unli harflar 5: euioa" matndan hamma unli va probel bo'lmagan harlarni ekranga chiqaring
```python
matn = "unli harflar 5: euioa"

```
```text
['n', 'l', 'h', 'r', 'f', 'l', 'r', '5', ':']
```
17. filter, list yordamida berilgan satrdan faqat sonlarni chiqarsin
```python
matn="2022 yilgi Qishki Olimpiya o'yinlari Xitoyning Pekin shahrida bo'lib o'tadi"

```
```text
['2', '0', '2', '2']
```
18. filter va map dan foydalanib berilgan roy'xatdan 8000 dan kichik bo'lgan sonlarga 2000 sonini qo'shing
```python
sonlar =[1000, 500, 600, 700, 5000, 90000, 17500]
sonlar = list(filter(lambda a: a < 8000, sonlar))
natija = map(lambda a: a+ 2000, sonlar)
print(list(natija))
```
```text
[3000, 2500, 2600, 2700, 7000]
```
19. Berilgan ro'yxat elementlari manfiy bo'lsa, musbatga o'girib, ikkiga bo'ling, manfiy bo'lsa, ikkiga ko'paytiring
```python
sonlar = [-1000, 500, -600, 700, 5000, -90000, -17500]
natija = map(lambda a: a/2*(-1) if a < 0 else a * 2, sonlar)
print(list(natija))
```
```text
[500.0, 1000, 300.0, 1400, 10000, 45000.0, 8750.0]
```
