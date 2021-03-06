# Mavzu 4: bool(mantiqiy). bool  bilan ishlash
 
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
- w3schools
  - [Mantiqiy](https://www.w3schools.com/python/python_booleans.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 True/False qiymatlari haqida](#21-truefalse-qiymatlari-haqida)
- [2.2 Sonlarni solishtirish](#22-sonlarni-solishtirish) 
  - [2.2.1 Sonlarni katta, kichik va tenglikka tekshirish](#221-sonlarni-katta-kichik-va-tenglikka-tekshirish)
  - [2.2.2 Sonlarni musbat/manfiylikka tekshirish](#222-sonlarni-musbatmanfiylikka-tekshirish)
  - [2.2.3 Sonlarni juft/toqlikka tekshirish](#223-sonlarni-jufttoqlikka-tekshirish)
  - [2.2.4 Sonlarni karralikka tekshirish](#224-sonlarni-karralikka-tekshirish)
- [2.3 Satrni solishtirish](#23-satrni-solishtirish)
  - [2.3.1 Tenglikka tekshirish](#231-tenglikka-tekshirish)
  - [2.3.2 Tarkibida borligini tekshirish](#232-tarkibida-borligini-tekshirish)
- [2.4 To'plam bilan solishtirish](#24-toplam-bilan-solishtirish)
- [2.5 Qiymatlarning True/False bo'lishi](#25-qiymatlarning-truefalse-bolishi)
- [2.6 Murakkab solishtirish: and/or](#26-murakkab-solishtirish-andor)
- [2.7 Operatorlar](#27-operatorlar)
  - [2.7.1 Arifmetik operatorlar](#271-arifmetik-operatorlar)
  - [2.7.2 O'zlashtirish operatorlar](#272-ozlashtirish-operatorlar)
  - [2.7.3 Tarkibida borligini bildiruvchi operatorlar](#273-Tarkibida-borligini-bildiruvchi-operatorlar)
  - [2.7.4 Taqqoslash operatori](#274-taqqoslash-operatori)
### 2.1 True/False qiymatlari haqida
Mantiqiy qiymat - shartni tekshirish natijasi bo'lib, u ikki qiymatdan iborat:<br>
True - shart to'g'ri <br>
False - shart xato<br><br>
Mantiqiy qiymatlar *if* ifodasida ishlatiladi. Ya'ni shart True bo'lsa, tegishli amal bajariladi, aks holda boshqa amal bajariladi. 
![alt text](images/if_condition.jpg)
<br>Shuningdek va *while* ifodasida ham ishlatiladi. Ya'ni shart True bo'lsa, while blokidagi amallar takroriy bajarilaveradi.   
![alt text](images/while-loop.jpg)
<br>Hozircha shartni qanday yozishni o'rganamiz.  Keyingi mavzularda *if* va *while* da shartlarni qanday ishlatishni ko'ramiz.<br>
Shartlarda turli belgilar ishlatilishi mumkin. Ular bilan [2.7.4 Taqqoslash operatorlari](#274-taqqoslash-operatori) mavzusiga o'tib tanishib chiqing, so'ng yana shu yerdan davom ettiring.
### 2.2 Sonlarni solishtirish
#### 2.2.1 Sonlarni katta, kichik va tenglikka tekshirish
1. 5 son 15 sonidan **kattami** solishtiring, so'ng javobini ekranga chiqaring:
```python
print(5 > 15)
```
```text
False
```
5 soni 15 dan katta emas, shuning uchun ifoda natijasi False - xato bo'ladi<br>
2. 5 soni 15 sonidan **kichikmi** solishtiring, so'ng javobini ekranga chiqaring:
```python
print(5 < 15)
```
```text
True
```
5 soni 15 dan kichik, shuning uchun ifoda natijasi True - to'g'ri bo'ladi<br>
3. 20 soni 200 ga **tengmi**, solishtiring, so'ng javobini ekranga chiqaring:
```python
print(20 == 200)
```
*Eslatma:*<br>
= - o'zlashtirish belgisi, lekin == tenglikka tekshirish belgisidir.<br>
4. 100 soni 100.4 ga **teng emasligini** tekshiring
```python
print(100 != 100.4)
```
```text
True
```
5. 18 soni 9 dan **katta yoki tengmi** tekshiring
```python
print(18 >= 9)
```
```text
True
```
Ya'ni ikki shartga tekshiradi: katta yoki tenglikka. Ikkalasidan bittasi bajarilsa True bo'ladi<br>
6. 18 soni 9 dan **kichik yoki tengmi** tekshiring
```python
print(18 <= 9)
```
```text
False
```
7. Foydalanuvchi ikki son kiritsin. Birinchi son ikkinchi sondan kattami tekshiring.
```python
print("Birinchi son ikkinchi sondan kattami?")
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
print(son1 > son2)
```
```text
Birinchi son ikkinchi sondan kattami?
Birinchi sonni kiriting: 10
Ikkinchi sonni kiriting: 15
False
```
```text
Birinchi son ikkinchi sondan kattami?
Birinchi sonni kiriting: 20
Ikkinchi sonni kiriting: 5
True
```

#### 2.2.2 Sonlarni musbat/manfiylikka tekshirish
![Musbat manfiy](images/positiv_and_negativ.png)
<br>8. Foydalanuvchi kiritgan son musbatmi, tekshiring.
```python
son = input("Son kiriting: ")
print(son > 0)
```
```text
Son kiriting: 10
True
```
```text
Son kiriting: -10
False
```
9. Foydalanuvchi kiritgan son manfiymi, tekshiring.
```python
son = input("Son kiriting: ")
print(son < 0)
```
```text
Son kiriting: 10
False
```
```text
Son kiriting: -10
True
```
10. Foydalanuvchi kiritgan son musbat yoki 0 ga tengmi, tekshiring.
```python
son = input("Son kiriting: ")
print(son >= 0)
```
```text
Son kiriting: 0
True
```
```text
Son kiriting: 10
True
```
```text
Son kiriting: -10
False
```
#### 2.2.3 Sonlarni juft/toqlikka tekshirish

11. Foydalanuvchi kiritgan son juftmi, tekshiring.
<br>*Eslatma:* Sonni juft ekanligini tekshirish uchun sonni 2 ga bo'lib, qoldig'i 0 ga tengligini tekshirish kerak
```python
son = input("Son kiriting: ")
print(son % 2 == 0)
```
12. Foydalanuvchi kiritgan son juft emasmi (ya'ni toqmi) , tekshiring.
<br>*Eslatma:* Sonni toq ekanligini tekshirish uchun sonni 2 ga bo'lib, qoldig'i 1 ga tengligini tekshirish kerak. Yoki uni o'rniga juft emaslikka tekshiramiz. Ikkala shart yozilishi har hil bo'lgani bilan ma'nosi bir hil.
```python
son = input("Son kiriting: ")
print(son % 2 != 0)
```
yoki
```python
son = input("Son kiriting: ")
print(son % 2 == 1)
```
```text
Son kiriting: 13
True
```
```text
Son kiriting: 14
False
```
#### 2.2.4 Sonlarni karralikka tekshirish
<br>*Eslatma:* s sonnni b songa karrali ekanligini tekshirish uchun  a sonni b songa bo'lib, qoldig'ini 0 ga tengligini tekshiramiz 

13. Foydalanuvchi kiritgan son 3 ga karralimi (ya'ni 3 ga bo'lganda qoldig'i 0 ga tengmi), tekshiring.
```python
son = input("Son kiriting: ")
print(son % 3 == 0)
```
```text
Son kiriting: 10
False
```
```text
Son kiriting: 12
True
```
14. Foydalanuvchi kiritgan son 15 ga karrali emasmi, tekshiring. Ya'ni 15 ga karrali emasligini tekshirish kerak
```python
son = input("Son kiriting: ")
print(son % 15 != 0)
```
```text
Son kiriting: 30
False
```
```text
Son kiriting: 35
True
```
### 2.3 Satrni solishtirish
#### 2.3.1 Tenglikka tekshirish
15. Foydalanuvchi kiritgan harf 'a' harf ekanligini tekshiring.
```python
harf = input("Harf kiriting: ")
print(harf == 'a')
```
```text
Harf kiriting: b
False
```
```text
Harf kiriting: A
False
```
```text
Harf kiriting: a
True
```
16. Foydalanuvchi kiritgan harf 'A' harf ekanligini tekshiring.
```python
harf = input("Harf kiriting: ")
print(harf == 'A')
```
```text
Harf kiriting: b
False
```
```text
Harf kiriting: A
True
```
```text
Harf kiriting: a
False
```
17. Foydalanuvchi kiritgan harf katta yoki kichik ekanligidan qa'iy nazar 'a' harfga tekshiring. Ya'ni 'a' yoki 'A' holatida ham True bo'lsin.
```python
harf = input("Harf kiriting: ")
print(harf.lower() == 'a')
```
yoki
```python
harf = input("Harf kiriting: ")
print(harf.upper() == 'A')
```
```text
Harf kiriting: a
True
```
```text
Harf kiriting: A
True
```
```text
Harf kiriting: b
False
```
18. Foydalanuvchi kiritgan so'z 'login' so'zi bilan bir hilmi tekshiring.
```python
soz = input("So'z kiriting: ")
print(soz == 'login')
```
```text
So'z kiriting: login
True
```
```text
So'z kiriting: abc
False
```
#### 2.3.2 Tarkibida borligini tekshirish
19. Foydalanuvchi kiritgan so'z boshqa satr(gap,so'z) ichida mavjudmi tekshiring.
```python
gap = "Men zo'r dasturhciman"
soz = input("So'z kiriting: ")
print(soz in gap)
```
```text
So'z kiriting: dasturchi
True
```
```text
So'z kiriting: haydovchi
False
```
20. Foydalanuvchi kiritgan harf so'zda mavjudmi tekshiring.
```python
hayvon_nomi = "buzoq"
print("Hayvon nomi: *****")
satr = input("Ekranda berkitilgan hayvon nomida qanday harf bor. \nBitta harf toki harflar ketma-ketligini kiriting: ")
print(satr in hayvon_nomi)
```
```text
Hayvon nomi: *****
Ekranda berkitilgan hayvon nomida qanday harf bor. 
Bitta harf toki harflar ketma-ketligini kiriting: b 
True
```
```text
Hayvon nomi: *****
Ekranda berkitilgan hayvon nomida qanday harf bor. 
Bitta harf toki harflar ketma-ketligini kiriting: h 
False
```
### 2.4 To'plam bilan solishtirish
21. Foydalnuvchi kiritgan son ro'yxatda borligini tekshiring
```python
sonlar = [2,3,4,5,6,7]
son = int(input("Ro'yxatda qanday son bor? "))
print(son in sonlar)
```
```text
Ro'yxatda qanday son bor? 10
False
```
```text
Ro'yxatda qanday son bor? 5
True
```
22. Foydalanuvchi kiritga meva nomi bozorda borligini tekshiring.
<br>*Eslatma:* Huddi shunda tuple, dict va set ma'lumot turlariga ham **in** yordamida element mavjudligini tekshirish mumkin 
```python
bozor = ['olma', 'nok', 'anor']
meva = input("Meva nomini kiriting: ")
print(meva in bozor)
```
```text
Meva nomini kiriting: banan
False
```
```text
Meva nomini kiriting: anor
True
```
23. Lug'atda kiritilgan o'zbekcha so'z borligini tekshring:
```python
lugat = {
    "car": "moshina",
    "run": "yugurmoq",
    "cat": "mushuk"
}
uz = input("Lug'atimizda qaysi o'zbekcha so'z borligini bilmoqchisiz? ")
print(uz in lugat.values())
```
```text
Lug'atimizda qaysi o'zbekcha so'z borligini bilmoqchisiz? mushuk
True
```
```text
Lug'atimizda qaysi o'zbekcha so'z borligini bilmoqchisiz? kuchuk
False
```
24. Lug'atda kiritilgan inglizcha  so'z borligini tekshring:
```python
lugat = {
    "car": "moshina",
    "run": "yugurmoq",
    "cat": "mushuk"
}
uz = input("Lug'atimizda qaysi inglizcha so'z borligini bilmoqchisiz? ")
print(uz in lugat.keys())
```
```text
Lug'atimizda qaysi o'zbekcha so'z borligini bilmoqchisiz? cat
True
```
```text
Lug'atimizda qaysi o'zbekcha so'z borligini bilmoqchisiz? rat
False
```
25. To'plamda element borligini tekshirish:
```python
foydalanuvchi_idlari = {1,2,3,4,5,6}
user_id = input("Foydalanuvchi idsini kiriting: ")
print(user_id in foydalanuvchi_idlari)
```
```text
Foydalanuvchi idsini kiriting: 3
True
```
```text
Foydalanuvchi idsini kiriting: 13
False
```
26. O'zgarmas to'plamda element borligini tekshirish:
```python
mashina_ranglari = ("oq", "qizil", "ko'p", "qora")
rang = input("Qanday mashina ranglari borligini bilish uchun rang kiriting: ")
print(rang in mashina_ranglari)
```
```text
Qanday mashina ranglari borligini bilish uchun rang kiriting: oq
True
```
```text
Qanday mashina ranglari borligini bilish uchun rang kiriting: kul rang
False
```
27. O'zgarmas to'plamda element yo'qligini tekshirish:
```python
mashina_ranglari = ("oq", "qizil", "ko'p", "qora")
rang = input("Qanday mashina ranglari yo'qligini bilish uchun rang kiriting: ")
print(rang not in mashina_ranglari)
```
```text
Qanday mashina ranglari yo'qligini bilish uchun rang kiriting: oq
False
```
```text
Qanday mashina ranglari yo'qligini bilish uchun rang kiriting: kul rang
True
```

### 2.5 Qiymatlarning True/False bo'lishi
bool() funksiyasi qiymatlarning True yoki False ekanligini aniqlab beradi:
```python
print(bool("Hello"))
print(bool(15))
```
```text
True
True
```
*Qoida:*<br>
**True** bo'ladi agar:
1. Son 0 ga teng bo'lmasa
2. Satr bo'sh bo'lmasa
3. To'plam (dict, list, set, tuple) bo'sh bo'lmasa
```python
print(bool("soz"))
print(bool(123))
print(bool(["olma", "anor", "banan"]))
```
```text
True
True
True
```
**False** bo'ladi agar:
1. Son 0 ga teng bo'lsa
2. Satr bo'sh bo'lsa
3. To'plam bo'sh bo'lsa
```python
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
```
```text
False
False
False
False
False
False
False
```
28. Foydalanuvchi kiritgan satrni bo'shligini tekshiring:
```python
soz = input("Agar bo'sh so'z kiritsangiz False yozuvini, aks holda True yozuvini ko'rasiz: ")
print(bool(soz))
```
```text
Agar bo'sh so'z kiritsangiz False yozuvini, aks holda True yozuvini ko'rasiz: 
False
```
```text
Agar bo'sh so'z kiritsangiz False yozuvini, aks holda True yozuvini ko'rasiz: abs 
True
```
29. Obyekt butun son ekanligini tekshiring:
```python
x = 400
print(isinstance(x, int))
```
```text
True
```
Boshqa holat:
```python
x = 400
del x
print(isinstance(x, int))
```
```text
False
```
### 2.6 Murakkab solishtirish: and/or
*Eslatma:*<br>
**and** - bir vaqtda bajarilish kerakligini bildiradi, ya'ni ikkala shart True bo'lsa, natijasi ham True bo'ladi<br>
**or** - ikkalasidan birontasi bajarilsa kifoya qiladi, ya'ni ikkala shartdan kamida bittasi True bo'lsa, umumiy natijasi ham True bo'ladi<br>
**not** - shartni teskarisiga tekshirish

30. Kiritilgan yosh 20 va 30 orasida ekanligini tekshiring:
```python
yosh = int(input("Yoshingizni kiriting: "))
print(yosh > 20 and yosh < 30)
```
yoki soddoroq usuli bilan yozadigan bo'lsak
```python
yosh = int(input("Yoshingizni kiriting: "))
print(20 < yosh < 30)
```
```text
Yoshingizni kiriting: 25
True
```
```text
Yoshingizni kiriting: 15
False
```
31. Son ham 3ga ham 5 karralik bo'lishini tekshiring:
```python
son = input("Son kiriting: ")
print(son % 3 == 0 and son % 5 == 0)
```
```text
Son kiriting: 15
True
```
```text
Son kiriting: 9
False
```
32. Kiritilgan qiymat son bo'lsin va u son 1,2,3,4,5 orasida ekanligini tekshiring:
```python
son = input("Son kiriting: ")
print(son.isdigit() and int(son) in [1,2,3,4,5])
```
```text
Son kiriting: 3
True
```
```text
Son kiriting: 13
False
```
```text
Son kiriting: bir
False
```
33. Bola pasport olishi uchun uni 16 yoshga teng yoki undan katta ekanligiga va bir paytda O'zbekistonda yashashligiga tekshiring:
```python
yosh = input("Pasport olish uchun yoshingizni kiriting: ")
davlat = input("Hozir qayerda yashaysiz: ")
print(int(yosh) >= 16 and davlat == "O'zbekiston")
```
```text
Pasport olish uchun yoshingizni kiriting: 13
Hozir qayerda yashaysiz: O'zbekiston
False
```
```text
Pasport olish uchun yoshingizni kiriting: 16
Hozir qayerda yashaysiz: O'zbekiston
True
```
```text
Pasport olish uchun yoshingizni kiriting: 17
Hozir qayerda yashaysiz: abs
False
```
34. Biz qidiruv tizimidan foydalanmoqchimiz. Bizga mahsulot nomi kitob va narxi 40 000 yuqori bo'lgan yoki  mahsulot nomi telefon va narxi 400 000 dan yuqori bo'lgan tovarlar kerak. Shu hartni yozing. Mahsulot va narxni foydalanuvchidan so'rang. So'ng shartga tekshiring:
```python
mahsulot = input("Mahsulot nomi: ") 
narx = input("Narxi: ")
print(mahsulot == "kitob" and narx > 10_000) or mahsulot == "telefon" and narx > 400_000)
```
```text
Mahsulot nomi: kitob
Narxi: 5000
False
```
```text
Mahsulot nomi: kitob
Narxi: 15000
True
```
```text
Mahsulot nomi: telefon
Narxi: 15000
False
```
```text
Mahsulot nomi: telefon
Narxi: 500000
True
```
35. Kiritilgan yosh 20 va 30 orasida emasligiga tekshiring:
```python
yosh = int(input("Yoshingizni kiriting: "))
print(not (yosh > 20 and yosh < 30))
```
yoki soddoroq usuli bilan yozadigan bo'lsak
```python
yosh = int(input("Yoshingizni kiriting: "))
print(not 20 < yosh < 30)
```
```text
Yoshingizni kiriting: 25
False
```
```text
Yoshingizni kiriting: 15
True
```
### 2.7 Operatorlar
#### 2.7.1 Arifmetik operatorlar
Arifmetik operatorlar oddiy matematik amallarni bajarish uchun ishlatiladi:
<table>
<tr><td>Operator</td><td>Nomi</td><td>Misol</td><td>Javobi</td></tr>
<tr><td>+</td><td>Qo'shish</td><td>3 + 6</td><td>9</td></tr>
<tr><td>-</td><td>Ayirish</td><td>3 - 6</td><td>-3</td></tr>
<tr><td>*</td><td>Kko'paytirish</td><td>3 * 6</td><td>18</td></tr>
<tr><td>/</td><td>Bo'lish</td><td>6/3</td><td>2.0</td></tr>
<tr><td>%</td><td>Qoldiq olish</td><td>7 % 4</td><td>3</td></tr>
<tr><td>**</td><td>Darajaga oshirish</td><td>7 * 2</td><td>49</td></tr>
<tr><td>//</td><td>Bo'lib butun qismini olish</td><td>9 // 4</td><td>2</td></tr>
</table>

36. To'rtburchak yuzini hisoblaydigan dastur yozing:
```python
a = input("To'rtburchakning tomoni a = ")
b = input("To'rtburchakning tomoni b = ")
print("To'rtburchakning yuzi ", a * b)
```
```text
To'rtburchakning tomoni a = 3
To'rtburchakning tomoni b = 7
To'rtburchakning yuzi 21
```
37. Kiritilgan soiniyani daqiqa va soniyalarga ajratib chiqaring
```python
soniya = input("Necha soniya: ")
print(f"{soniya // 60} daqiqayu {soniya % 60} soniya")
```
```text
Necha soniya: 75
1 daqiqayu 15 soniya
```
#### 2.7.2 O'zlashtirish operatorlar
O'zlashtirish operatori o'zgaruvchiga qiymat o'zlashtirish uchun ishlatiladi
38. Foydalanuvchi kiritgan songa yana 15 ni qo'shib ekranga chiqaring:
```python
son = int(input("Son kiriting: "))
son = son + 15
print(son)
```
O'zlashtirish operatorlari hillari ko'p, ularni quyidagi jadvalda keltiramiz:
<br>x = 9
<table>
<tr><td>Operator</td><td>Nomi</td><td>Misol</td><td>Bir hil</td><td>x</td></tr>
<tr><td>=</td><td>O'zlashtirish</td><td>x=9</td><td>x=9</td><td>9</td></tr>
<tr><td>-=</td><td>O'zidan ayirib o'zlashtirish</td><td>x -= 3</td><td>x = x - 3</td><td>6</td></tr>
<tr><td>+=</td><td>O'ziga qo'shib o'zlashtirish</td><td>3 += 3</td><td>x = x + 3</td><td>12</td></tr>
<tr><td>*=</td><td>O'ziga ko'paytirib o'zlashtirish</td><td>x *= 3</td><td>x = x * 3</td><td>27</td></tr>
<tr><td>/=</td><td>O'ziga bo'lib o'zlashtirish</td><td>x /= 3</td><td>x = x / 3</td><td>3</td></tr>
<tr><td>%=</td><td>O'zidan qoldiq olib o'zlashtirish</td><td>x %= 4</td><td>x = x % 4</td><td>1</td></tr>
<tr><td>//=</td><td>O'zidan butun qismini olib o'zlashtirish</td><td>x //= 4</td><td>x = x // 4</td><td>2</td></tr>
<tr><td>**=</td><td>O'zini darajaga ko'tarib o'zlashtirish</td><td>x **= 2</td><td>x = x ** 2</td><td>81</td></tr>
</table>
39. Foydalanuvchi kiritgan parametr asosida kvadrat yuzini ekranga chiqaring:

```python
son = int(input("Kvadrat tomonini kiriting: "))
son **= 2 # son = son ** 2 bilan bir hil
print("Kvadrat yuzi:", son)
```
```text
Kvadrat tomonini kiriting: 5
Kvadrat yuzi: 25
```
#### 2.7.3 Tarkibida borligini bildiruvchi operatorlar
in operatori biron qiymat to'plamda yoki satrda borligini tekshirish uchun ishlatiladi 
<table>
<tr><td>Operator</td><td>Misol</td><td>Ma'nosi</td><td>Natija</td></tr>
<tr><td>in</td>
<td>'h' in 'habar'<br>5 in [1,2,3]<br>5 in (1,2,3)<br>3 in {1,2,3}<br>'car' in lugat.keys()<br>'moshina' in lugat.values()</td>
<td>h harfi habar so'zida bormi<br>5 soni [1,2,3] to'plamida bormi<br>5 soni (1,2,3) to'plamida bormi<br>5 soni {1,2,3} to'plamida bormi<br>'car' so'zi lugat kalitlari to'plamida bormi<br>'moshina' so'zi lugat ning qiymatlari to'plamida bormi</td>
<td>True<br>False<br>False<br>True<br>True<br>True</td></tr>
<tr><td>not in</td>
<td>'h' not in 'habar'<br>5 not in [1,2,3]<br>5 not in (1,2,3)<br>3 not in {1,2,3}<br>'car' not in lugat.keys()<br>'moshina' not in lugat.values()</td>
<td>h harfi habar so'zida yo'qmi<br>5 soni [1,2,3] to'plamida yo'qmi<br>5 soni (1,2,3) to'plamida yo'qmi<br>5 soni {1,2,3} to'plamida yo'qmi<br>'car' so'zi lugat kalitlari to'plamida yo'qmi<br>'moshina' so'zi lugat ning qiymatlari to'plamida yo'qmi</td>
<td>False<br>False<br>False<br>True<br>True<br>True</td></tr>
</table>

40. Kiritilgan harf lotin harfiga tegishli ekanligini aniqlang:
```python
lotin_harflar = "abdefghijklmnopqrstuvxyzo'g'shchng'"
harf = input("Lotin harfini kiriting: ").lower()
print(harf in lotin_harflar)
```
```text
Lotin harfini kiriting: sh
True
```
```text
Lotin harfini kiriting: w
False
```
### 2.7.4 Taqqoslash operatori

<table>
<tr><td>Operator</td><td>Nomi</td><td>Misol</td><td>Javobi</td></tr>
<tr><td>==</td><td>Tengmi</td><td>3 == 6</td><td>False</td></tr>
<tr><td>!=</td><td>Teng emasmi</td><td>3 != 6</td><td>True</td></tr>
<tr><td>></td><td>(Chapdagi son o'ngdagi sondan) kattami</td><td>3 > 6</td><td>False</td></tr>
<tr><td><</td><td>Kichikmi</td><td>3 < 6</td><td>True</td></tr>
<tr><td>>=</td><td>Katta yoki tengmi</td><td>6 >= 6</td><td>True</td></tr>
<tr><td><=</td><td>Kichik yoki tengmi</td><td>3 <= 6</td><td>True</td></tr>
</table>

41. a soni b soniga teng emasligini tekshiring:
```python
a = int(input("a = "))
b = int(input("b = "))
print(a != b)
```
```text
a = 5
b = 15
True
```
```text
a = 5
b = 5
False
```
### Sohaviy
#### Oson daraja
Sohaviy masalalarni mantiqiy masaladan farqi shuki, u ham mantiqiy lekin uni yechish uchun usha sohani o'rganish talab qilinadi. Masalan quyida shaxmat qoidalarini bilmasdan turib, masalani yecha olmaysiz, shuning uchun avval kerakli qoidalar bilan tanishib chiqamiz, so'ng uni yechamiz<br><br>
42. Piyoda shaxmat doskasida (2,2) koordinatada joylashgan. Siz shunday dastur tuzinki, foydalnuvchi x va y koordinatasini kiritsin, agar piyoda usha koordinataga yurish qila olsa, ekranga True, aks holda False qiymati chiqsin

<p align="center">
<img src="images/chess_1.png">
</p>

<br>Masalani yechishdan oldin, qoidalarni tushunib olamiz:<br>
Shaxmat doskasini x,y o'qidan iborat deb tasavvur qilamiz va x,y qiymatlari [1-8] oraliqdagi qiymatlardan iborat.
Biz bilamizki, piyoda 2-qatorda turganda ikkita yurish qila oladi. Ya'ni (2,3) yoki (2,4) koordinataga yurish qila oladi. Qolgan holatda yura olmaydi.
<br>
*x0,y0* - boshlang'ich koordinata<br>
*x1,y2* - ohirgi koordinata<br>
O'ylab ko'ring bizda piyoda faqat to'g'riga yuradi, ya'ni x o'qida o'zgarish bo'lmaydi, shuning uchun ham x1 qiymati boshlang'ich holatga teng (ya'ni x1 = x0). y1 esa boshlang'ich koordinatasiga  nisbatan 1 yoki 2 qadam farq qilishi mumkin (ya'ni y1 = y0 + 1 yoki y1 = y0 + 2). Mana shunday qilib ui formulasini tuzib olamiz. Endi mana shu shartlarni and/or kalit so'zlari bilan yozamiz  
```python
x0 = 2
y0 = 2
print("Shaxmat doskasida piyoda (2,2) koordinatada joylashgan\nPiyoda qaysi koordinataga yurish qila oladi?")
x1 = input("x ni kiriting: ")
y1 = input("y ni kiriting: ")
 
print(x0 == x1 and (y1 == y0 + 1 or y1 == y0 + 2))    
```
```text
Shaxmat doskasida piyoda (2,2) koordinatada joylashgan
Piyoda qaysi koordinataga yurish qila oladi?
x ni kiriting: 4 
y ni kiriting: 5
False
```
```text
Shaxmat doskasida piyoda (2,2) koordinatada joylashgan
Piyoda qaysi koordinataga yurish qila oladi?
x ni kiriting: 2 
y ni kiriting: 3
True
```

*Izoh:* Biz x va y ni bir paytda tekshirishimiz kerak, shuning uchun uni orasiga and qo'yamiz, y esa ikki qiymatdan birini oladi, yoki y0 + 1 yoki y0 + 2. Shuning uchun uni orasiga or qo'ydik. Lekin qavslarni esdan chiqarmaslik kerak. Agar qavslar qo'yilmasa, shart ma'nosi o'zgarib ketadi.<br>
Keling mana bu xato bo'lgan holatni ko'ramiz: <br>
```text
print(x0 == x1 and y1 == y0 + 1 or y1 == y0 + 2)    
```
Bu yerda **x0 == x1 and y1 == y0 + 1** sharti to'g'ri yozilgan, x1=2, y1=3 holatida ishlaydi. Endi keyingi shartni ko'ramiz. **or y1 == y0 + 2** shartida x1 qiymati uchun shart qolib ketgan, shuning uchun y1=3 teng bo'lsa bo'ldi, 'True' chiqaveradi. Bu esa xato x1=2 bo'lishi kerak edi 
<br>
43. Rux shaxmat doskasida (1,1) koordinatada joylashgan. Siz shunday dastur tuzinki, foydalnuvchi x va y koordinatasini kiritsin, agar rux usha koordinataga yurish qila olsa, ekranga True, aks holda False qiymati chiqsin

<p align="center">
<img src="images/chess_2.png">
</p>

```python
x0 = 1
y0 = 1
print("Shaxmat doskasida rux (1,1) koordinatada joylashgan\nRux qaysi koordinataga yurish qila oladi?")
x1 = input("x ni kiriting: ")
y1 = input("y ni kiriting: ")
print(x1 == x0 or y1 == y0)
```
```text
Shaxmat doskasida rux (1,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 2 
y ni kiriting: 3
False
```
```text
Shaxmat doskasida rux (1,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 1 
y ni kiriting: 3
True
```
```text
Shaxmat doskasida rux (1,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 4 
y ni kiriting: 1
True
```

## 3. Amaliyot. O'quvchi
### Mantiqiy
#### Oson daraja
1. Kiritilgan son musbatligini tekshiring:
```text
Son kiriting: 5
True
```
```text
Son kiriting: -5
False
```
```text
Son kiriting: 0
False
```
2. Kiritilgan son manfiyligini tekshiring:
```text
Son kiriting: 5
False
```
```text
Son kiriting: -10
True
```
```text
Son kiriting: 0
False
```
3. Kiritilgan son 0 ga tengligini tekshiring:
```text
Son kiriting: 0
True
```
```text
Son kiriting: -10
False
```
```text
Son kiriting: 10
False
```
4. Kiritilgan son toq ekanligini tekshiring:
```text
Son kiriting: 10
False
```
```text
Son kiriting: 11
True
```
5. Kiritilgan son juft emasligini tekshiring:
```text
Son kiriting: 10
False
```
```text
Son kiriting: 11
True
```
6. Foydalanuvchidan 4 + 6 = ? bo'lishini so'rang, so'ng kiritilgan sonni 10 soniga tengligini tekshiring:
```text
Quyidagi ifoda natijasini kiriting:
4 + 6 = 11
False
```
```text
Quyidagi ifoda natijasini kiriting:
4 + 6 = 10
True
```
7. Foydalnuvchidan 5 ga karrali son kiritishini so'rang, so'ng tekshiring:
```text
5 ga karrali son kiriting: 15
True
```
```text
5 ga karrali son kiriting: 16
False
```
8. Ekranga bitta harfi berkitilgan so'z chiqaring, so'ng foydalanuvchidan usha harfni topishini so'rang, so'ng javobni solishtiring:
```text
Quyida * bilan berkitilgan harfni toping:
olmax*n 
Harf kiriting: o
True
```
```text
Quyida * bilan berkitilgan harfni toping:
olmax*n 
Harf kiriting: g
False
```
9. Foydalanuvchidan login kiritishini so'rang, so'ng harflar katta yoki kichikligidan qat'iy nazar 'admin' so'ziga tengligini tekshiring:
```text
Loginni kiriting: abc
False
```
```text
Loginni kiriting: admin
True
```
```text
Loginni kiriting: ADMin
True
```
10. Katta harfga tekshirish. Foydalanuvchidan harf kiritishni so'rang, agar harf katta bo'lsa, True , aks holda False chiqsin
```text
Harf kiriting: f
False
```
```text
Harf kiriting: H
True
```
11. Foydalnuvchi kiritgan harf kiril ekanligini tekshiring:
```text
Kiril harfini kiriting: g
False
```
```text
Kiril harfini kiriting: н
True
```
12. Sizda ikki o'zgruvchi bor. Birida o'zbekcha matn, ikkinchisida uning tarjimasi bo'lgan inglizcha matn. O'zbekcha matnni ekranga chiqarib, foydalanuvchidan matnda uchragan ixtiyoriy so'zning ingliz tilida tarjimasini yozib berishini so'rang. So'ng foydalanuvchi kiritgan so'zni inglizcha matnda borligini aniqlang  
```text
Men ismim Otabek. Men 40 yoshdaman. Men muhandisman.
Yuqoridagi matnda kelgan ixtiyoriy so'zni tarjimasini kiriting: name
True 
```
```text
Men ismim Otabek. Men 40 yoshdaman. Men muhandisman.
Yuqoridagi matnda kelgan ixtiyoriy so'zni tarjimasini kiriting: car
False
```
13. Agar foydalanuvchi hech nima yozmasa, False biron narsa yozsa True chiqarsin:
```text
Login kiriting: 
False
```
```text
Login kiriting: abs 
True
```
#### O'rta daraja
14. foydalanuvchi o'sish tartibida 3 ta son kiritsin. O'sish tartibida ekanligini tekshiring:
```text
Birinchi son: 4
Ikkinchi son: 6
Uchinshi son: 10
True
```
```text
Birinchi son: 4
Ikkinchi son: 16
Uchinshi son: 10
False
```
15. Foydalanuvchi kiritgan ikki son toq ekanligini tekshiring:
```text
Birinchi son: 4
Ikkinchi son: 16
False
```
```text
Birinchi son: 7
Ikkinchi son: 9
True
```
```text
Birinchi son: 7
Ikkinchi son: 16
False
```
16. Foydalanuvchi kiritgan ikki sondan hech bo'lmaganda bittasi toqligini tekshiring:
```text
Birinchi son: 7
Ikkinchi son: 16
True
```
```text
Birinchi son: 7
Ikkinchi son: 17
True
```
```text
Birinchi son: 8
Ikkinchi son: 16
False
```
17. Foydalanuvchi kiritgan ikki sondan faqat bittasi toqligini tekshiring: 
```text
Birinchi son: 8
Ikkinchi son: 16
False
```
```text
Birinchi son: 7
Ikkinchi son: 16
True
```
```text
Birinchi son: 8
Ikkinchi son: 9
True
```
```text
Birinchi son: 7
Ikkinchi son: 15
False
```
18. Foydalanuvchi kiritgan ikkala son bir paytda yoki juft bo'lsin yoki toq bo'lsin:
```text
Birinchi son: 7
Ikkinchi son: 15
True
```
```text
Birinchi son: 8
Ikkinchi son: 16
True
```
```text
Birinchi son: 7
Ikkinchi son: 16
False
```
```text
Birinchi son: 8
Ikkinchi son: 15
False
```
19. Foydalanuvchi kiritgan uchchala son hammasi musbatligini tekshiring:
```text
Birinchi son: 8
Ikkinchi son: 15
Uchinchi son: 6
True
```
```text
Birinchi son: -8
Ikkinchi son: 15
Uchinchi son: 6
False
```
20. Foydalanuvchi kiritgan uchchala sondan hech bo'lmasa bittasi musbatligini tekshiring:
```text
Birinchi son: 8
Ikkinchi son: 15
Uchinchi son: 6
True
```
```text
Birinchi son: -8
Ikkinchi son: 15
Uchinchi son: 6
True
```
```text
Birinchi son: -8
Ikkinchi son: -15
Uchinchi son: 6
True
```
```text
Birinchi son: -8
Ikkinchi son: -15
Uchinchi son: -6
False
```
21. Foydalanuvchi kiritgan son ikki honali ekanligini tekshiring:
```text
Ikki honali son kiriting: 20
True
```
```text
Ikki honali son kiriting: 2
False
```
```text
Ikki honali son kiriting: 200
False
```
22. Foydalanuvchi kiritgan son ikki honali va juft ekanligini tekshiring: 
```text
Ikki honali son kiriting: 20
True
```
```text
Ikki honali son kiriting: 21
False
```
```text
Ikki honali son kiriting: 2
False
```
```text
Ikki honali son kiriting: 200
False
```
23. Foydalanuvchi kiritgan uchta sondan hech bo'lmaganda ikkitasi bir-biriga tengligini tekshiring:
```text
Birinchi son: 8
Ikkinchi son: 8
Uchinchi son: 8
True
```
```text
Birinchi son: 18
Ikkinchi son: 8
Uchinchi son: 8
True
```
```text
Birinchi son: 18
Ikkinchi son: 28
Uchinchi son: 8
False
```
24. Foydalanuvchi kiritgan uchta sondan ikkitasining ishoralari qarama-qarshiligini tekshiring:
```text
Birinchi son: 18
Ikkinchi son: -18
Uchinchi son: 8
True
```
```text
Birinchi son: 18
Ikkinchi son: 18
Uchinchi son: 8
False
```
```text
Birinchi son: 18
Ikkinchi son: 40
Uchinchi son: 8
False
```
25. Foydalanuvchi kiritgan uchta sonning hammasi har hil ekanligini tekshiring:
```text
Birinchi son: 18
Ikkinchi son: 40
Uchinchi son: 8
True
```
```text
Birinchi son: 8
Ikkinchi son: 40
Uchinchi son: 8
False
```
```text
Birinchi son: 8
Ikkinchi son: 8
Uchinchi son: 8
False
```
26. Foydalanuvchi kiritgan uchchala son yoki o'suvchi tartibda yoki kamayish tartibida ekanligini tekshiring:
```text
Birinchi son: 8
Ikkinchi son: 10
Uchinchi son: 20
True
```
```text
Birinchi son: 18
Ikkinchi son: 10
Uchinchi son: 4
True
```
```text
Birinchi son: 8
Ikkinchi son: 30
Uchinchi son: 20
False
```
27. Foydalanuvchi kiritgan 5 honali sonni chapdan o'qisa ham o'ngdan o'qisa ham bir hil ekanligini tekshiring:
```text
5 honali son kiriting: 34567
False
```
```text
5 honali son kiriting: 34543
True
```
```text
5 honali son kiriting: 12321
True
```
### Sohaviy
#### Oson daraja
28. Fil shaxmat doskasida (1,1) koordinatada joylashgan. Siz shunday dastur tuzinki, foydalnuvchi x va y koordinatasini kiritsin, agar fil usha koordinataga yurish qila olsa, ekranga True, aks holda False qiymati chiqsin
<br>*Yordam:*<br>
Mumkin bo'lgan koordinatalarni hammasini qog'ozga yozib chiqing, so'ng formulani topishga harakat qiling
<br>
<p align="center">
<img src="images/chess_4.png">
</p>

```text
Shaxmat doskasida rux (1,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 2 
y ni kiriting: 2
True
```
```text
Shaxmat doskasida rux (1,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 5 
y ni kiriting: 2
False
```
29. Fil shaxmat doskasida (3,1) koordinatada joylashgan. Siz shunday dastur tuzinki, foydalnuvchi x va y koordinatasini kiritsin, agar fil usha koordinataga yurish qila olsa, ekranga True, aks holda False qiymati chiqsin
<br>
<p align="center">
<img src="images/chess_3.png">
</p>

```text
Shaxmat doskasida rux (3,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 2 
y ni kiriting: 2
True
```
```text
Shaxmat doskasida rux (3,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 4 
y ni kiriting: 2
True
```
```text
Shaxmat doskasida rux (3,1) koordinatada joylashgan
Rux qaysi koordinataga yurish qila oladi?
x ni kiriting: 4 
y ni kiriting: 4
False
```
30. Huddi shunday shoxga nisbatan bajaring
<br>
<p align="center">
<img src="images/chess_5.png">
</p>

```text
Shaxmat doskasida shox (5,1) koordinatada joylashgan
Shox qaysi koordinataga yurish qila oladi?
x ni kiriting: 6 
y ni kiriting: 1
True
```

```text
Shaxmat doskasida shox (5,1) koordinatada joylashgan
Shox qaysi koordinataga yurish qila oladi?
x ni kiriting: 7 
y ni kiriting: 1
False
```
