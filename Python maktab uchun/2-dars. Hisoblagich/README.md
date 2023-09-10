# 02. O'zgaruvchi, ma'lumot turlari, sonlar, boshqa turga o'girish
 
**Reja:**
- [0 Terminlar](#0-terminlar)
- [1 O'zgaruvchi](#1-ozgaruvchi)
- [2 O'zgaruvchi nomlanishi](#2-ozgaruvchi-nomlanishi)
- [3 Ko'p qiymatlarni o'zlashtirish](#3-kop-qiymatlarni-ozlashtirish)
- [4 Ma'lumot turlari](#4-qiymat-turlari)
- [5 Ma'lumot turlarini o'zgartirish](#5-qiymat-turlarini-ozgartirish)


### Qayatirish uchun

#### Ta'riflar

| Nomi              | Ta'rifi                               | Masalan                                             |      
|-------------------|---------------------------------------|-----------------------------------------------------|
 | Qiymat            | Son, satr, True/False kabilar kiradi  | 5, 'Otabek', True, 10.5                             |
| O'zgaruvchi       | O'zida qiymatni saqlaydi              | a = 5<br/>ism = 'Otabek'                            |    
| O'zlashtirish     | Qiymatni o'zgaruvchiga yozish/saqlash | a = 10<br/>a o'zgaruvchiga 10 qiymat o'zlashtirildi |    


#### O'zgaruvchi nomlanishi

| O'zgaruvchi nomi | To'g'riligi                                                      |
|------------------|------------------------------------------------------------------|
| son_1            | To'g'ri                                                          |
| 1_son            | Xato. Son bilan boshlanishi mumkin emas                          |
| son$             | Xato. Son, harf va _ belgidan tashqari belgi kelishi mumkin emas |
| _son             | To'g'ri                                                          |

#### Ko'p qiymatlarni o'zlashtirish

| Ko'p qiymatlarni o'zlashtirish | Boshqacha yozilishi           |
|--------------------------------|-------------------------------|
| a, b = 10, 30                  | a = 10<br/>b = 30             |
| a,b,c = 10,20,30               | a = 10<br/>b = 20<br/> c = 30 |
| a = b = c = 40                 | a = 40<br/>b = 40<br/> c = 40 |

#### Ma'lumot turini bilish

|              |                 |
|--------------|-----------------|
| type(10)     | <class 'int'>   |
| type(30)     | <class 'int'>   |
| type(20.4)   | <class 'float'> |
| type('satr') | <class 'str'>   |


#### Ma'lumot turini o'zgartirish

| O'zgartirish | Xato                        | Natija | To'g'ri                          | Natija       |
|--------------|-----------------------------|--------|----------------------------------|--------------|
| Satrni songa | '23' * 2                    | XATO   | int('23') * 4                    | 46           |
|              | input('Son kiriting: ') * 3 | XATO   | int(input('Son kiriting: ')) * 3 | 15           |
| Sonni satrga | 'Yoshim' + 23 + ' da'       | XATO   | 'Yoshim' + str(23) + ' da'       | Yoshim 23 da |








### 0 Terminlar
```
qiymat                        - 0,1,2, "abc", 'abc', 5.6, """Ko'p qatorli satr""",True, False
ma'lumot turi                 - int, bool, str, float, list
ma'lumot turini o'zgartirish  - qiymatni bir turdan ikkinchi turga o'girish: int("5") # 5
o'zgaruvchi nomlanishi        - son, soz1, _gap, guruh, Alfavit
=                             - o'zgaruvchini o'zgartirish yoki qiymatni saqlash
kalit so'z                    - Ular python tizimida ishlatiladi. Bu so'zlarni o'zgaruvchi nomiga qo'yib bo'lmaydi
```

### 1 O'zgaruvchi

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

1. Ekranga 'Assalom alaykum' jumlasini ekranga chiqarish:

Natija: 

```text
Assalom alaykum
```

Yechim:

```python
print("Assalom alaykum")
```

Endi o'zgaruvchi bilan yozamiz

```python
salom = "Assalom alaykum"
print(salom)
```

2. Ekranga foydalanuvchi kiritgan ism bilan salom berib, yoshini so'rash kerak

Natija:


```text
Ismingiz: Otabek
Assalomu alaykum Otabek
Otabek yoshingiz nechada? 13
Sizning yoshingiz: 13
```

Yechim:

```python
ism = input("Ismingiz: ")
print("Assalomu alaykum " + ism)
yosh = input(ism + " yoshingiz nechada?")
print("Sizning yoshingiz: " + yosh)
```

3. To'rtburchak eni 14, bo'yi 20. To'rtburchak yuzini toping (S = a * b). Eni, bo'yi va yuzini o'zgaruvchilar bilan yozing

Natija:

```text
To'rtburchak yuzi:  280
```

Yechim:

```python
a = 14
b = 20
S = a * b
print("To'rtburchak yuzi: ", S)
```

### 2 O'zgaruvchi nomlanishi

O'zgaruvchi nomi son, harf va _ dan iborat bo'ladi va sondan boshlanmaydi

```
a = 2 # To'g'ri
a3 = 4 # To'g'ri
3e = 5 # XATO
e$ = 12 # XATO
_e = 15 # To'g'ri
```

O'zgaruvchiga ma'noli nom berish tavsiya etiladi

```python
eni = 10
boyi = 20
bolalar_soni = 20
oyinchilar_soni = 100
e = 10 # Tushunarsiz
b = 20 # Tushunarsiz
bs = 20 # Tushunarsiz
os = 100 # Tushunarsiz

```

4. Olmalar soni 100. Har bir o'quvchiga 13 tadan bersa, nechta ortib qoladi va nechta o'quvchi 13 ta olma oladi

Natija:

```text
7 ta o'quvchi olma oldi. 9 ta olma ortib qoldi
```

Yechim:

```python
olmalar_soni = 100
har_biri = 13
oquvchi_soni = olmalar_soni // har_biri
ortib_qogani = olmalar_soni % har_biri
print( oquvchi_soni, "ta o'quvchi olma oldi.", ortib_qogani, "ta olma ortib qoldi")

```

### 3 Ko'p qiymatlarni o'zlashtirish

Bir nechta o'zgaruvchiga mos ravishda bir nechta qiymatlar berish mumkin

5. a va b mos ravishda 114345 va 115765 ga teng. Ikkalasini yig'indisini chiqaring

Natija:

```text
a + b = 230110
```

Yechim:

```python
"""
a = 114_345
b = 115_765
o'rniga quyidagicha yozish mumkin
"""
a, b = 114_345, 115_765 
print("a + b =", a + b) 
```


6. Bir nechta o'zgaruvchiga bir hil qiymat berish

Natija:

```text
25
```

Yechim:

```python
"""
a = 10
b = 10
c = 10
o'rniga quyidagicha berish mumkin
"""
a = b = c = 10 # 
b = 5 # b = 5
print(a + b + c) # 10 + 5 + 10
```



7. O'zgaruvchilar qiymatlarini almashish

Natija:

```text
a =  30     b =  10
```

Yechim:

```python  
a = 10
b = 30
temp = a
a = b
b = temp
print("a = ", a, "\tb = ", b)
```

Yoki

```python  
a = 10
b = 30
a, b = b, a
print("a = ", a, "\tb = ", b)
```


8. To'rtburchak eni 10, bo'yi 20. Yuzasini toping

Natija:

```text
To'rtburchak yuzi  200
```

Yechim:

```python
eni = 10 
boyi = 20
print("To'rtburchak yuzi ", eni * boyi)
```

### 4 Ma'lumot turlari

9. Ma'lumot turini bilish

Natija:

```
34 					     <class 'int'>
34.4 					 <class 'float'>
test 					 <class 'str'>
[1, 2, 3] 				 <class 'list'>
(1, 2, 3, 5) 			 <class 'tuple'>
{2, 3, 4} 				 <class 'set'>
{'ismi': 'Otabek'} 		 <class 'dict'>
```

Yechim:


```python
print(34, "\t\t\t\t\t", type(34))
print(34.4, "\t\t\t\t\t", type(34.4))
print("test", "\t\t\t\t\t", type("test"))
print([1,2,3], "\t\t\t\t", type([1,2,3]))
print((1,2,3,5), "\t\t\t\t", type((1,2,3,5)))
print({2,3,4}, "\t\t\t\t", type({2,3,4}))
print({"ismi": "Otabek"}, "\t\t\t", type({"ismi": "Otabek"}))
```

### 5 Ma'lumot turlarini o'zgartirish


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

10. Foydalanuvchi kiritgan ikki sonni ko'paytirib, natijani ekranga chiqarish 

Natija:


```text
1-sonni kiriting: 23
2-sonni kiriting: 2
23 * 2 = 46
```

Yechim:


```python
son1 = input("1-sonni kiriting: ")
son2 = input("2-sonni kiriting: ")
print(son1, "*", son2, " = " , int(son1) * int(son2))
```

yoki

```python
son1 = input("1-sonni kiriting: ")
son2 = input("2-sonni kiriting: ")
print(son1 + " * " + son2 + " = " + str(int(son1) * int(son2)))
```

11. Tomonlari a=10 bo'lgan kvadratning perimetrini hisoblaydigan dastur yozing (P = 4 * a )

Natija:

```text
Kvadrat perimetri:  40
```

Yechim:

```python
a = 10
p = 4 * a
print("Kvadrat perimetri: ", p)
```

12. Endi kvadratning tomonini foydalnuvchi kiritsin, so'ng uni perimetrini hisoblasin

Natija:

```text
Kvadrat tomonini kiriting: 15
Kvadrat perimetri: 60
```

Yechim:

```python
a = input("Kvadrat tomonini kiriting: ")
p = 4 * int(a)
print("Kvadrat perimetri: ", p)
```
