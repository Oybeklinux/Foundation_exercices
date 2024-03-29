# 10. O'zgarmas ro'yxat (tuple) bilan ishlash
 
**Reja:**
<!-- TOC -->
  * [1 tuple haqida](#1-tuple-haqida)
  * [2 O'zgartirish](#2-ozgartirish)
  * [3 Element qo'shish](#3-element-qoshish)
  * [4 Element o'chirish](#4-element-ochirish)
  * [5 for - hammasini ko'rish](#5-for---hammasini-korish)
  * [6 Tartiblash](#6-tartiblash)
  * [7 Ko'chirish](#7-kochirish)
  * [8 Elementlarni formatlab chiqarish](#8-elementlarni-formatlab-chiqarish)
  * [9 Turli mavzular](#9-turli-mavzular)
<!-- TOC -->
  
###  1 tuple haqida

Tuple bilan list farqi

| № | List                        | Tuple                               |
|---|-----------------------------|-------------------------------------|
| 1 | O'zgaruvchan                | O'zgarmas                           |
| 2 | Tsiklda sekinroq            | Tsiklda tezroq                      |
| 3 | Xotiradan ko'p joy oladi    | Xotiradan kam joy oladi             |
| 4 | Metodlari ko'p              | Metodlari kam                       |
| 5 | Xatoliklar kutilishi mumkin | Xatoliklar juda kam bo'lishi mumkin |

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
### 2 O'zgartirish
___
O'zgartirish metodi mavjud emas, chunki tuple o'zgarmas ro'yxat. Lekin shunda ham uni yo'li bor, avval list ga o'girib bajariladi, so'ng qayta tuple ga o'giriladi. Odatda unday qilinmaydi. Chunki bu samarasizdir
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
### 3 Element qo'shish
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

###  4 Element o'chirish
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
### 5 for - hammasini ko'rish
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

### 6 Tartiblash
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
### 7 Ko'chirish
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
### 8 Elementlarni formatlab chiqarish
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

### 9 Turli mavzular

42. Mijozlar ismlari, shariflari va yoshlari alohida ro'yxatlarda saqlanadi. Bu mijozga tegishli ma'lumotlarni yaxlit holatda tuple ma'lumot turida saqlash kerak

```python
ismlar = ('Anvar', 'Otabek', 'Jasur', 'Bekzod')
shariflar = ('Botirov', 'Fazliddinov', 'Murodov', 'Muslimov')
yoshlar = (49, 55, 39, 33)
mijozlar = zip(ismlar, shariflar,yoshlar)

print(type(mijozlar), mijozlar)

for mijoz in mijozlar:
    print(mijoz)
```
Natija:
```text
<class 'zip'> <zip object at 0x00000229702B7CC0>
('Anvar', 'Bortirov', 49)
('Otabek', 'Fazliddinov', 55)
('Jasur', 'Murodov', 39)
('Bekzod', 'Muslimov', 33)
```

yoki

```python
ismlar = ('Anvar', 'Otabek', 'Jasur', 'Bekzod')
shariflar = ('Bortirov', 'Fazliddinov', 'Murodov', 'Muslimov')
yoshlar = (49, 55, 39, 33)
mijozlar = tuple(zip(ismlar, shariflar,yoshlar))

print(type(mijozlar), mijozlar)

for mijoz in mijozlar:
    print(mijoz)
```

Natija:

```text
<class 'tuple'> (('Anvar', 'Bortirov', 49), ('Otabek', 'Fazliddinov', 55), ('Jasur', 'Murodov', 39), ('Bekzod', 'Muslimov', 33))
('Anvar', 'Bortirov', 49)
('Otabek', 'Fazliddinov', 55)
('Jasur', 'Murodov', 39)
('Bekzod', 'Muslimov', 33)
```

43. Endi aksincha bizda mijozlarga tegishli ismi, sharifi va yoshini tegishli o'zgaruvchilarga saqlash kerak

```python
mijozlar = (('Anvar', 'Bortirov', 49), ('Otabek', 'Fazliddinov', 55), ('Jasur', 'Murodov', 39), ('Bekzod', 'Muslimov', 33))

for mijoz in mijozlar:
    ismi = mijoz[0]
    sharifi = mijoz[1]
    yoshi = mijoz[2]
    print(f"{ismi.center(10)}{sharifi.center(20)}{str(yoshi).center(10)}")
```

Natija:

```text
  Anvar         Bortirov          49    
  Otabek      Fazliddinov         55    
  Jasur         Murodov           39    
  Bekzod        Muslimov          33 
```