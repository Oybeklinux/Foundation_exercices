# Mavzu 6: tuple (o'zgarmas ro'yxat)
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
tuple - o'zgarmas ro'yxat. s'ni boshida bir marta qiymat beriladi, keyin o'zgartirib bo'lmaydi
element - ro'yxat tarkibidagi har bir qiymat
indeks - elementlarning ro'yxatdagi pozitsiyasi
```
### 1.2 O'qish uchun materiallar
- w3schools
  - [tuples](https://www.w3schools.com/python/python_tuples.asp)
- sariq dev
  - [Ro'yxat bilan ishlash](https://python.sariq.dev/ozgaruvchilar-va-malumot-turlari/08-list-tuple)
## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 tuple - o'zgarmas ro'yxat](#21-tuple---ozgarmas-royxat)
  - [2.1.1 Foydalanish](#211-foydalanish)
  - [2.1.2 O'zgartirish](#212-ozgartirish)
  - [2.1.3 Qo'shish](#213-qoshish)
  - [2.1.4 O'chirish](#214-ochirish)
  - [2.1.5 for - hammasini ko'rish](#215-for---hammasini-korish)
  - [2.1.6 Tartiblash](#216-tartiblash)
  - [2.1.7 Ko'chirish](#217-kochirish)
  - [2.1.8 Birlashtirish](#218-birlashtirish)
  
### 2.1 tuple - o'zgarmas ro'yxat
#### 2.1.1 Foydalanish

1. Bo'sh ro'yxatni e'lon qiling:
```python
royxat = ()
```
yoki
```python
royxat = tuple()
```
2. (1-10) sonlarni saqlovchi ro'yxatni e'long qiling:
```python
royxat = (1,2,3,4,5,6,7,8,9,10)
```
3. (a-z) harflarni saqlovchi ro'yxat e'lon qiling:
```python
alfavit = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
```
4. Ro'yxatda nechta son bor?
```python
royxat = (1,2,3,4,5)
print(f"Ro'yxat uzunligi: {len(royxat)}")
```
```text
Ro'yxat uzunligi: 5
```
5. Ro'yxat e'lon qiling unga element sifatida, 34, True, 'so"z', [1,2,3], (4,5,6) kabi sodda va murakkab bo'lgan qiymatlarni o'zlashtiring
```python
sonlar = (1,2,3,4,5)
harflar = ('a','b','c')
sozlar = ('olma', 'nok', 'anor')
royxatlar = ([1,2,3], [4,5,6], [7,8,9])
lugatlar = ({"car": "moshina"}, {"pencil": "qalam"})
ozgarmas_royxatlar = ((10,20,30), (40,50,60))
mantiqiy = (True, False, True)
aralash = (1,'a', True,[1,2,3], {'car':'moshina'}, ('oq', 'yashil'))
```
6. Ro'yxat e'lon qiling, so'ng uni ma'lumot turini yozing:
```python
sonlar = (1, 2, 3)
print(type(sonlar))
```
```text
<class 'tuple'>
```
Royxatning har bir elementi ma'lum pozitsiyada joylashgan  bo'ladi. U pozitsiya - indeks deyiladi. Indeks orqali biz ro'yxatning elementini olamiz
<br>
![](images/img_1.png)
<br>
<li>Musbat indeks - chapdan o'ngga qarab 0 dan boshluvchi son: 0,1,2,3, ..</li>
<li>Manfiy indeks - o'ngdan chapga qarab -1 boshlanuvchi son: -1,-2,-3,-4, ..</li>
<br>
7. Ro'yxatdan ikkinchi elementni ekranga chiqaring:

```python
harflar = ('d','a','s','t','u','r','c','h','i')
print(f"Ikkinchi harf: {harflar[1]}")
#harflar[2] emas
```
```text
Ikkinchi harf: a
```
8. Ro'yxatdan birinchi va ohirgi elementni chiqaring:
```python
harflar = ('d','a','s','t','u','r','c','h','i')
print(f"Birinchi harf: {harflar[0]}")
print(f"Ohirgi harf: {harflar[-1]}")
```
```text
Birinchi harf: d
Ohirgi harf: i
```
9. Ro'yxatdan 70,30,20,90 elementlarni qirqib oling, so'ng ekranga chiqaring:
```python
harflar = (50,70,30,20,90,10,50)
bazi_harflar = harflar[1:5]
print(bazi_harflar)
```
```text
(70, 30, 20, 90)
```
*Izoh:*<br>
Ro'yxatyda 70 ikkinchi son, lekin indeks 0 dan boshlangani uchun, boshlanish indeksga 2 emas 1 beramiz. 90 5-o'rinda, indesk bo'yicha 4-o'rinda, lekin tugash indeksidagi elementni o'zini hisobga olmagani uchun biz 6 ni beramiz.
<br>
![](images/img.png)

10. Ro'yxat boshidan 4, ohiridan 4 elementni qirqib, ekranga chiqaring
```python
harflar = (50,70,30,20,90,10,50)
bosh_harflar = harflar[:4]
ohirgi_harflar = harflar[-4:]
print(f"Boshidagi 4 harf: {bosh_harflar}")
print(f"Ohiridagi 4 harf: {ohirgi_harflar}")
```
*Izoh:*<br>
Boshidan qirqib oladigan bo'lsa, boshidagi 0 indeksni bermasak ham bo'ladi.<br>
Ohiridan qirqadigan bo'lsak, ohiridagi indeksni bermaymiz. Agar -1 bersak, uholda ohirgi elementni hisobga olmaydi<br>
11. Sizda bozorlik ro'yxati bor. Ro'yxatda foydalanuvchi kiritgan mahsulot bozorlik ro'yxatida borligini aniqlang: 

```python
bozorlik = ('olma', 'nok', 'sabzi')
mahsulot = input("Ro'yxatdan nimani qaramoqchisiz: ")
print(mahsulot in bozorlik)
```
```text
Ro'yxatdan nimani qaramoqchisiz: uzum
False
```
```text
Ro'yxatdan nimani qaramoqchisiz: olma
True
```
12. Foydalanuvchi siz belgilagan formatda bir qancha mahsulotlarni kiritsin. So'ng siz ularni tuple ga o'girib, birinchi va ohirini chiqaring
```python
satr = input(f"olma,anor,banan ko'rinishida mahsulotlarni kiriting: ")
royxat = tuple(satr.split(","))
print(f"Birinchi mahsulot: {royxat[0]}")
print(f"Ohirgi mahsulot: {royxat[-1]}")
```
```text
olma,anor,banan ko'rinishida mahsulotlarni kiriting: bodring,pamildori,garimdori,zanjabil,ko'kat
Birinchi mahsulot: bodring
Ohirgi mahsulot: ko'kat
```

14. Foydalanuvchidan har birini orasi # belgisi bilan ajratilgan 5 son kiritishini so'rang, so'ng ularni tuple ga o'girib, haqiqatda 5 ta elementdan iboratligini aniqlang:
```python
satr = input("Orasi # bilan ajratilgan faqat 5 son kiriting: ")
royxat = tuple(satr.split("#"))
print(len(royxat) == 5)
```
```text
Orasi # bilan ajratilgan faqat 5 son kiriting: 3#5#6#5
False 
```
```text
Orasi # bilan ajratilgan faqat 5 son kiriting: 3#5#6#5#67
True 
```
#### 2.1.2 O'zgartirish
___
O'zgartirish metodi mavjud emas, chunki tuple o'zgarmas ro'yxat. Lekin shunda ham uni yo'li bor, avval list ga o'girib bajariladi, so'ng qayta tuple ga o'giriladi. Odatda unday qilinmaydi
___
15. (1,2,3,5,6) ro'yxat berilgan. Birinchi elementini 10 soniga o'zgartiring. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring
```python
sonlar = (1,2,3,5,6)
print(sonlar)
# o'zgartirish uchun list ga o'girib olamiz
sonlar = list(sonlar)
sonlar[0] = 10
# qiymatlar o'zgardi, endi qayta tuple ga o'giramiz
sonlar = tuple(sonlar)
print(sonlar)
```
yoki
```python
sonlar = (1,2,3,5,6)
print(sonlar)
sonlar = (10, ) + sonlar[1:]
print(sonlar)
```
```text
(1, 2, 3, 5, 6)
(10, 2, 3, 5, 6)
```
16. (10,20,30,50,60) ro'yxat berilgan. Ikkinchi elementini shunday o'zgartirinki, o'zini ikkiga ko'paytirib natiani yozing. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```python
sonlar = (10,20,30,50,60)
print(sonlar)
# o'zgartirish uchun list ga o'girib olamiz
sonlar = list(sonlar)
sonlar[1] = sonlar[1] * 2
# qiymatlar o'zgardi, endi qayta tuple ga o'giramiz
sonlar = tuple(sonlar)
print(sonlar)
```
```text
(10, 20, 30, 50, 60)
(10, 40, 30, 50, 60)
```
17. (10,20,30,50,60) ro'yxat berilgan. Ikkinchi va uchinchi pozitsiyadagi qiymatlar o'rni almashib qolsin. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```python
sonlar = (10,20,30,50,60)
print(sonlar)
sonlar = list(sonlar)
sonlar[1], sonlar[2] = sonlar[2], sonlar[1]
sonlar = tuple(sonlar)
print(sonlar)
```
```text
(10, 20, 30, 50, 60)
(10, 30, 20, 50, 60)
```
18. ('olcha', 'olma', 'nok', 'anor') shu yerdan olcha va olma o'rniga bodring va sabzi qiymatiga o'zgartiring. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ('olcha', 'olma', 'nok', 'anor')
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar = list(mahsulotlar)
mahsulotlar[0] = 'bodring'
mahsulotlar[1] = 'sabzi'
mahsulotlar = tuple(mahsulotlar)
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ['olcha', 'olma', 'nok', 'anor']
O'zgargan ro'yxat: ['bodring', 'sabzi', 'nok', 'anor']
```
19. ('olcha', 'olma', 'nok', 'anor') shu yerdan olma va nokni chiqarib tashlab, o'rniga o'rik qiymati yozing. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ('olcha', 'olma', 'nok', 'anor')
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar = list(mahsulotlar)
mahsulotlar[1:3] = ["o'rik"]
mahsulotlar = tuple(mahsulotlar)
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ('olcha', 'olma', 'nok', 'anor')
O'zgargan ro'yxat: ('olcha', "o'rik", 'anor')
```
20. ('olcha', 'sabzi') shu yerdan sabzi o'rniga olma, nok, anor qiymatini yozing. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ('olcha', 'sabzi')
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar = list(mahsulotlar)
mahsulotlar[1:2] = ['olma', 'nok', 'anor']
mahsulotlar = tuple(mahsulotlar)
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ('olcha', 'sabzi')
O'zgargan ro'yxat: ('olcha', 'olma', 'nok', 'anor')
```
### 2.1.3 Qo'shish
___
Qo'shish metodi mavjud emas, chunki tuple o'zgarmas ro'yxat. Shunda ham yo'li bor, ya'ni list ga o'girilib amalga oshirish, lekin odatda bunday qilinmaydi 
___
21. ('olma', 'nok') berilgan. Endi foydalanuvchi kiritgan mevani ro'yxat ohiriga qo'shamiz:
```python
bozorlik = ('olma', 'nok')
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Yana nimani kiritaylik: ")
bozorlik = list(bozorlik)
bozorlik.append(meva)
bozorlik = tuple(bozorlik)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ('olma', 'nok') bor
Yana nimani kiritaylik: bodom
O'zgargan ro'yxat: ('olma', 'nok', 'bodom')
```
22. Bizda ('olma', 'nok') bozorlik ro'yxati berilgan. Foydalnuvchi yana bir muhim mahsulotni kiritadi, uni muhim bo'lgani uchun ro'yxat boshiga kiritamiz:
```python
bozorlik = ('olma', 'nok')
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Yana bitta muhim mahsulotni kiritaylik: ")
bozorlik = list(bozorlik)
bozorlik.insert(0, meva)
bozorlik = tuple(bozorlik)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ('olma', 'nok') bor
Yana bitta muhim mahsulotni kiritaylik: non
O'zgargan ro'yxat: ('non', 'olma', 'nok')
```
23. Bizda ('olma', 'nok') bozorlik ro'yxati berilgan, foydalanuvchi yana bir nechta mahsulot olish kerakligi esiga tushib qoldi, shularni foydaluvchi ma'lumot formatda kiritsin so'ng, hammasini ro'yxatga qo'shib qo'ying:
```python
bozorlik = ('olma', 'nok')
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Nimalar esingizdan chiqib ketdi. ',' bilan yozing: ")
bozorlik = list(bozorlik)
mevalar = meva.split(",")
bozorlik.extend(mevalar)
bozorlik = tuple(bozorlik)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ('olma', 'nok') bor
Nimalar esingizdan chiqib ketdi. ',' bilan yozing: o'rik,shaftoli,banan
O'zgargan ro'yxat: ('olma', 'nok', "o'rik", 'shaftoli', 'banan')
```
24. mevalar = ('olma', 'nok') va sabzavotlar=('sabzi', 'bodring') ro'yxatlari berilgan, ularni birlashtirib yangi ro'yxat hosil qilib, ekranga chiqaring:
```python
mevalar = ('olma', 'nok')
sabzavotlar = ('sabzi', 'bodring')
mahsulotlar = mevalar + sabzavotlar
print(mahsulotlar)
```
```text
('olma', 'nok', 'sabzi', 'bodring')
```

###  2.1.4 O'chirish
___
O'chirish metodi mavjud emas, chunki tuple o'zgarmas ro'yxat. Lekin shunda ham uni yo'li bor, yuqoridagi kabi avval list ga o'girib bajariladi, so'ng qayta tuple ga o'giriladi. Odatda unday qilinmaydi
___
25. (1,2,4,5) ro'yxatidan 4 ni o'chiring:
```python
sonlar = (1,2,4,5)
sonlar = list(sonlar)
print(f"Boshlang'ich holat: {sonlar}")
sonlar.remove(4)
sonlar = tuple(sonlar)
print(f"O'zgargan holat: {sonlar}")
```
26. Foydalanuvchi kiritgan harfni ro'yxatdan o'chiring:
```python
sozlar = ('olma', 'nok', 'banan')
print(sozlar)
sozlar = list(sozlar)
meva = input("Qaysi mahsulotni ro'yxatdan olib tashlash kerak: ")
sozlar.remove(meva)
sozlar = tuple(sozlar)
print(f"O'zgargan ro'yxat: {sozlar}")
```
```text
('olma', 'nok', 'banan')
Qaysi mahsulotni ro'yxatdan olib tashlash kerak: nok
O'zgargan ro'yxat: ('olma', 'banan')
```
27. Ro'yxatdan  4-elementni o'chirib, ro'yxatni va o'chirilgan elementni ekranga chiqaring
```python
sonlar = (20,30,40,50,60)
print(f"Boshlang'ich holat: {sonlar}")
sonlar = list(sonlar)
son = sonlar.pop(3)
sonlar = tuple(sonlar)
print(f"O'zgargan holat: {sonlar}")
print(f"O'chirilgan element: {son}")
```
```text
Boshlang'ich holat: (20, 30, 40, 50, 60)
O'zgargan holat: (20, 30, 40, 60)
O'chirilgan element: 50
```
28. Ro'yxatdan ohirgi elementni o'chiring:
```python
sonlar = (1,2,3,4,5,6)
print(f"Boshlang'ich holat: {sonlar}")
sonlar = sonlar[:-1]
print(f"O'zgargan holat: {sonlar}")
```
yoki 
```text
Boshlang'ich holat: (20, 30, 40, 50, 60)
O'zgargan holat: (20, 30, 40, 50)
O'chirilgan element: 60
```
29. Ro'yxat elementlari yig'indisini topish:
```python
sonlar = (1,2,3,4,5)
print(f"Ro'yxat: {sonlar}")
print(f"Yig'indi: {sum(sonlar)}")
```
```text
Ro'yxat: (1, 2, 3, 4, 5)
Yig'indi: 15
```
### 2.1.5 for - hammasini ko'rish
30. sonlar = [1,2,3,4,5,6] ro'yxatdan hamma sonlarni quyidagi ko'rinishda chiqaring:
```python
sonlar = (1,2,3,4,5,6)
for son in sonlar:
    print(son)
```
```text
1
2
3
4
5
6
```
31. sozlar = ('dastur', 'dasturchi', 'python') ro'xatida har bir elementi va undagi harflar sonini ekranga chiqaring:
```python
sozlar = ('dastur', 'dasturchi', 'python')
for soz in sozlar:
    print(f"soz: {soz}; uzunligi: {len(soz)}")   
```
```text
soz: dastur; uzunligi: 6
soz: dasturchi; uzunligi: 9
soz: python; uzunligi: 6
```

32. sozlar = ('dastur', 'dasturchi', 'python') ro'yxatidan har bir elementi va undagi indeksini chiqaring:
```python
sozlar = ('dastur', 'dasturchi', 'python')
for i in range(0,3):
    print(i, sozlar[i])
```
```text
0 dastur
1 dasturchi
2 python 
```

### 2.1.6 Tartiblash
33. Ro'yxatdagi ismlarni alfavit bo'yicha tartiblab bering:

```python
ismlar = ('Anvar','bekzod', 'Ravshan', 'Lola', 'Otabek')
for ism in sorted(ismlar):
    print(ism)
```
```text
Anvar
Lola
Otabek
Ravshan
bekzod
```
34. Ro'yxatdagi ismlarni alfavit bo'yicha teskari tartiblab bering:

```python
ismlar = ('Anvar','bekzod', 'Ravshan', 'Lola', 'Otabek')
# ismlar.sort() xato
for ism in sorted(ismlar, reverse=True):
    print(ism)
```
```text
Anvar
bekzod
Lola
Otabek
Ravshan
```
35. Harflarni kichik kattaligini hisobga olmay tartiblang
```python
ismlar = ('Anvar','bekzod', 'Ravshan', 'Lola', 'Otabek')

for ism in sorted(ismlar,key=str.lower):
    print(ism)
```
```text
Anvar
bekzod
Lola
Otabek
Ravshan
```
36. Ro'yxatdagi sonlari tartiblab bering:

```python
sonlar = (100, 50, 200, 60, 300, 10)

for son in sorted(sonlar):
    print(son)
```
```text
10
50
60
100
200
300
```
37. Ballarni teskari tartiblab bering:
```python
ballar = (100, 45, 60, 55, 90, 70)

for bal in sorted(ballar, reverse=True):
    print(bal)
```
```text
100
90
70
60
55
45
```
### 2.1.7 Ko'chirish
Quyidagi kodni ishga tushirganda hotiradan ikkita joy ajratiladi. Biri son1 uchun ikkinchisi son2 uchun. Ikkala hotirada ham 10 soni saqlanadi 
```python
son1 = 10
son2 = son1
```
tuple toifasida ham huddi shunday (list, set, dict toifalaridan farqli ravishda):
```python
sonlar1 = (1,2,3,4)
sonlar2 = sonlar1
del sonlar1
print(sonlar2)
```
### 2.1.8 Birlashtirish
**Agar elementlari str bo'lsa**, u holda ro'yxat elementlarini birlashtirish uchun join() metodini ishlatishimiz mumkin. Bu str metodi hisoblanadi:
39. Siz bozordan mevalar = ('olma', 'nok') olgansiz. Shuni gap bilan dasturda yozishingiz kerak. Ya'ni men olma va nok oldim deb yozishingiz kerak
```python
mevalar = ('olma', 'nok')
print(f"Men bozordan {' va '.join(mevalar)} oldim")
```
```text
Men bozordan olma va nok oldim
```
40. mevalar = ('olma', 'nok', 'banan') ro'yxati berilgna. Siz shularni har birini orasiga vergul qo'ygan holda quyidagicha gap yozishingiz kerak:
```python
mevalar = ('olma', 'nok', 'banan')
print(f"{', '.join(mevalar)} mevalardir")
```
```text
olma, nok, banan mevalardir
```

41. mevalar = ('olma', 'nok', 'banan') ro'yxati berilgna. Siz shularni har birini orasiga vergul qo'ygan holda quyidagicha gap yozishingiz kerak:
```text
olma, nok va banan mevalardir
```
```python
mevalar = ('olma', 'nok', 'banan')
mevalar2 = mevalar[:-1]
print(f"{', '.join(mevalar2)} va {mevalar[-1]} mevalardir")
```

## 3. Amaliyot. O'quvchi
### Sintaksis masalalar
1. To'rtta ro'yxat e'lon qiling, biri bo'sh, ikkinchisi sonlardan, uchinchisi satrdan, to'rtinchisi mantiqiy qiymatlardan iborat bo'lsin, so'ng quyidagicha ularni qiymatlarini va uzunligini ekranga chiqaring:
```text
Birinchi ro'yxat: (). Uning uzunligi: 0
Birinchi ro'yxat: (1, 2, 3, 4, 5). Uning uzunligi: 5
Birinchi ro'yxat: ('olma', 'anor', 'banan', 'uzum', 'nok'). Uning uzunligi: 5
Birinchi ro'yxat: (True, False, True, True, False). Uning uzunligi: 5
```
2. To'rtta ro'yxat e'lon qiling, biri bo'sh, ikkinchisi sonlardan, uchinchisi satrdan, to'rtinchisi mantiqiy qiymatlardan iborat bo'lsin, so'ng quyidagicha ularni ma'lumot turini (type) va qiymatlarining ma'lumot turini  ekranga chiqaring: 
```text
Birinchi ro'yxat toifasi: <class 'tuple'>. 
Birinchi ro'yxat toifasi: <class 'tuple'>. Qiymatining toifasi: <class 'int'>
Birinchi ro'yxat toifasi: <class 'tuple'>. Qiymatining toifasi: <class 'str'>
Birinchi ro'yxat toifasi: <class 'tuple'>. Qiymatining toifasi: <class 'bool'>
```
3. Shunday ro'yxat tuzingki, har bir elementi toifasi har hil bo'lsin (int,str,bool, float va hak). So'ng ro'yxatni va uning toifasini, har bir elementni va uning toifasini quyidagi ko'rinishda ekranga chiqaring chiqaring:
```text
Ro'yxat: ('olma', True, 3.14, 3000, [1, 2, 3, 4]). Uning toifasi: <class 'tuple'>
Birinchi element: olma. Uning toifasi: <class 'str'>
Birinchi element: True. Uning toifasi: <class 'bool'>
Birinchi element: 3.14. Uning toifasi: <class 'float'>
Birinchi element: 3000. Uning toifasi: <class 'int'>
Birinchi element: [1, 2, 3, 4]. Uning toifasi: <class 'list'>
```
4. Siz bozor qilish uchun tahminan 10 ta elementli royxat tuzishingiz kerak. Har meva, sabzavotlardan iborat royxat bo'lsin. Endi ro'yxatdan quyidagilarni chiqarishingiz kerak:
<ul>
<li>Birinchisi</li>
<li>Ohirisi</li>
<li>2,3,4 o'rindagi narsalar</li>
<li>Boshidagi 5 tasi</li>
<li>Ohiridagi 5 tasi</li>
</ul>
Shularni quyidagi ko'rinishda ekranga chiqarishingiz kerak:

```text
Birinchisi: anor
Ohiridagisi: qaymoq
2,3,4 o'rindagi mahsulotlar: ('banan', 'kartoshka', 'sabzi')
Boshidan 5 tasi: ('anor', 'banan', 'kartoshka', 'sabzi', 'qulupnay')
Ohiridan 5 tasi: ("sholg'om", "balg'ari", 'baliq', "mol go'shti", 'qaymoq')
```
5. Foydalanuvchi kamida 4 mahsulot kiritishini so'rang va har birini orasi : bilan ajratib yozsin. Siz shulardan boshidagi 2tasini ekranga chiqaring
```text
qulupnay:sabzi:anor ko'rinishida kamida 4 mahsulot kiriting: olcha shaftoli banan anor uzum
boshidagi 2 mahsulot: ('olcha', 'shaftoli')
```
6. Har birini orasini '-' bilan ajratib foydalanuvchi kamida 4 mahsulot kiritishini so'rang, so'ng kiritilgan qiymat kamida 4 ekanligini aniqlang:
```text
qulupnay-sabzi-anor ko'rinishida kamida 4 mahsulot kiriting: olma-o'rik-olho'ri
False
```
```text
qulupnay-sabzi-anor ko'rinishida kamida 4 mahsulot kiriting: olma-o'rik-olho'ri-anor
True
```
```text
qulupnay-sabzi-anor ko'rinishida kamida 4 mahsulot kiriting: olma-o'rik-olho'ri-anor-banan
True
```
7. Foydalanuvchi 5 son kiritadi. Siz uni ro'yxatga aylantirib bo'lgach, ohirgi elementni 0 ga o'zgartiring. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```text
Sonlarni ',' belgisi bilan kiriting: 7,34,3,507,160 
Asl ro'yxat: (7,34,3,507,160)
O'zgargan ro'yxat: (7,34,3,507,0)
```
8. Foydalanuvchi 5 son kiritadi. Siz uni ro'yxatga aylantirib bo'lgach, ohirgi elementni 10 ga bo'lib natijani uni o'rniga yozib qo'ying. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```text
Sonlarni ',' belgisi bilan kiriting: 7,34,3,507,160 
Asl ro'yxat: (7,34,3,507,160)
O'zgargan ro'yxat: (7,34,3,507,16)
```
9. Foydalanuvchi 5 son kiritadi. Siz uni ro'yxatga aylantirib bo'lgach, birinchi element bilan ohirgi, ikkinchi element bilan ohiridan ikkinchi elementni o'rnini almashtiring. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```text
Sonlarni ',' belgisi bilan kiriting: 7,34,3,507,160 
Asl ro'yxat: (7,34,3,507,160)
O'zgargan ro'yxat: (160,507,3,34,7)
```
10. Foydalanuvchi 5 ta mahsulot kiritasi, keyin qarasaki ro'yxatdagi 2 va 3 mahsulot bozorda yo'q ekan, endi ularni o'rniga boshqa mahsulot oladi. Shuni dasturini yozing:
```text
kamida 5 mahsulotlarni ',' bilan yozing: olma,nok,anor,bodring,sabzi,uzum
Ro'yxat: olma,nok,anor,bodring,sabzi,uzum
2 va 3 mahsulotlar o'rniga nima(lar) olasiz? karam
O'zgargan ro'yxat: ('olma', 'karam', 'bodring', 'sabzi', 'uzum') 
```
```text
kamida 5 mahsulotlarni ',' bilan yozing: olma,nok,anor,bodring,sabzi,uzum
Ro'yxat: olma,nok,anor,bodring,sabzi,uzum
2 va 3 mahsulotlar o'rniga nima(lar) olasiz? go'sht,tovuq,bodom,yer-yong'oq
O'zgargan ro'yxat: ('olma', "go'sht", 'tovuq', 'bodom', "yer-yong'oq", 'bodring', 'sabzi', 'uzum')
```
11. (1,2,3,4) ro'yxat berilgan. Foydalanuvchidan bitta son kiritishni so'rang, so'ng uni ro'yxatga qo'shib qo'ying:
```text
Ro'yxat: (1, 2, 3, 4)
Son kiriting: 15
O'zgargan ro'yxat: (1, 2, 3, 4, 15)
```
12. (1,2,3,4) ro'yxat berilgan. Foydalanuvchidan bitta son kiritishni so'rang, so'ng uni ro'yxatning boshiga qo'shib qo'ying:
```text
Ro'yxat: (1, 2, 3, 4)
Son kiriting: 150
O'zgargan ro'yxat: (150, 1, 2, 3, 4)
```
13. ('qalam', 'ruchka') ro'yxati berilgan. Foydalanuvchi yana ikkita so'z kiritishsin, ularni ro'yxatga qo'shib qo'ying:
```text
Ro'yxat: ('qalam', 'ruchka')
Son kiriting: daftar kitob
O'zgargan ro'yxat: ('qalam', 'ruchka', 'daftar', 'kitob')
```
14. ('uzum','nok') ro'yxati berilgan. Foydalanuvchidan bitta mahsulot qo'shishni so'rang. Uni ro'yxat ohirisiga qo'shing. So'ng yana bitta muhimroq bo'lgan mahsulot kiritishini so'rang, uni ro'yxatda ikkinchi pozitsiyaga qo'shing, so'ng yana bir nechta mahsulot kiritishni so'rang, ularni ro'yxat ohirisiga qo'shib qo'ying:
```text
Hozircha bozorlik ro'yxatida ('olma', 'nok') bor
Bitta muhim bo'lmagan mahsulot yozing: bodring
O'zgargan ro'yxat: ('olma', 'nok', 'bodring')
Endi bitta muhim mahsulot yozing: go'sht
O'zgargan ro'yxat: ('olma', "go'sht", 'nok', 'bodring')
Endi bir nechta muhim bo'lmagan mahsulotlarni ',' bilan yozing: pista,magiz,hurmo
O'zgargan ro'yxat: ('olma', "go'sht", 'nok', 'bodring', 'pista', 'magiz', 'hurmo')
```
15. ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp') ro'yxatni ekranga chiqaring. Foydalanuvchidan o'chirish kerak bo'lgan meva nomini yozishni so'rab, uni ro'yxatdan o'chirigin
```text
Ro'yxat: ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp')
O'chiriladigan mevani kiriting: olma
O'zgartirilgan ro'yxat: ('sabzi','banan', 'bodring', 'nok', 'turp')
```
16. ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp') ro'yxatidan 2 va 3-elementni o'chiring
```text
Boshlang'ich ro'yxat: ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp')
O'zgartirilgan ro'yxat: ('sabzi','nok', 'turp')
```
17. ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp') ro'yxatidan hamma elementlarni tartiblab chiqaring:
```text
Asl ro'yxat: ('olma', 'sabzi','banan', 'bodring', 'nok', 'turp')
Tartiblangan ro'yxat: ['banan', 'bodring', 'nok', 'olma', 'sabzi', 'turp']
```
18. Ro'yxatdagi kompaniyalarni alfavit bo'yicha ekranga chiqaring
```python
konpaniyalar = ('Apple', 'Microsoft', 'Sumsung', 'Mi')
```
```text
Apple
Mi
Microsoft
Sumsung
```
19. Yuqoridagi ro'yxatni teskarilab berin:
```text
Sumsung
Microsoft
Mi
Apple
```
20. mevalar = ('olma', 'banan') ro'yxatini boshqa ro'yxatga ko'chirib oling, son'ng uni teskari tartiblab chiqaring:
```text
Asl ro'yxat: ('olma', 'banan', 'sabzi', 'magiz')
Tartiblangan ro'yxat: ('sabzi', 'olma', 'magiz', 'banan')
```
21. mevalar = ('olma', 'nok', 'banan') ro'yxati berilgan. Siz shu ro'yxatdan foydalanib, quyidagi gapni hosil qiling:
```text
Men olma, nok, banan mevalarini yaxshi ko'raman
```
23. Foydalanuvchidan bozordan nima mahsulotlar olganini so'rang. Har birini , belgisi bilan kiritsin. So'ng ularni ro'yxat hosil qiling. Keyin esa gap hosil qiling, ohirida bitta oldin va so'zi bo'lsin
```text
Bozordan nima mahsulotlar oldingiz (olma,nok formatida yozing): olma,nok,banan,bodring
Siz bozordan olma, nok, banan va bodring oldingiz
```
