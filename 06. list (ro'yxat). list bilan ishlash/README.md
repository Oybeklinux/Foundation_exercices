# 06. Ro'yxat (list) bilan ishlash
 
**Reja:**

<!-- TOC -->
* [](#06-royxat--list--bilan-ishlash)
    * [Qayatirish](#qayatirish)
    * [1 Ro'yxatdan foydalanish](#1-royxatdan-foydalanish)
      * [1.1 Elementidan foydalanish](#11-elementidan-foydalanish)
      * [1.2 Ro'yxatni kesish](#12-royxatni-kesish)
    * [2 O'zgartirish](#2-ozgartirish)
    * [3 Qo'shish](#3-qoshish)
    * [4 O'chirish](#4-ochirish)
    * [5 for - hammasini ko'rish](#5-for---hammasini-korish)
    * [6 Tartiblash](#6-tartiblash)
    * [7 Ko'chirish](#7-kochirish)
    * [8 Formatlash](#8-formatlash)
  

<!-- TOC -->

### Qayatirish

sonlar = [2, 10, 3, 11, 4, 12]

| №   | Mavzular               | Misol                                                                                                                                             | sonlar qiymati                                                                                                                                                                                               | Natija                                                                                                                                                                                                     |
|-----|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Ro'yxatdan foydalanish | sonlar[0] <br/> sonlar[-1]<br/>  sonlar[:2]<br/> sonlar[3:]                                                                                       | [2, 10, 3, 11, 4, 12] <br/>[2, 10, 3, 11, 4, 12] <br/> [2, 10, 3, 11, 4, 12]<br/> [2, 10, 3, 11, 4, 12]                                                                                                      | 2<br/>12<br/>  [2, 10]<br/>  [11, 4, 12]                                                                                                                                                                   |
| 2   | O'zgartirish           | sonlar[0] = 100<br/> sonlar[0:1] = [100, 200] <br/>sonlar[0:4] = [1]                                                                              | [2, 10, 3, 11, 4, 12] <br/>[2, 10, 3, 11, 4, 12] <br/> [2, 10, 3, 11, 4, 12]                                                                                                                                 | [100, 10, 3, 11, 4, 12]<br/>[100, 200, 10, 3, 11, 4, 12]<br/> [1, 4, 12]                                                                                                                                   | 
| 3   | Qo'shish               | sonlar.append(100)<br/> sonlar.insert(0,100)<br/>  sonlar.extend([100,200])<br/> sonlar = sonlar + [100,200]                                      | [2, 10, 3, 11, 4, 12] <br/>[2, 10, 3, 11, 4, 12] <br/> [2, 10, 3, 11, 4, 12]<br/> [2, 10, 3, 11, 4, 12]                                                                                                      | [2, 10, 3, 11, 4, 12, 100] <br/> [100, 2, 10, 3, 11, 4, 12] <br/>  [2, 10, 3, 11, 4, 12, 100, 200] <br/> [2, 10, 3, 11, 4, 12, 100, 200]                                                                   |
| 4   | O'chirish              | sonlar.remove(10)<br/> sonlar.pop()<br/> sonlar.pop(2)<br/> del sonlar[2]  <br/>del sonlar                                                        | [2, 10, 3, 11, 4, 12] <br/>[2, 10, 3, 11, 4, 12] <br/> [2, 10, 3, 11, 4, 12]<br/> [2, 10, 3, 11, 4, 12] <br/> [2, 10, 3, 11, 4, 12]                                                                          | [2, 3, 11, 4, 12]<br/> [2, 10, 3, 11, 4]<br/> [2, 10, 11, 4, 12]<br/>[2, 10, 11, 4, 12] <br/> sonlar o'zgaruvchisi xotiradan o'chib ketadi                                                                 |
| 5   | for tsikli             | for son in sonlar:<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(son)                                                                                         | [2, 10, 3, 11, 4, 12]                                                                                                                                                                                        | 2<br>10<br>3<br>11<br>4<br>12                                                                                                                                                                              |

#### Tartiblash
sonlar = [2, 10, 3, 11, 4, 12]
ismlar = ['anvar', 'Bekzod', 'bobur', 'Akmal', 'Jasur']
shaharlar = ['Toshkent', 'Xiva', 'Qarshi', 'Andijon']

| Misollar                   | Natija                                         | Tavsif                            |
|----------------------------|------------------------------------------------|-----------------------------------|
| sonlar.sort()              | [2, 3, 4, 10, 11, 12]                          | Sonlarni tartiblash               |     
| sonlar.sort(reverse=True)  | [12, 11, 10, 4, 3, 2]                          | Teskari tartiblash                |
| ismlar.sort()              | ['Akmal', 'Bekzod', 'Jasur', 'anvar', 'bobur'] | Alfavit bo'yicha tartiblash       |
| ismlar.sort(key=str.lower) | ['Akmal', 'anvar', 'Bekzod', 'bobur', 'Jasur'] | Registrga qaramasdan tartiblash   |
| shaharlar.sort(key=len)    | ['Xiva', 'Qarshi', 'Andijon', 'Toshkent']      | So'z uzunligi bo'yicha tartiblash |

#### Ko'chirish
sonlar1 = [2, 10]

| Misollar                                       | sonlar1   | sonlar2   | Tavsif                                         |
|------------------------------------------------|-----------|-----------|------------------------------------------------|
| sonlar2 = sonlar1<br/> sonlar2[0] = 100        | [100, 10] | [100, 10] | son2 son1 dan nusha olmaydi, (xotirada yagona) |
| sonlar2 = sonlar1.copy()<br/> sonlar2[0] = 100 | [2, 10]   | [100, 10] | son2 son1 dan nusha oldi, (xotirada alohida)   |
| sonlar2 = sonlar1[:]<br/> sonlar2[0] = 100     | [2, 10]   | [100, 10] | son2 son1 dan nusha oldi, (xotirada alohida)   |
| sonlar2 = list(sonlar1)<br/> sonlar2[0] = 100  | [2, 10]   | [100, 10] | son2 son1 dan nusha oldi, (xotirada alohida)   |

 #### Formatlash
sonlar1 = [2, 10]
shaharlar = ['Toshkent', 'Xiva', 'Qarshi', 'Andijon']

| Misol             | Natija                                        |
|-------------------|-----------------------------------------------|
| ', '.join(sonlar) | XATO. Ro'yxat elementlari satr bo'lishi kerak |
| ','.join(ismlar)  | Toshkent,Xiva,Qarshi,Andijon                  |
| '#'.join(ismlar)  | Toshkent#Xiva#Qarshi#Andijon                  |



### 1 Ro'yxatdan foydalanish
Python dasturlash tilida 4 xil massivlar mavjud:
- [List](README.md)
- [Tuple](../05.%20tuple%20(o'zgarmas%20ro'yxat).%20tuple%20bilan%20ishlash)
- [Set](../06.%20set%20(to'plam).%20set%20bilan%20ishlash)
- [Dict](../07.%20dict%20(lug'at).%20dict%20bilan%20ishlash)
<br>Massiv - bitta o'zgaruvchida bir nechta elementlarni saqlash uchun ishlatiladi<br>

1. Bo'sh ro'yxatni e'lon qiling:

Kod:

```python
royxat = []
```
yoki
```python
royxat = list()
```
2. (1-10) sonlarni saqlovchi ro'yxatni e'long qiling:

Kod:

```python
royxat = [1,2,3,4,5,6,7,8,9,10]
```
3. (a-z) harflarni saqlovchi ro'yxat e'lon qiling:

Kod:

```python
alfavit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
```
4. Ro'yxatda nechta son bor?

Kod:

```python
royxat = [1,2,3,4,5]
print(f"Ro'yxat uzunligi: {len(royxat)}")
```

Natija:

```text
Ro'yxat uzunligi: 5
```

5. Ro'yxat e'lon qiling unga element sifatida, 34, True, 'so"z', [1,2,3], (4,5,6) kabi sodda va murakkab bo'lgan qiymatlarni o'zlashtiring

Kod:

```python
sonlar = [1,2,3,4,5]
harflar = ['a','b','c']
sozlar = ['olma', 'nok', 'anor']
royxatlar = [[1,2,3], [4,5,6], [7,8,9]]
lugatlar = [{"car": "moshina"}, {"pencil": "qalam"}]
ozgarmas_royxatlar = [(10,20,30), (40,50,60)]
mantiqiy = [True, False, True]
aralash = [1,'a', True,[1,2,3], {'car':'moshina'}, ('oq', 'yashil')]
```

6. Ro'yxat e'lon qiling, so'ng uni ma'lumot turini yozing:

Kod:

```python
sonlar = [1,2, 3]
print(type(sonlar))
```

Natija:
```text
<class 'list'>
```
Royxatning har bir elementi ma'lum pozitsiyada joylashgan  bo'ladi. U pozitsiya - indeks deyiladi. Indeks orqali biz ro'yxatning elementini olamiz
<br>
![](images/img_1.png)
<br>
<li>Musbat indeks - chapdan o'ngga qarab 0 dan boshluvchi son: 0,1,2,3, ..</li>
<li>Manfiy indeks - o'ngdan chapga qarab -1 boshlanuvchi son: -1,-2,-3,-4, ..</li>
<br>

#### 1.1 Elementidan foydalanish

7. Ro'yxatdan ikkinchi elementni ekranga chiqaring:

```python
harflar = ['d','a','s','t','u','r','c','h','i']
print(f"Ikkinchi harf: {harflar[1]}")
#harflar[2] emas
```
```text
Ikkinchi harf: a
```
8. Ro'yxatdan birinchi va ohirgi elementni chiqaring:
```python
harflar = ['d','a','s','t','u','r','c','h','i']
print(f"Birinchi harf: {harflar[0]}")
print(f"Ohirgi harf: {harflar[-1]}")
```
```text
Birinchi harf: d
Ohirgi harf: i
```

#### 1.2 Ro'yxatni kesish

9. Ro'yxatdan 70,30,20,90 elementlarni qirqib oling, so'ng ekranga chiqaring:
```python
harflar = [50,70,30,20,90,10,50]
bazi_harflar = harflar[1:5]
print(bazi_harflar)
```
```text
[70, 30, 20, 90]
```
*Izoh:*<br>
Ro'yxatyda 70 ikkinchi son, lekin indeks 0 dan boshlangani uchun, boshlanish indeksga 2 emas 1 beramiz. 90 5-o'rinda, indesk bo'yicha 4-o'rinda, lekin tugash indeksidagi elementni o'zini hisobga olmagani uchun biz 6 ni beramiz.
<br>
![](images/img.png)

10. Ro'yxat boshidan 4, ohiridan 4 elementni qirqib, ekranga chiqaring
```python
harflar = [50,70,30,20,90,10,50]
bosh_harflar = harflar[:4]
ohirgi_harflar = harflar[-4:]
print(f"Boshidagi 4 harf: {bosh_harflar}")
print(f"Ohiridagi 4 harf: {ohirgi_harflar}")
```
*Izoh:*<br>
Boshidan qirqib oladigan bo'lsa, boshidagi 0 indeksni bermasak ham bo'ladi.<br>
Ohiridan qirqadigan bo'lsak, ohiridagi indeksni bermaymiz<br>
11. Sizda bozorlik ro'yxati bor. Ro'yxatda foydalanuvchi kiritgan mahsulot bozorlik ro'yxatida borligini aniqlang: 

```python
bozorlik = ['olma', 'nok', 'sabzi']
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
12. Foydalanuvchi siz belgilagan formatda bir qancha mahsulotlarni kiritsin. So'ng siz shulardan birinchi va ohirini chiqaring
```python
satr = input(f"olma,anor,banan ko'rinishida mahsulotlarni kiriting: ")
royxat = satr.split(",")
print(f"Birinchi mahsulot: {royxat[0]}")
print(f"Ohirgi mahsulot: {royxat[-1]}")
```
```text
olma,anor,banan ko'rinishida mahsulotlarni kiriting: bodring,pamildori,garimdori,zanjabil,ko'kat
Birinchi mahsulot: bodring
Ohirgi mahsulot: ko'kat
```

14. Foydalanuvchidan har birini orasi # belgisi bilan ajratilgan 5 son kiritishini so'rang, so'ng ular haqiqatda 5 taligini aniqlang:
```python
satr = input("Orasi # bilan ajratilgan faqat 5 son kiriting: ")
royxat = satr.split("#")
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
15. [1,2,3,5,6] ro'yxat berilgan. Birinchi elementini 10 soniga o'zgartiring. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring
```python
sonlar = [1,2,3,5,6]
print(sonlar)
sonlar[0] = 10
print(sonlar)
```
```text
[1, 2, 3, 5, 6]
[10, 2, 3, 5, 6]
```
16. [10,20,30,50,60] ro'yxat berilgan. Ikkinchi elementini shunday o'zgartirinki, o'zini ikkiga ko'paytirib natiani yozing. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```python
sonlar = [10,20,30,50,60]
print(sonlar)
sonlar[1] = sonlar[1] * 2
print(sonlar)
```
```text
[10, 20, 30, 50, 60]
[10, 40, 30, 50, 60]
```
17. [10,20,30,50,60] ro'yxat berilgan. Ikkinchi va uchinchi pozitsiyadagi qiymatlar o'rni almashib qolsin. Avvalgi va o'zgargan ro'yxatni ekranga chiqaring:
```python
sonlar = [10,20,30,50,60]
print(sonlar)
sonlar[1], sonlar[2] = sonlar[2], sonlar[1]
print(sonlar)
```
```text
[10, 20, 30, 50, 60]
[10, 30, 20, 50, 60]
```
18. ['olcha', 'olma', 'nok', 'anor'] shu yerdan olcha va olma o'rniga bodring va sabzi qiymatiga o'zgartiring. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ['olcha', 'olma', 'nok', 'anor']
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar[0] = 'bodring'
mahsulotlar[1] = 'sabzi'
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
2-usul
```python
mahsulotlar = ['olcha', 'olma', 'nok', 'anor']
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar[0:2] = ['bodring', 'sabzi']
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ['olcha', 'olma', 'nok', 'anor']
O'zgargan ro'yxat: ['bodring', 'sabzi', 'nok', 'anor']
```
19. ['olcha', 'olma', 'nok', 'anor'] shu yerdan olma va nokni chiqarib tashlab, o'rniga o'rik qiymati yozing. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ['olcha', 'olma', 'nok', 'anor']
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar[1:3] = ["o'rik"]
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ['olcha', 'olma', 'nok', 'anor']
O'zgargan ro'yxat: ['olcha', "o'rik", 'anor']
```
20. ['olcha', 'sabzi'] shu yerdan sabzi o'rniga olma, nok, anor qiymatini yozing. Asl va o'zgargan ro'yxatni ekranga chiqaring:
```python
mahsulotlar = ['olcha', 'sabzi']
print(f"Asl ro'yxat: {mahsulotlar}")
mahsulotlar[1:2] = ['olma', 'nok', 'anor']
print(f"O'zgargan ro'yxat: {mahsulotlar}")
```
```text
Asl ro'yxat: ['olcha', 'sabzi']
O'zgargan ro'yxat: ['olcha', 'olma', 'nok', 'anor']
```
### 3 Qo'shish
<ul>
<li>append(qiymat) - bitta element ro'yxat ohiriga qo'shish</li>
<li>insert(indeks, qiymat) - bitta element ro'yxatning ko'rsatilgan joyiga qo'shish</li>
<li>extend(ro'yxat) - ro'yxat elementlarini ro'yxat ohiriga qo'shish</li>
<li>+ - bu belgi bilan ikki ro'yxatni qo'shsa bo'ladi</li>
</ul>

21. ['olma', 'nok'] berilgan. Endi foydalanuvchi kiritgan mevani ro'yxat ohiriga qo'shamiz:
```python
bozorlik = ['olma', 'nok']
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Yana nimani kiritaylik: ")
bozorlik.append(meva)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ['olma', 'nok'] bor
Yana nimani kiritaylik: bodom
O'zgargan ro'yxat: ['olma', 'nok', 'bodom']
```
22. Bizda ['olma', 'nok'] bozorlik ro'yxati berilgan. Foydalnuvchi yana bir muhim mahsulotni kiritadi, uni muhim bo'lgani uchun ro'yxat boshiga kiritamiz:
```python
bozorlik = ['olma', 'nok']
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Yana bitta muhim mahsulotni kiritaylik: ")
bozorlik.insert(0, meva)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ['olma', 'nok'] bor
Yana bitta muhim mahsulotni kiritaylik: non
O'zgargan ro'yxat: ['non', 'olma', 'nok']
```
23. Bizda ['olma', 'nok'] bozorlik ro'yxati berilgan, foydalanuvchi yana bir nechta mahsulot olish kerakligi esiga tushib qoldi, shularni foydaluvchi ma'lumot formatda kiritsin so'ng, hammasini ro'yxatga qo'shib qo'ying:
```python
bozorlik = ['olma', 'nok']
print(f"Hozircha bozorlik ro'yxatida {bozorlik} bor")
meva = input("Nimalar esingizdan chiqib ketdi. ',' bilan yozing: ")
mevalar = meva.split(",")
bozorlik.extend(mevalar)
print(f"O'zgargan ro'yxat: {bozorlik}")
```
```text
Hozircha bozorlik ro'yxatida ['olma', 'nok'] bor
Nimalar esingizdan chiqib ketdi. ',' bilan yozing: o'rik,shaftoli,banan
O'zgargan ro'yxat: ['olma', 'nok', "o'rik", 'shaftoli', 'banan']
```
24. mevalar = ['olma', 'nok'] va sabzavotlar=['sabzi', 'bodring'] ro'yxatlari berilgan, ularni birlashtirib yangi ro'yxat hosil qilib, ekranga chiqaring:
```python
mevalar = ['olma', 'nok']
sabzavotlar=['sabzi', 'bodring']
mahsulotlar = mevalar + sabzavotlar
print(mahsulotlar)
```
```text
['olma', 'nok', 'sabzi', 'bodring']
```

### 4 O'chirish
- remove(qiymat) - qiymat bo'yicha o'chirish
- pop(indeks) - indeks bo'yicha o'chirish
- del element- o'zgaruvchini yoki elementini o'chirish
- clear() - ro'yxatdan hamma elementni o'chiradi

remove(qiymat)
```html
Sintaksis: 
royxat_nomi.remove(obj) 

Parametrlar:  
obj: ro'yxatdan o'chirilishi kerak bo'lgan obyekt (element) 

Qaytadi:  
Bu metoddan qiymat qaytmaydi

Xatolik:
Agar obyekt ro'yxat ichida bo'lmasa xatolik yuzaga keladi

Izoh: 
Ro'yxatda birinchi uchragan obyektni o'chiradi  
```
25. [1,2,4,5] ro'yxatidan 4 ni o'chiring:
```python
sonlar = [1,2,4,5]
print(f"Boshlang'ich holat: {sonlar}")
sonlar.remove(4)
print(f"O'zgargan holat: {sonlar}")
```
26. Foydalanuvchi kiritgan harfni ro'yxatdan o'chiring:
```python
mevalar = ['olma', 'nok', 'banan']
print(mevalar)
meva = input("Qaysi mahsulotni ro'yxatdan olib tashlash kerak: ")
mevalar.remove(meva)
print(f"O'zgargan ro'yxat: {mevalar}")
```
```text
['olma', 'nok', 'banan']
Qaysi mahsulotni ro'yxatdan olib tashlash kerak: nok
O'zgargan ro'yxat: ['olma', 'banan']
```

pop(indeks)
```html
Sintaksis: 
royxat_nomi.pop(indeks:int) 

Parametrlar:  
    - indeks(ixtiyoriy): berilgan indeks bo'yicha elementni o'chiradi. Agar indeks bo'lmasa, ohirgi elementni o'chiradi 

Qaytadi:  
O'chirilgan element 

Xatolik:
Indeks royxat indekslaridan tashqarida bo'lsa, IndexError xatolik yuzaga keladi
```
27. Ro'yxatdan  4-elementni o'chirib, ro'yxatni va o'chirilgan elementni ekranga chiqaring
```python
sonlar = [20,30,40,50,60]
print(f"Boshlang'ich holat: {sonlar}")
son = sonlar.pop(3)
print(f"O'zgargan holat: {sonlar}")
print(f"O'chirilgan element: {son}")
```
yoki
```python
sonlar = [20,30,40,50,60]
print(f"Boshlang'ich holat: {sonlar}")
son = sonlar[3]
del sonlar[3]
print(f"O'zgargan holat: {sonlar}")
print(f"O'chirilgan element: {son}")
```
```text
Boshlang'ich holat: [20, 30, 40, 50, 60]
O'zgargan holat: [20, 30, 40, 60]
O'chirilgan element: 50
```
28. Ro'yxatdan ohirgi elementni o'chiring:
```python
sonlar = [1,2,3,4,5,6]
print(f"Boshlang'ich holat: {sonlar}")
son = sonlar.pop()
print(f"O'zgargan holat: {sonlar}")
print(f"O'chirilgan element: {son}")
```
yoki 
```python
sonlar = [1,2,3,4,5,6]
print(f"Boshlang'ich holat: {sonlar}")
son = sonlar[-1]
del sonlar[-1]
print(f"O'zgargan holat: {sonlar}")
print(f"O'chirilgan element: {son}")
```
```text
Boshlang'ich holat: [20, 30, 40, 50, 60]
O'zgargan holat: [20, 30, 40, 50]
O'chirilgan element: 60
```
29. Ro'yxat elementlarini hammasini o'chiring:
```python
sonlar = [1,2,3,4,5]
print(f"Boshlang'ich holat: {sonlar}")
sonlar.clear()
print(f"O'zgargan holat: {sonlar}")
```
```text
Boshlang'ich holat: [1, 2, 3, 4, 5]
O'zgargan holat: [] 
```
### 5 for - hammasini ko'rish
30. sonlar = [1,2,3,4,5,6] ro'yxatdan hamma sonlarni quyidagi ko'rinishda chiqaring:
```text
1
2
3
4
5
6
```
```python
sonlar = [1,2,3,4,5,6]
for son in sonlar:
    print(son)
```
31. sozlar = ['dastur', 'dasturchi', 'python'] ro'xatida har bir elementi va undagi harflar sonini ekranga chiqarin:
```text
soz: dastur; uzunligi: 6
soz: dasturchi; uzunligi: 9
soz: python; uzunligi: 6
```
```python
sozlar = ['dastur', 'dasturchi', 'python']
for soz in sozlar:
    print(f"soz: {soz}; uzunligi: {len(soz)}")   
```
32. sozlar = ['dastur', 'dasturchi', 'python'] ro'yxatidan har bir elementi va undagi indeksini chiqaring:
```text
0 dastur
1 dasturchi
2 python 
```
```python
sozlar = ['dastur', 'dasturchi', 'python']
for i in range(0,3):
    print(i, sozlar[i])
```
for range lar bilan keyingi darsda batafsil ko'ramiz, hozircha esa list toifasi for da ishlarilishini bilib olishimiz yetarli
### 6 Tartiblash
33. Ro'yxatdagi ismlarni alfavit bo'yicha tartiblab bering:

```python
ismlar = ['Anvar','bekzod', 'Ravshan', 'Lola', 'Otabek']
ismlar.sort()
for ism in ismlar:
    print(ism)
```
```text
Anvar
Lola
Otabek
Ravshan
bekzod
```

34. Ro'yxatdagi sonlari tartiblab bering:

```python
sonlar = [100, 50, 200, 60, 300, 10]
sonlar.sort()
for son in sonlar:
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
35. Ballarni teskari tartiblab bering:
```python
ballar = [100, 45, 60, 55, 90, 70]
ballar.sort(reverse=True)
for bal in ballar:
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

36. Harflarni kichik kattaligini hisobga olmay tartiblang
```python
ismlar = ['Anvar','bekzod', 'Ravshan', 'Lola', 'Otabek']
ismlar.sort(key=str.lower)
for ism in ismlar:
    print(ism)
```
```text
Anvar
bekzod
Lola
Otabek
Ravshan
```

37. Satr uzunligi bo'yicha tartiblang
```python
ismlar = ['Tiko','Damas', 'Malubi', 'Lacetti']
ismlar.sort(key=len)
for ism in ismlar:
    print(ism)
```
```text
Tiko
Damas
Malubi
Lacetti
```
### 7 Ko'chirish
![](images/list_copy.png)
Quyidagi kodni ishga tushirganda hotiradan ikkita joy ajratiladi. Biri son1 uchun ikkinchisi son2 uchun. Ikkala hotirada ham 10 soni saqlanadi 
```python
son1 = 10
son2 = son1
```
list da esa (set, dict toifalarida ham) unday emas, agar biz quyidagini ishga tushirsak hotiradan ikkita ro'yxat uchun joy ajratilmaydi, aksincha bittasi uchun ajratiladi, lekin ularning nomi ikkita bo'ladi:
```python
sonlar1 = [1,2,3,4]
sonlar2 = sonlar1
sonlar2.pop()
print(sonlar1)
print(sonlar2)
```
Agar ikki ro'yxat alohida bo'lishini hohlasakchi, unda nima qilamiz? U holda biz qiymatlarini ko'chirishimiz kerak, uning bir nechta usuli bor:
- copy() metodi
- list() funksiyasi
- [:]
38. sonlar1 = [1,2,3,4] ro'yxatini ko'chirib oling, ikkinchi ro'yxatda 5 ni qo'chib qo'ying, so'ng ikkala ro'yxatni ekranga chiqaring:
```python
sonlar1 = [1,2,3,4]
sonlar2 = sonlar1.copy()
sonlar2.append(5)
print("1-ro'yxat:", sonlar1)
print("2-ro'yxat:", sonlar2)
```
yoki
```python
sonlar1 = [1,2,3,4]
sonlar2 = list(sonlar1)
sonlar2.append(5)
print("1-ro'yxat:", sonlar1)
print("2-ro'yxat:", sonlar2)
```
yoki
```python
sonlar1 = [1,2,3,4]
sonlar2 = sonlar1[:]
sonlar2.append(5)
print("1-ro'yxat:", sonlar1)
print("2-ro'yxat:", sonlar2)
```

```text
1-ro'yxat: [1, 2, 3, 4]
2-ro'yxat: [1, 2, 3, 4, 5]
```
### 8 Formatlash
**Agar elementlari str bo'lsa**, u holda ro'yxat elementlarini birlashtirish uchun join() metodini ishlatishimiz mumkin. Bu str metodi hisoblanadi:
39. Siz bozordan mevalar = ['olma', 'nok'] olgansiz. Shuni gap bilan dasturda yozishingiz kerak. Ya'ni men olma va nok oldim deb yozishingiz kerak
```python
mevalar = ['olma', 'nok']
print(f"Men bozordan {' va '.join(mevalar)} oldim")
```
```text
Men bozordan olma va nok oldim
```
40. mevalar = ['olma', 'nok', 'banan'] ro'yxati berilgna. Siz shularni har birini orasiga vergul qo'ygan holda quyidagicha gap yozishingiz kerak:
```text
olma, nok, banan mevalardir
```
```python
mevalar = ['olma', 'nok', 'banan']
print(f"{', '.join(mevalar)} mevalardir")
```
41. mevalar = ['olma', 'nok', 'banan'] ro'yxati berilgna. Siz shularni har birini orasiga vergul qo'ygan holda quyidagicha gap yozishingiz kerak:
```python
mevalar = ['olma', 'nok', 'banan']
mevalar2 = mevalar[:-1]
print(f"{', '.join(mevalar2)} va {mevalar[-1]} mevalardir")
```
```text
olma, nok va banan mevalardir
```
### min, max, sum

42. Sonlarli ro'yxat ustida quyidagilarni toping:
- Eng katta son
- Eng kichik son
- O'rta arifmetigi
- Yig'indisi

```python
sonlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
eng_kichigi = min(sonlar)
eng_kattasi = max(sonlar)
yigindisi = sum(sonlar)
ortachasi = sum(sonlar)/len(sonlar)
print(f"""
Eng kattasi: {eng_kattasi}
Eng kichigi: {eng_kichigi}
O'rtachasi: {ortachasi}
Yig'indisi: {yigindisi}""")
```

Natija:

```text
Eng kattasi: 32874
Eng kichigi: 5600
O'rtachasi: 16594.85714285714
Yig'indisi: 116164
```