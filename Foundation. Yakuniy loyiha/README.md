
# Ikx nolik o'yini

**Stsenariy**

Sizning vazifangiz foydalanuvchi bilan **iks nolik** o'yinini o'ynaydigan oddiy dastur yozishdir. Siz uchun hamma narsani osonlashtirish uchun biz o'yinni soddalashtirishga qaror qildik. Mana bizning talablarimiz:

- kompyuter (ya'ni, sizning dasturingiz) o'yinni ```"X" ```yordamida o'ynashi kerak;
- foydalanuvchi (masalan, siz) o'yinni ```"O"``` dan foydalanib o'ynashingiz kerak;
- birinchi harakat kompyuterga tegishli - u har doim o'zining birinchi ```X``` belgisini doskaning o'rtasiga qo'yadi;
- barcha kvadratlar ```1``` dan boshlab satr bo'yicha raqamlangan (ma'lumot uchun quyidagi misolga qarang)
- foydalanuvchi o'zi tanlagan kvadrat raqamini kiritish orqali harakatini kiritadi - raqam haqiqiy bo'lishi kerak, ya'ni u butun son bo'lishi kerak, u ```0``` dan katta va ```10``` dan kichik bo'lishi kerak va u allaqachon kiritilgan maydonni ko'rsata olmaydi;
- dastur o'yin tugaganligini tekshiradi - to'rtta mumkin bo'lgan hukm bor: o'yin davom etishi kerak, o'yin durang bilan tugaydi, siz g'alaba qozonasiz yoki kompyuter g'alaba qozonadi;
- kompyuter o'z harakati bilan javob beradi va tekshirish takrorlanadi;
- sun'iy intellektning hech qanday shaklini qo'llamang - kompyuter tomonidan tasodifiy maydonni tanlash o'yin uchun yetarli.

Dastur bilan misol sessiyasi quyidagicha ko'rinishi mumkin:
```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Sizni galingiz: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Sizni galingiz: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Sizni galingiz: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Sizni galingiz: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Yutdingiz!
```

## Talablar

Quyidagi xususiyatlarni amalga oshiring:

- Quyidagi xususiyatlarni amalga oshiring:

Doska uch elementli ro'yxat sifatida saqlanishi kerak, har bir element esa boshqa uch elementli ro'yxat (ichki ro'yxatlar qatorlarni ifodalaydi), shunda barcha kvadratlarga quyidagi sintaksis yordamida kirish mumkin:

```text
doska[row][column]
```

- ichki ro'yxatning har bir elementida ```"O"```, ```"X"``` yoki kvadrat raqamini ifodalovchi raqam bo'lishi mumkin (bunday kvadrat bo'sh hisoblanadi)
- doska ko'rinishi misolda keltirilganidek bir xil bo'lishi kerak.
- quyida siz uchun belgilangan funksiyalarni amalga oshiring.

Tasodifiy butun sonni hosil qilish randrange() deb nomlangan Python funksiyasidan foydalanish orqali amalga oshirilish mumkin. Quyidagi dastur misolida undan qanday foydalanish ko'rsatilgan (dastur 0 dan 8 gacha bo'lgan o'nta tasodifiy sonni chop etadi).

_Eslatma_: ```from random import choice``` ko'rsatma random nomli tashqi modulidagi choice funksiyasini ko'rishini ta'minlaydi

```text
from random import choice
 
raqam = choice([1,2,3,4,5,6,7,8,9])
print(raqam)
```

Dastur strukturasi. Bu yordam uchun, agar hohlasangiz boshidan o'zingiz qiling

```python
from random import choice

def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param 
        None - hech narsa qaytarmaydi
    :return 
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    pass
    

def doskani_korsat(doska):
    """
    Doskani ekranga chiqaradi
    :param 
        doska
    :return
        None - hech narsa qaytarmaydi
    """
    pass

def foydalanuvchi_tanlasin(doska):
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """



def bosh_maydonlar(doska):
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi 
    :param 
        doska
    :return 
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    pass    
    
def golib_bormi(doska, belgi):
    """
    G'olib borligini aniqlaydi
    :param 
        doska
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """
    pass
 
    
def kompyuter_tanlasin(doska):
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    pass



while bosh_maydonlar:
    pass
```