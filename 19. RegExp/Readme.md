# Mavzu 19: RegExp - Andoza asosida satrlar bilan ishlash
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqitucvhi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
regexp -

```
### 1.2 O'qish uchun materiallar
- sariq dev
  -[Kutubhonalar](https://python.sariq.dev/extras/regex) 
- w3schools
  - [RegEx](https://www.w3schools.com/python/python_regex.asp)

## 2. Amaliyot. O'qitucvhi
**Reja:**
- [2.1 Kirish]
- [2.2 Maxsus belgilar](#)
- [2.3 Metabelgilar](#)
- [2.4 To'plam](#)
- [2.5 Funksiyalar](#)
  - [2.5.1 search](#)
  - [2.5.2 split](#)
  - [2.5.3 sub](#)
  - [2.5.4 findall](#)


### 2.1 Kirish
RegEx yoki Regular Expression andoza asosida matn ichidan biron satrni qidirish uchun ishlatiladi. Masalan quyidagilar bo'lishi mumkin:
- matn ichidan telefon raqamlarni qisirish
- matn ichidan sanalarni qidirish
- matn ichidan sarlavhalarni qidirish

RexEx dan foydalnish uchun re kutubhonasini import qilib olamiz
```python
import re
```
re kutubhonasida bir qancha funksiyalar bor. Hozir biz shulardan search funksiyasi yordamida RegEx andoza qoidalarini o'rganamiz

1. Matnni telefon raqamiga tekshiramiz

```python
import re

matn = "971234567"
andoza = "\d{9}"
natija = re.search(andoza, matn)
print(natija)
```
Bu misolda biz matnni raqamga tekshiryapmiz. <br>
Bu yerda:
- **\d** - ixtiyoriy raqamni bildiradi
- {9} - raqamlar 9 tadan iborat bo'lishi kerak, kam ham emas, ko'p ham emasligini tekshiradi

```text
<re.Match object; span=(0, 9), match='971234567'>
```
Agar matn andozaga mos bo'lsa, search funkisyasidan *Match* obyekti qaytadi, mos bo'lmasa None qaytadi

2. Quyidagi misolda sanani 23-04-22 formatda yozilganligida tekshiramiz
```python
import re

matn = "23-aprel"
andoza = "\d{2}-\d{2}-\d{2}"
natija = re.search(andoza, matn)
print(natija)
```
Natija
```python
None
```
Natija **None** qaytdi, chunki sana 23-04-22 formatda yozilmagan. Andozada esa shu format ko'rsatilgan, ya'ni bu yerda: <br>
- \d{2} - ikkita sonni bildiradi
- '-' belgisi '-' ni bildiradi xolos

Mana endi RegEx andozasi qoidalari bilan tanishib, misol ko'rib chiqamiz

### 2.2 Maxsus belgilar
<table>
<thead>
<tr>
    <th>Belgi</th>
	<th>Ta'rifi</th>
	<th>Misol</th>
</tr>
</thead>
<tbody>
<tr>
    <td><code>\A</code></td>
	<td>O'zidan keyingi belgilarni matn boshida ekanligiga tekshiradi</td>
	<td>3-misol</td>
</tr>
<tr>
    <td><code>\b</code></td>
	<td>O'zidan keyingi belgilarni so'z boshida ekanligiga tekshiradi</td>
	<td>4-misol</td>
</tr>
<tr>
    <td><code>\B</code></td>
	<td>O'zidan keyingi belgilarni so'z boshida emasligiga tekshiradi</td>
	<td>5-misol</td>
</tr>
<tr>
    <td><code>\d</code></td>
	<td>son ekanligiga tekshiradi</td>
	<td>5-misol</td>
</tr>
<tr>
    <td><code>\D</code></td>
	<td>son emasligiga tekshiradi</td>
	<td>6-misol</td>
</tr>
<tr>
    <td><code>\s</code></td>
	<td>bo'sh joy ekanligiga tekshiradi</td>
	<td>7-misol</td>
</tr>
<tr>
    <td><code>\S</code></td>
	<td>bo'sh joy emasligiga tekshiradi</td>
	<td></td>
</tr>
<tr>
    <td><code>\w</code></td>
	<td>so'z belgilariga (ya'ni harf, son va _ belgisi) tekshiradi </td>
	<td>8-misol</td>
</tr>
<tr>
    <td><code>\W</code></td>
	<td>so'z belgilari emasligiga tekshiradi</td>
	<td>9-misol</td>
</tr>
<tr>
    <td><code>\Z</code></td>
	<td>O'zidan keyingi belgilarni matn ohirida ekanligiga tekshiradi</td>
	<td>10-misol</td>
</tr>
</tbody>
</table>

3. Shunday dastur tuzinki, foydaluvchi kiritgan telefon raqam boshi 998 bo'lsa, 'To'g'ri aks holda 'Xato' deb ekrancha chiqarsin
```python
import re
matn = input("Telefon raqamingizni kiriting (Raqam 998 dan boshlansin)\n: ")
andoza = "\A998\d{9}"
natija = re.search(andoza, matn)
print("To'g'ri") if natija else print('Xato')
```
```text
Telefon raqamingizni kiriting (Raqam 998 dan boshlansin):
998974251234
To'g'ri
```
```text
Telefon raqamingizni kiriting (Raqam 998 dan boshlansin):
990974251234
Xato
```

4. Matndan 3-tor ko'cha, 5-tor ko'cha va hak. kabi so'zni topsin
```python
import re
matn = "Bizning manzil Hondamir 3-tor ko'cha"
andoza = r"\b\d{1,2}-tor"
natija = re.search(andoza, matn)
print(natija)
```
Bu yerda: <br>
- r'' - '\' belgisi bilan keladigan maxsus belgilarni python satr deb qabul qilishi uchun *str* dan avval **r** qo'yiladi. Aks holda biz ko'rsatgan andoza buzilib ketadi
- \b\d raqam so'z boshida ekanini tekshiradi

5. Matnda ichida yoki ohirida raqam uchragan so'z borligini aniqlang. Bor bo'lsa topildi, aks holda bunday so'z mavjud emas degan habar chiqsin 
```python
import re
matn = "O'zgaruvchi3 nomi _, harf va raqamdan iborat bo'lishi kerak3"
andoza = r"\d\B"
natija = re.findall(andoza, matn)
print(natija)
```
```text
<re.Match object; span=(131, 132), match='2'>
```
6. Matndan son emaslarni aratib olish: 

```python
import re

matn = 'Bizning maktab Yunusobod 9-dahada joylashgan'
andoza = r'\D+'
print(re.findall(andoza, matn))
```
```text
['Bizning maktab Yunusobod ', '-dahada joylashgan']
```
7. Quyidagi matndagi so'zlar ro'yxatini hosil qiling
```python
import re

matn = '''Ismim Otabek
Yoshim 20
Kasbim dasturchi'''
andoza = r'\s+'
print(re.split(andoza, matn, re.M))
```
Natija:
```text
['Ismim', 'Otabek', 'Yoshim', '20', 'Kasbim', 'dasturchi']
```
8. Ro'yxatdagi hamma o'zgaruvchilar ekranga chiqaring
```python
import re
vars = ['player_1','rt%65', 'groups_', 'r%te']
andoza = '\A\w+\Z'
ozgaruvchilar = []
for var in vars:
    natija = re.search(andoza, var)
    
    if natija:
        ozgaruvchilar.append(var)

print(ozgaruvchilar)
```
Natija
```text
['player_1', 'groups_']
```
9. Ro'yxatda nomlarida xato belgi ishlatilgan o'zgaruvchilarni  chiqaring
```python
import re
vars = ['player_1','rt%65', 'groups_', 'r%te']
andoza = '\W+'
ozgaruvchilar = []
for var in vars:
    natija = re.search(andoza, var)
    
    if natija:
        ozgaruvchilar.append(var)

print(ozgaruvchilar)
```
Natija
```text
['player_1', 'groups_']
```
10. Ro'yxatda nomlarining ohirida raqam yozilgan o'zgaruvchilarni  chiqaring
```python
import re
vars = ['player_1','rt%65', 'groups_', 'r%te']
andoza = '\A\w+\d\Z'
ozgaruvchilar = []
for var in vars:
    natija = re.search(andoza, var)
    
    if natija:
        ozgaruvchilar.append(var)

print(ozgaruvchilar)
```
Natija
```text
['player_1']
```
### 2.3 Metabelgilar 

## Amaliyot. O'quvchi
