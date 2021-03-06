# Mavzu 2: O'zgaruvchi, ma'lumot turlari, sonlar, boshqa turga o'girish
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
value         - qiymat: - 0,1,2, "abc", 'abc', 5.6, """Matn""",True, False
type          - qiymat (ma'lumot) turi: int, bool, str, float, list
cast          - qiymatni bir turdan ikkinchi turga o'girish: int("5") # 5
variable      - o'zgaruvchi: son, soz1, _gap, guruh, Alfavit
=             - o'zgaruvchini o'zgartirish, qiymat saqlash
keyword       - kalit so'z. Ular python tizimida ishlatiladi. Bu so'zlarni o'zgaruvchi nomiga qo'yib bo'lmaydi
```
### 1.2 O'qish uchun materiallar
- sariq dev
  - [#04 O'ZGARUVCHILAR](https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/04-variables)
  - [#05 STRING (MATN)](https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/05-string)
  - [#06 SONLAR](https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/06-sonlar)
- w3schools
  - [Variables](https://www.w3schools.com/python/python_variables.asp)
  - [Data Types](https://www.w3schools.com/python/python_datatypes.asp)
  - [Numbers](https://www.w3schools.com/python/python_numbers.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**

- [2.1 O'zgaruvchi](#21-ozgaruvchi)

### 2.1 O'zgaruvchi
#### 2.1.1 Turlicha ishlatilishi
```python
son = 5 # int
Son = 15 # int . Nomi yuqoridagi o'zgaruvchidan farq qiladi
sonlar = [1,2,3,4] # list
sonlar = (1,2,3,4) # tuple - o'zgarmas ro'yxat
sonlar = {1,2,3,4} # set
hayvonlar = ["echki", "fil", "kuchuk"] # list
hayvon = "echki" # str
oquvchi = "Olim" # str
hodim = {"ismi": "Otabek", 
        "familiyasi": "Anvarov", 
        "yoshi": 15} # dict
komanda1 = "Bunyodkor" # str
komanda2 = "Pahtakor" # str
sport = "futbol" # str
bormi = True # bool
tugadi = False # bool
a, b = 6, 7 # a=6, a=7
a, b = b, a # qiymatlar o'rnini almashtirish
a = b = 2 #a = 2, b = 2
```
---
O'zgaruvchi - harf, son va _ iborat bo'lgan, son bilan boshlanmaydigan ketma-ketlik. Qiymat saqlovchi
---
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
salom = "Assalom alaykum"
print(salom)
```
2. Ekranga foydalanuvchi kiritgan ism bilan salom berish kerak
```python
print("Assalomu alaykum " + input("Ismingiz: "))
```
```text
Ismingiz: Otabel
Assalomu alaykum Otabek
```
yoki
```python
ism = input("Ismingiz: ")
print("Assalomu alaykum " + ism)
```
```text
Ismingiz: Otabel
Assalomu alaykum Otabek
```
3. Bir nechta o'zgaruvchiga mos ravishda bir qiymatlar berish
```python
a, b = 4, 5 # a = 4, b = 5
print("a + b =", a + b) # a + b = 9
```
```text
9
```
4. Bir nechta o'zgaruvchiga bir hil qiymat berish
```python  
a = b = c = 10 # a = 10, b = 10, c = 10
b = 5
print(a + b + c) 
```
```text
25
```
5. O'zgaruvchilar qiymatlarini almashish
```python  
a = 10
b = 30
temp = a
a = b
b = temp
print("a = ", a, "\tb = ", b)
```
```text
a =  30     b =  10
```
6. To'rtburchak eni 10, bo'yi 20. Yuzasini toping
```python
eni = 10 
boyi = 20
print("To'rtburchak yuzi ", eni * boyi)

```
7. Ma'lumot turini bilish
```python
print(type(34))
print(type(34.4))
print(type("test"))
print(type([1,2,3]))
print(type((1,2,3,5)))
print(type({2,3,4}))
print(type({"ismi": "Otabek"}))
```
```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
```
8. Qiymatni turini o'zgartirish
```python
son = int("1")   # son = 1
son = int(2.8) # son = 2
son = int("3") # son = 3
son = int("3.4") # XATO
son = int("Otabek") # XATO
son = int(None) # XATO
son = int(True) # son = 1
son = int(False) # son = 0

son = float("1")   # son = 1.0
son = float(2.8) # son = 2.8
son = float("3.4") # son = 3.4
son = float("Otabek") # XATO
son = float(None) # XATO
son = float(True) # son = 1.0
son = float(False) # son = 0

satr = str(1)   # satr = "1"
satr = str(2.8) # satr = "2.8"
satr = str(True) # satr = "True"
satr = str(None) # satr = "None"
satr = str([2,3,4]) # satr = "[2, 3, 4]" 
satr = str({"ismi": "Otabek"}) # satr = "{'ismi': 'Otabek'}"
```
9. Foydalanuvchi kiritgan ikki sonni ko'paytirib, natijani ekranga chiqarish 
```python
son1 = input("1-sonni kiriting: ")
son2 = input("2-sonni kiriting: ")
print(son1, "*", son2, " = " , int(son1) * int(son2))
```
```text
1-sonni kiriting: 23
2-sonni kiriting: 2
23 * 2 = 46
```
yoki
```python
son1 = input("1-sonni kiriting: ")
son2 = input("2-sonni kiriting: ")
print(son1 + " * " + son2 + " = " + str(int(son1) * int(son2)))
```
10. Kvadratning perimetrini hisoblaydigan dastur yozing.
    <br>Formula: P = 4 * a 
    <br>a = 10. 
    <br>P - ?
```python
a = 10
p = 4 * a
print("Kvadrat perimetri: ", p)
```
## 3. Amaliyot. O'quvchi 
### Sintaksis
1. Ekranga quyidagini chiqaring. Qiymatni avval o'zgaruvchiga o'zlashtiring, keyin print ga usha o'zgaruvchini bering ([Yechim](1.%20Sintaksis/ozgaruvchi1.py))
```text
Men dasturchiman
```
2. 365 // 7 (Yilda hafta soni) natijasini ekranga chiqaring. Endi natijasini o'zgaruvchiga o'zlashtiring. O'zgaruvchiga ma'noli nom bering. M: hafta_soni. Izoh ham ishlating. M: "1 yilda hafta soni" ([Yechim](1.%20Sintaksis/ozgaruvchi2.py))
```text
52
```
3. 35 ni 8 bo'lib, qoldig'ni chiqaring. 35 va natijani o'zgaruvchi bilan bering. Ma'noli nom beramiz va izoh bilan kod yozamiz ([Yechim](1.%20Sintaksis/ozgaruvchi3.py))
```text
35 ni 8 bo'lganda 3 qoldiq qoladi
```
4. Foydalanuvchi kiritgan sonni 8 bo'lib, qoldig'ni chiqaring. Foydalanuvchi kiritgan sonni va natijani o'zgaruvchi bilan bering. Ma'noli nom beramiz va izoh bilan kod yozamiz ([Yechim](1.%20Sintaksis/ozgaruvchi4.py))
```text
Son kiriting: 40
40 ni 8 bo'lganda 0 qoldiq qoladi
```
5. 35 ni 8 bo'lib, butun qismini ekranga chiqaring.  35 va natijani o'zgaruvchi bilan bering. Ma'noli nom beramiz va izoh bilan kod yozamiz ([Yechim](1.%20Sintaksis/ozgaruvchi5.py))
```text    
35 ni 8 bo'lib butun qismini olsa 4 bo'ladi
```
6. Foydalanuvchi kiritgan sonni 8 bo'lib, butun qismini ekranga chiqaring.  Foydalanuvchi kiritgan son va natijani o'zgaruvchi bilan bering. Ma'noli nom beramiz va izoh bilan kod yozamiz(Bunda keyin har doim o'zgaruvchi bilan ishlaymiz va ma'noli nom beramiz. Bu jumla boshqa yozilmaydi) ([Yechim](1.%20Sintaksis/ozgaruvchi6.py))
```text    
Son kiriting: 45
45 ni 8 ga bo'lib butun qismini olsa 5 bo'ladi
```

7. a va b o'zgaruvchilarga qiymat bering. So'ng natijasini o'zgaruvchiga yozib, ekranga chiqaramiz. ([Yechim](1.%20Sintaksis/ozgaruvchi7.py))
```text
5 + 9 = 14
```
8. a va b o'zgaruvchilarga foydalanuvchi kiritgan sonlarni o'zlashtiring. So'ng natijasini o'zgaruvchiga yozib, ekranga chiqaramiz. ([Yechim](1.%20Sintaksis/ozgaruvchi8.py))
```text
Birinchi sonni kiriting: 10
Ikkinchi sonni kiriting: 20
10 + 20 = 30
```
9. Foydalanuvchi kiritgan ikki sonni ko'paytmasini chiqaradigan kod yozing. ([Yechim](1.%20Sintaksis/ozgaruvchi9.py))
```text
Birinchi sonni kiriting: 10
Ikkinchi sonni kiriting: 20
10 * 20 = 200
```
10. Kvadratning yuzasi *S* ni aniqlaydigan dastur yozing. Kvadratning tomoni *a* ga ixtiyoriy son bering. ([Yechim](1.%20Sintaksis/ozgaruvchi10.py)) 
S = <img src="https://latex.codecogs.com/svg.image?\inline&space;a^{2}" title="\inline a^{2}" />
```text
Kvadratning tomoni 5 bo'lganda, yuzi 25 ga teng bo'ladi
```
11. To'rtburchakning tomonlari *a* va *b* ni foydalnuvchi kiritsin. So'ng formula asosida to'rtburchakning yuzasi *S* va perimetri *P* aniqlansin. S = a * b va P = 2 * (a + b) ([Yechim](1.%20Sintaksis/ozgaruvchi11.py))
```text
a ni kiriting: 4
b ni kiriting: 5
S = 20
P = 18
```
### Mantiqiy
#### Oson daraja
12. Shar hajmini aniqlaydigan kod yozing.
<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\pi" title="\pi" /> o'zgarmas sondan iborat bo'lib, uni 3.14 deb olamiz, ya'ni pi=3.14. Radius R ni esa foydalanuvchi kiritsin. Shar hajmi formulasi: <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\inline&space;V=\frac{4}{3}\pi&space;R^{3}" title="\inline V=\frac{4}{3}\pi R^{3}" /> ([Yechim](2.%20Mantiqiy/ozgaruvchi12.py))
    
```text
Shar radiusini kiriting: 9
Sharning hajmi 3052.08
```
13. Hozir vaqt 14:00. 65 minutdan keyin u 15:05 bo'ladi. 70 minutdan keyin 15:10. Mana shuni dasturini yozing. Foydalanuvchi kiritgan minutdan keyin mazkur 14:00 ga nisbatan vaqtni chiqarsin. ([Yechim](2.%20Mantiqiy/ozgaruvchi13.py)) 
```text
Hozir soat 14:00
Minutni kiriting: 400
400 minutdan keyin vaqt 20:40 bo'ladi
```
14. Yuqoridagi dasturni universallashtiramiz. Endi mazkur vaqtni ham qo'shiladigan minutni ham foydalanuvchi kiritsin. ([Yechim](2.%20Mantiqiy/ozgaruvchi14.py)) 
```text
Hozirgi vaqt soatini kiriting: 13
Hozirgi vaqt minutini kiriting: 50
Qancha minutdan keyin vaqtni bilmoqchisiz? 30
30 minutdan keyin vaqt 14:20 bo'ladi
```
#### O'rta daraja
15. 10 qavatli bitta podyezddan iborat binoda 30 honadon bor. Foydalanuvchi kiritgan honadon raqamiga qarab uni nechanchi qavatda ekanligini chiqaring
Masalani yechishdan avval math.ceil bilan tanishib chiqing. ([Yechim](2.%20Mantiqiy/ozgaruvchi15.py)) 
```text
30 honadondan iborat 10 qavatli binoga hush kelibsiz
Honadon raqamini kiriting: 6
6-honadon 2-qavatda joylashgan
```
16. Yuqoridagi masalaga ozgina o'zgartirish qilamiz. Yana foydalanuvchi qavatni kiritadi dastur usha qavatda 3 honadon raqamlarini chiqarib berishi kerak. ([Yechim](2.%20Mantiqiy/ozgaruvchi16.py)) 
```text
30 honadondan iborat 10 qavatli binoga hush kelibsiz
Bino qavatini kiriting: 5
5-qavatda 13, 14 va 15-honadonlar joylashgan
```