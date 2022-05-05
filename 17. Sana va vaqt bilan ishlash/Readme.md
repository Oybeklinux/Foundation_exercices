# Mavzu 16: Sana va vaqt bilan ishlash
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqitucvhi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
timezone -
datetime
time
date

```
### 1.2 O'qish uchun materiallar
- sariq dev
  -[Kutubhonalar](https://python.sariq.dev/last-words/38-python-library) 
- w3schools
  - [Dates](https://www.w3schools.com/python/python_datetime.asp)

## 2. Amaliyot. O'qitucvhi
**Reja:**
- [2.1 Sana va vaqt haqida](#)
- [2.2. datetime.date](#)
- [2.3 datetime.time](#)
- [2.4 datetime.datetime](#)
- [2.5 datetime.timedelta](#)
- [2.6 timestamp](#)
- [2.7 timezone](#)

### 2.1 Sana va vaqt haqida
<ul>Sanalar bilan ishlash nega kerak? Masalan quyidagi holatlar ishlatiladi:
<li>Yangiliklarni chop etilgan sanasi bo'yicha ko'rish</li>
<li>Bir oyda sotilgan mahsulotlarni ko'rish</li>
<li>Har haftada nechta foydalanuvchilar ro'yxatdan o'tishi</li>
<li>Ishlab chiqilgan sanasi bo'yicha mahsulotlarni tartiblab chiqarish.</li>
<li>va hak.</li>
</ul>
<br>
<ul>
Sanalar bilan ishlaydigan modul datetime bo'lib, biz quyidagi sinf(class)lar bilan ishlasni ko'ramiz:
<li>1. datetime</li>
<li>2. date</li>
<li>3. time</li>
<li>4. timedelta</li>
<li>5. tzinfo</li>
<li>6. timezone</li>
</ul>

### 2.2. datetime.date

1. Ixtiyoriy sanaga ega bo'lgan datetime obyektini yarating
```python
from datetime import date

sana = date(2022, 2, 14)
print(sana)
```
```text
2022-02-14
```

Bu yerda date() funksiya emas, datetime moduliga kiruvchi sinf (class). Biz shu paytgacha ularni ma'lumot turlari deb o'qib keldik. Aslida esa ular <font color="red"> class </font>deb nomlanadi. Masalan int, list kabi ma'lumot turlari ham aslida class. Shu class ga tegishli bo'lgan o'zgaruvchi <font color="red"> obyekt</font> deyiladi. class va obyekt haqida to'liqloq boshqa mavzuda tanishamiz.<br>
2. Sanani quyidagi formatda chiqaring:
```python
from datetime import date

sana = date(2022, 2, 14)
print(f"Hozir {sana.year} yil {sana.month}-oy {sana.day}-kun")
print(f"Haftaning {sana.weekday() + 1}-kuni") 
# sana.weekday() + 1 = sana.isoweekday()
```
```text
Hozir 2022 yil 2-oy 14-kun
Haftaning 1-kuni
```

3. Sanani oyi o'zgartirilsin
```python
from datetime import date

sana = date(2022, 2, 14)
sana = sana.replace(month=10)
print(sana)
```
```text
2022-10-14
```

4. Sanani kuni, oyi,  va yil o'zgartirilsin
```python
from datetime import date

sana = date(2022, 2, 14)
sana = sana.replace(day=10, month=10, year=2020)
print(sana)
```
```text
2020-10-10
```
5. Ro'yxatda veb sahifa foydalnuvchilari haqida ma'lumotlar berilgan. Ulardan 1990 yilda tug'ilgan talabaning ismi va loginini ekranga chiqaring (filtrlash)
```python
from datetime import date
talabalar = [
    {
        "ismi": "Otabek",
        "tugilgan_sana": date(1990,4,5),
        "login": "otabek@gmail.com"
    },
    {
        "ismi": "Anvar",
        "tugilgan_sana": date(1991,4,15),
        "login": "anvar@gmail.com"
    },
    {
        "ismi": "Bekzod",
        "tugilgan_sana": date(1990,4,12),
        "login": "bekzod@gmail.com"
    },
    {
        "ismi": "Farida",
        "tugilgan_sana": date(1990,1,1),
        "login": "farida@gmail.com"
    }
]
yil = 1990
print(f"{yil} yilda tug'ilgan talabalar:")
for talaba in talabalar:
    if talaba["tugilgan_sana"].year == yil:
        print(talaba["ismi"], talaba["login"])
```

```text
1990 yilda tug'ilgan talabalar:
Otabek otabek@gmail.com
Bekzod bekzod@gmail.com
Farida farida@gmail.com
```
6. Dushanbada tug'ilgan talabalarning ismi va tug'ilgan sanalarini ekranga chiqaring. Sana quyidagi ** bo'lsin:
```text
Dushanbada tug'ilgan talabalar:
Anvar 15 April 1991
Farida 01 January 1990
```
```python
from datetime import date
talabalar = [
    {
        "ismi": "Otabek",
        "tugilgan_sana": date(1990,4,5),
        "login": "otabek@gmail.com"
    },
    {
        "ismi": "Anvar",
        "tugilgan_sana": date(1991,4,15),
        "login": "anvar@gmail.com"
    },
    {
        "ismi": "Bekzod",
        "tugilgan_sana": date(1990,4,12),
        "login": "bekzod@gmail.com"
    },
    {
        "ismi": "Farida",
        "tugilgan_sana": date(1990,1,1),
        "login": "farida@gmail.com"
    }
]
yil = 1990
print(f"Dushanbada tug'ilgan talabalar:")
for talaba in talabalar:
    sana = talaba["tugilgan_sana"]
    if sana.weekday() == 0:
        print(talaba["ismi"], sana.strftime("%d %B %Y"))
```
7. Yuqoridagi masalada bitta kamchilik bor, u boshqa tilida, endi natijani o'zbek tilida chiqaramiz:
```text
Dushanbada tug'ilgan talabalar:
Anvar 15 Aprel 1991
Farida 01 Yanvar 1990
```
```python
from datetime import date

import locale
locale.setlocale(locale.LC_TIME, 'uz_Uz.UTF-8')

talabalar = [
    {
        "ismi": "Otabek",
        "tugilgan_sana": date(1990,4,5),
        "login": "otabek@gmail.com"
    },
    {
        "ismi": "Anvar",
        "tugilgan_sana": date(1991,4,15),
        "login": "anvar@gmail.com"
    },
    {
        "ismi": "Bekzod",
        "tugilgan_sana": date(1990,4,12),
        "login": "bekzod@gmail.com"
    },
    {
        "ismi": "Farida",
        "tugilgan_sana": date(1990,1,1),
        "login": "farida@gmail.com"
    }
]
yil = 1990
print(f"Dushanbada tug'ilgan talabalar:")
for talaba in talabalar:
    sana = talaba["tugilgan_sana"]
    if sana.weekday() == 0:
        print(talaba["ismi"], sana.strftime("%d %B %Y"))
```

Quyida datetime.strftime() metodiga berish mumkin bo'lgan format berilgan:<br>
*Eslatma:*<br>
Locale ni o'zgartirish bilan natialar mos ravishda ozgaradi. Biz 'uz_Uz.UTF-8' uchun ko'rib ciqamiz:

<table>
<thead>
<tr>
    <td><strong>Format</strong></td>
	<td><strong>Ma'nosi</strong></td>
	<td><strong>Misol</strong></td>
</tr>
</thead>
<tbody>
<tr>
    <td><code>%a</code></td>
	<td>Hafta kunining qisqa nomi</td>
	<td>Dush,Sesh,...</td>
</tr>
<tr>
    <td><code>%A</code></td>
	<td>Hafta kunining to'liq nomi</td>
	<td>dushanba, seshanba, ...</td>
</tr>
<tr>
    <td><code>%w</code></td>
	<td>Hafta kunining tartib raqami</td>
	<td>0, 1, ..., 6</td>
</tr>
<tr>
    <td><code>%d</code></td>
	<td>Oyning kuni</td>
	<td>01, 02, ..., 31</td>
</tr>
<tr>
    <td><code>%b</code></td>
	<td>Oyning qisqa nomi</td>
	<td>Yan, Fev, ..., Dek</td>
</tr>
<tr>
    <td><code>%B</code></td>
	<td>Oyning to'liq nomi</td>
	<td>Yanvar, Fevral, ..., Dekabr</td>
</tr>
<tr>
    <td><code>%m</code></td>
	<td>Oyning tartib raqami. Qiymatlar: (0-11)</td>
	<td>20,21,22</td>
</tr>
<tr>
    <td><code>%y</code></td>
	<td>Ikki raqamdan iborat yil</td>
	<td>00, 01, ..., 99</td>
</tr>
<tr>
    <td><code>%Y</code></td>
	<td>To'rt raqamdan iborat yil</td>
	<td>2013, 2019 va hak.</td>
</tr>
<tr>
    <td><code>%H</code></td>
	<td>Soat. Qiymatlar: 0-23</td>
	<td>00, 01, ..., 23</td>
</tr>
<tr>
    <td><code>%I</code></td>
	<td>Soat. Qiymatlar: (1:12)</td>
	<td>01, 02, ..., 12</td>
</tr>
<tr>
    <td><code>%p</code></td>
	<td>Locale’s AM or PM.</td>
	<td>T, TO (inglizchada AM, PM)</td>
</tr>
<tr>
    <td><code>%M</code></td>
	<td>Daqiqa. Qiymatlar: (0-59)</td>
	<td>00, 01, ..., 59</td>
</tr>
<tr>
    <td><code>%S</code></td>
	<td>Second as a zero-padded decimal number.</td>
	<td>00, 01, ..., 59</td>
</tr>
<tr>
    <td><code>%f</code></td>
	<td>Mikrosoniya</td>
	<td>000000 - 999999</td>
</tr>
<tr>
    <td><code>%z</code></td>
	<td>+HHMM yoki -HHMM formatdagi UTC vaqt.</td>
	<td>&nbsp;</td>
</tr>
<tr>
    <td><code>%Z</code></td>
	<td>Vaqt hududit nomi</td>
	<td>&nbsp;</td>
</tr>
<tr>
    <td><code>%j</code></td>
	<td>Yildagi kun tartirbi</td>
	<td>001, 002, ..., 366</td>
</tr>
<tr>
    <td><code>%U</code></td>
	<td>Yildagi haftaning tartibi (Yakshanba haftaning 1-kun deb olinadi). All days in a new year preceding the first Sunday are considered to be in week 0.</td>
	<td>00, 01, ..., 53</td>
</tr>
<tr>
    <td><code>%W</code></td>
		<td>Yildagi haftaning tartibi (Dushanbda haftaning 1-kun deb olinadi). All days in a new year preceding the first Sunday are considered to be in week 0.</td>
	<td>00, 01, ..., 53</td>
</tr>
<tr>
    <td><code>%c</code></td>
	<td>locale formatiga mos sana va vaqtni korsatish.</td>
	<td>14/02/2020 13:30:04</td>
</tr>
<tr>
    <td><code>%x</code></td>
	<td>locale formatiga mos sana</td>
	<td>09/30/13</td>
</tr>
<tr>
    <td><code>%X</code></td>
	<td>locale formatiga mos vaqt</td>
	<td>07:06:05</td>
</tr>
<tr>
    <td><code>%%</code></td>
    <td>% belgisi.</td>
	<td>%</td>
</tr>
</tbody>
</table>

8. Bugungi sanani ekranga chiqaring
```python
from datetime import date
print(date.today())
```
```text

```
9. Quyidagi kodni ishlatib, tushunib oling:
```python
from datetime import date
import locale
locale.setlocale(locale.LC_TIME, 'uz_Uz.UTF-8')

sana = date(2020, 2, 14)
print(sana)
print(sana.strftime("""
Sana:
    %x (mahalliy format bo'yicha)
Hafta kuni:
    %a (qisqa nomi)
    %A (to'liq nom)
    %w (tartib raqami)
Oy kuni:
    %d (tartib raqami)
Oy:
    %b (qisqa nomi)
    %B (to'liq nomi)
    %m (tartib raqami)
Yil:
    %y (2 raqamli)
    %Y (4 raqamli)
"""))
```
```text
2020-02-14

Sana:
    14/02/2020 (mahalliy format bo'yicha)
Hafta kuni:
    Jum (qisqa nomi)
    juma (to'liq nom)
    5 (tartib raqami)
Oy kuni:
    14 (tartib raqami)
Oy:
    Fev (qisqa nomi)
    Fevral (to'liq nomi)
    02 (tartib raqami)
Yil:
    20 (2 raqamli)
    2020 (4 raqamli)
```
10. Sanani quyidagi formatda chiqaring:
```text
Sana: 2020 yil 14-Fevral juma, haftaning 5-kuni   
```
```python
from datetime import date
import locale
locale.setlocale(locale.LC_TIME, 'uz_Uz.UTF-8')

sana = date(2020, 2, 14)
print(sana.strftime("Sana: %Y yil %d-%B %A, haftaning %w-kuni"))
```
### 2.3 datetime.time
11. Vaqt qiymatini o'zlashtiring
```python
from datetime import time

vaqt = time(12, 40, 50, 200)
print(vaqt)
```
```text
12:40:50.002000
```
12. Vaqt qiymatini o'zlashtirib, quyidagi formatda chiqaring
```text
12:40:50 
```
```python
from datetime import time

vaqt = time(12, 40, 50)
# 1-usul
print(f"{vaqt.hour}:{vaqt.minute}:{vaqt.second}")
# 2-usul
print(vaqt.strftime("%H:%M:%S"))
# 3-usul
print(vaqt.isoformat())
# 4-usul
print(vaqt)
```
13. Satrni vaqtga o'girish
```python
from datetime import time

vaqt = time.fromisoformat("12:04:10")
print(vaqt.isoformat())
```
```text
12:04:10
```
*Eslatma:* strftime() metodi date, time va datetime uchun ishlatish mumkin, lekin time bilan ishlaganda strftime() metodiga kun, oy va yilni ko'rsatmaslik kerak. Aks holda xato bo'ladi, ya'ni kun, oy va yil o'rnida 1900 yil 1-yanvar qiymatlari bo'ladi.<br>
```python
from datetime import time

vaqt = time.fromisoformat("14:04:10")
print(vaqt.strftime("%c"))
```
```text
Mon Jan  1 14:04:10 1900
```
14. 15:30:20 vaqtni o'zlashtiring. Ekranga 03:30:20 PM ko'rinishida chiqaring:
```python
from datetime import time

vaqt = time.fromisoformat("15:30:20")
print(vaqt.strftime("%I:%M:%S %p"))
```
```text
02:04:10 PM
```
Natija mahalliy format turiga qarab farqlanishi mumkin<br>
15. Foydalanuvchidan ro'yxatdan o'tgan vaqtni %H:%M:%S formatida kiritishini so'rang, so'ng vaqtni ekranga chiqaring. "Daqiqani o'zgartirishni hohlaysizmi" deb so'rang. Agar 'ha' desa u kiritgan daqiqani almashtirib qo'ying:
```text
Ro'yxatdan qachon o'tdingiz (M: 12:04:05)? 16:04:04
Siz ro'yxatdan o'tgan vaqt 16:04:04
Yana o'zgartirmoqchimisiz (h/y)?h
Daqiqani kiriting: 40
Siz ro'yxatdan o'tgan vaqt 16:40:04
```
```python
from datetime import time

vaqt_str = input("Ro'yxatdan qachon o'tdingiz (M: 12:04:05)? ")
vaqt = time.fromisoformat(vaqt_str)
print(vaqt.strftime("Siz ro'yxatdan o'tgan vaqt %H:%M:%S"))
if input("Yana o'zgartirmoqchimisiz (h/y)?") == "h":
    daqiqa = int(input("Daqiqani kiriting: "))
    vaqt = vaqt.replace(minute=daqiqa)
    print(vaqt.strftime("Siz ro'yxatdan o'tgan vaqt %H:%M:%S"))
```
### datetime.datetime
datetime time va date qiymatlarini birlashtirgan holda ishlatish uchun mo'ljallangan, ya'ni unda ham sana ham vaqt bo'ladi<br>
16. Sana va qiymat o'zlashtirib, turli usullarda ekranga chiqarish
```python
from datetime import datetime
dt = datetime(2020, 5, 15, 12, 30, 40)
print(dt)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(f"{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}")
```
```text
2020-05-15 12:30:40
2020-05-15 12:30:40
2020-5-15 12:30:40
```
17. Hozirgi vaqt va sanani ekranga chiqarish
```python
from datetime import datetime
dt = datetime.now()
print(dt)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
```
```text
2022-02-14 17:48:07.269415
2022-02-14 17:46:23
```
18. Satrdan datetime ga o'girish:
```python
from datetime import datetime
dt = datetime.fromisoformat('2020-02-14T17:50:23')
print(dt)
```
```text
2020-02-14 17:50:23
```
### datetime.timedelta
timedelta ikki ikki vaqt (time, date va datetime) orasidagi farqni bilish uchun ishlatiladi<br>
19. O'qish boshlanishi va tugash sanasini belgilang, so'ng ular orasidagi farqni ekranga chiqaring. Ikki sana orasidagi farqni chiqarish kerak
```python
from datetime import date
sana1 = date(2020, 9, 1)
sana2 = date(2021, 6, 24)
farq = sana2 - sana1
print(type(farq))
print(f"Talabalar 1 yilda {farq.days} kun o'qishar ekan")
```
```text
<class 'datetime.timedelta'>
Talabalar 1 yilda 296 kun o'qishar ekan
```
Natijadan ko'rinib turibdiki, farq o'zgaruvchisi timedelta class iga tegishli <br>
20. Huddi shu masalani datetime bilan ko'rsak bo'ladi:
```python
from datetime import datetime
sana1 = datetime(2020, 9, 1, 12, 4, 4)
sana2 = datetime(2021, 6, 24, 13, 5, 6 )
farq = sana2 - sana1
print(type(farq))
print(f"Talabalar 1 yilda {farq.days} kun o'qishar ekan")
```
```text
<class 'datetime.timedelta'>
Talabalar 1 yilda 296 kun o'qishar ekan
```
21. Ikki bo'lib o'tgan voqealarni sana va soatlardagi farqini ekranga chiqaramiz:<br>
*Eslatma* <br>
timedelta class i time bilan ishlamaydi, shuning uchun biz datetime ni ishlatamiz, va yil, oy, kun ga bir hil qimyat berib qo'yamiz
```python
from datetime import datetime
voqea1 = datetime(2020, 9, 1, 12, 4, 4)
voqea2 = datetime(2021, 6, 24, 13, 5, 6 )
farq = voqea2 - voqea1
print(type(farq))
print(f"Ikki voqealar orasi  {farq.days} kunu  {farq.seconds//3600} soat ekan")
```
```text
<class 'datetime.timedelta'>
Ikki voqealar orasi  296 kunu  1 soat ekan
```
## Amaliyot. O'quvchi
1. 25.04.2022 sanaga ega bo'lgan datetime obyektini yarating. So'ng ekranga chiqaring

```text
2022-04-25
```
2. Bugungi sanani quyidagi formatda chiqaring:
```text
Hozir 2022 yil 5-oy 5-kun
Haftaning 5-kuni
```
3. Bugungi sanani va 2 oy keyingi sanani ekranga chiqaring:
<br>
Sizda ekranga chiqadigan usha kun sanasi bo'ladi. Ya'ni quyidagidan farqli bo'ladi
```text
Hozir 2022 yil 5-oy 5-kun
2 oydan keyin: 2022 yil 7-oy 5-kun
```
4. Bugungi sanani va 10 yil keyingi sanani ekranga chiqaring
```text
Hozir 2022 yil 5-oy 5-kun
10 yil keyin: 2032 yil 5-oy 5-kun
```
5. Ekranga aprel oyida tug'ilgan va elektron manzili mavjud bo'lgan talabalarni chiqaring:
```python
from datetime import date
talabalar = [
    {
        "ismi": "Otabek",
        "tugilgan_sana": date(1990,4,5),
        "login": "otabek@gmail.com"
    },
    {
        "ismi": "Anvar",
        "tugilgan_sana": date(1991,4,15),
        "login": None
    },
    {
        "ismi": "Bekzod",
        "tugilgan_sana": date(1990,4,12),
        "login": "bekzod@gmail.com"
    },
    {
        "ismi": "Farida",
        "tugilgan_sana": date(1990,1,1),
        "login": "farida@gmail.com"
    }
]
```

```text
Aprel oyida tug'ilgan va elektron manzili bor talabalar:
Otabek
Bekzod
```
6. Juma kuni nima rejalar bor,ekranga chiqaring:
```python
from datetime import date
reja = [
    {
        "nomi": "Toqqa chiqish",
        "sana": date(2022,5,5)
    },
    {
        "nomi": "To'yga borish",
        "sana": date(2022,5,6)
    },
    {
        "nomi": "Do'stlar bilan uchrashuv",
        "sana": date(2022,5,7)
    },
    {
        "nomi": "Qarindoshlarni ko'rishga borish",
        "sana": date(2022,5,13)
    }
]
```
```text
Dushanbada tug'ilgan talabalar:
Anvar 15 April 1991
Farida 01 January 1990
```
