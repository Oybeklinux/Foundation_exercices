# Mavzu 14: Class va obyekt
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
class - ya'ni klass bu huddi bino qurish uchun arxitektura chizmasi. Yoki tikuvchilar unga qarab kiyim tikadigan andoza kabidir 
object - andozaga qarab kiyim tikilganidek, class ga qarab konkret bir narsa yaratiladi, usha narsa obyekt deyiladi. Klass bu sxema, obyekt bu sxemaga qarab tuzilgan konkret narsa
method - ya'ni metod, bu huddi funksiya kabi ishlaydi, faqat bu funkisya ma'lum obyektga tegishli bo'ladi (M: ism.strip() - strip() metodi ism obyektiga tegishli)
property - ya'ni hususiyat, bu huddi o'zgaruvchi kabi ishlaydi, lekin bu o'zgaruvchi  ma'lum obyektga tegishli bo'ladi (M: ism.strip() - strip() metodi ism obyektiga tegishli)
```

### 1.2 O'qish uchun materiallar
- sariq dev
  - [OOP NIMA?](https://python.sariq.dev/oop/kirish)
  - [#28 KLASSLAR](https://python.sariq.dev/oop/28-klasslar)
  - [#29 OBYKETLAR BILAN ISHLASH](https://python.sariq.dev/oop/29-obyektlar-bilan-ishlash)
- w3schools
  - [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Klass yaratish](#21-sintaksis)

### 2.1 Klass yaratish
1. Eng qisqa koddan iborat Talaba nomli klass yarating:
```python
class Talaba:
    pass
```
2. Ismi, sharifi, yoshi kabi hususiyatlarga ega bo'lgan Talaba klassini yarating:
```python
class Talaba:
    ismi = None
    sharifi = None
    yoshi = None
```
yoki 
```python
class Talaba:
    
    def __init__(self):
        self.ismi = None
        self.sharifi = None
        self.yoshi = 30
```
yoki
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi
```
3. Talaba klassidan Anvar ismli obyekt yarating:
```python
class Talaba:
    ismi = None
    sharifi = None
    yoshi = None

anvar = Talaba()
print(anvar)
```
yoki
```python
class Talaba:
    
    def __init__(self):
        self.ismi = None
        self.sharifi = None
        self.yoshi = 30

anvar = Talaba()
print(anvar)
```
yoki
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi

anvar = Talaba("Anvar", "Otabekov", 30)
print(anvar)
```
```text
<__main__.Talaba object at 0x000002006E005540>
```
4. Talabaning hamma hususiyatlarini ekranga chiqaring:
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi

anvar = Talaba("Anvar", "Otabekov", 30)
print(anvar.ismi, anvar.sharifi, anvar.yoshi)
```
```text
Anvar Otabekov 30
```
5. Yuqoridagi masalani metod bilan amalga oshiring:
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)
        
anvar = Talaba("Anvar", "Otabekov", 30)
anvar.write()
```
```text
Anvar Otabekov 30
```
6. Talaba obyektini yaratgandan so'ng, uning yoshini 40ga o'zgartiring:
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)
        
anvar = Talaba("Anvar", "Otabekov", 30)
anvar.yoshi = 40
anvar.write()
```
```text
Anvar Otabekov 40
```
7. Yuqoridagi masalani metod bilan amalga oshiring:
```python
class Talaba:
    
    def __init__(self, ismi, sharifi,yoshi):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)
    
    def set_yoshi(self, yoshi):
        self.yoshi = yoshi   
        
anvar = Talaba("Anvar", "Otabekov", 30)
anvar.set_yoshi(40)
anvar.write()
```
```text
Anvar Otabekov 40
```
8. Yuqoridagi klassga tegishli hamma hususiyat va metodlarni ekranga chiqaring:
```python
class Talaba:
    
    def __init__(self):
        self.ismi = None
        self.sharifi = None
        self.yoshi = 30
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)
    
    def set_yoshi(self, yoshi):
        self.yoshi = yoshi   

talaba = Talaba()
print(dir(talaba))
```
9. Talabalar ro'yxatini yarating. So'ng Tsiklda hamma talabalar ismini ekranga chiqaring
```python
class Talaba:
    
    def __init__(self, ismi, sharifi="", yoshi=30):
        self.ismi = ismi
        self.sharifi = sharifi
        self.yoshi = yoshi
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)

talaba1 = Talaba("Anvar")
talaba2 = Talaba("Otabek")
talabalar = [talaba1, talaba2]

for talaba in talabalar:
    print(talaba.ismi)
```
```text
Anvar
Otabek
```
10. Talaba obyektini yarating. Obyekt orqali talabaning hamma hususiyatlarini ekranga chiqaring:
```python
class Talaba:
    
    def __init__(self):
        self.ismi = None
        self.sharifi = None
        self.yoshi = 30
    
    def write(self):
        print(self.ismi, self.sharifi, self.yoshi)
    
    def set_yoshi(self, yoshi):
        self.yoshi = yoshi   

talaba = Talaba()
# Sizning kod shu yerdan boshlanadi
```
```text
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ismi', 'set_yoshi', 'sharifi', 'write', 'yoshi']
```
11. Talaba klasiga dasturchiga uchun klass haqidagi ma'lumot (docstring) kiriting:
```python
class Talaba:
    """Talabani boshqarish uchun klass""" 
    def __init__(self):
        self.ismi = None
        self.sharifi = None
        self.yoshi = 30
```
12. Quyidagi rasmga qarab class tuzing:
<br>

![](images/salad.png)

<br>

```python
class Pitsa:

    def __init__(self, nomi, haqida, narxi, rasmi="default.png", turi="salat"):
        self.nomi = nomi
        self.haqida = haqida
        self.narxi = narxi
        self.rasmi = rasmi
        self.turi = turi
```
13. PitsaRestoran nomli class yarating. Unda quyidagi hususiyatlar bo'lsin:
- pitsalar - [Pitsa,Pitsa,...,] elementlardan iborat bo'ladi
- manzili
- telefon raqami 
```python
class Pitsa:

    def __init__(self, nomi, haqida, narxi, rasmi="default.png", turi="salat"):
        self.nomi = nomi
        self.haqida = haqida
        self.narxi = narxi
        self.rasmi = rasmi
        self.turi = turi

class PitsaMagazin:
    def __init__(self, nomi):
        self.hususiyat = []
        self.nomi = nomi
```
14. PitsaMagazin klassiga quyidagi metodlarni qo'shing:
- pitsa_add(Pitsa)
- pitsa_change(Pitsa)
- pitsa_delete(Pitsa)

## 3. Amaliyot. O'quvchi
1. Narxi, soni, nomi, muddati kabi hususiyatlarga ega bo'lgan Mahsulot klassini yarating
2. Modeli, narxi, kompaniyasi kabi hususiyatlarga ega bo'lgan Kompyuter klassini yozing
3. Manzili, nomi, ishga tushgan yili, hodimlar soni bor hususiyatlarga ega bo'lgan Tashkilot klassini yozing
4. Janri, kategoriyasi, ishlab chiqqan davlati, ishlab chiqqan yil, qisqacha ma'lumot kabi hususiyatlarga ega bo'lgan Multfilm klassini yozing
5. Mahsulot klassiga set_nom (nomini o'zgartiradigan), set_narx (narxini o'zgartiradigan), set_soni (sonini o'zgartiradigan) kabi metodlar yozing   
6. Tashkilot klassiga tegishli hamma ma'lumotlarni quyidagi ko'rinishida ekranga chiqaradigan metod qo'shing:
```text
Manzili: Shahrisabz ko'chasi
Nomi: IT Academy
Ishgan tushgan yil: 2020
Hodimlar soni: 15
```
7. Tashkilot obyektining foydalanuvchi tarafdan yozilgan hamma hususiyat vametodlarni ekranga chiqaring
8. Ikkita tashkilotlar ro'yxatini tuzing. So'ng tsiklda hamma tashkilotlar haqida ma'lumotni ekranga chiqaring
```text
== 1 ==
Manzili: Shahrisabz ko'chasi
Nomi: IT Academy
Ishgan tushgan yil: 2020
Hodimlar soni: 15
== 2 ==
Manzili: Amir Temur 18A
Nomi: TATU
Ishgan tushgan yil: 1956
Hodimlar soni: 7000
```