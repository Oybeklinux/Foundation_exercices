# 09. Puffakchali tartiblash va ro'yxat ichida ro'yxat


<!-- TOC -->

* [Puffakchali tartiblash](#puffakchali-tartiblash)
* [Ro'yxat ichida ro'yxat](#royxat-ichida-ro--yxat)
  * [Qiymatdan foydalanish](#qiymatdan-foydalanish)
  * [Qiymat kiritish](#qiymat-kiritish)
  * [Qiymatni o'zgartirish](#qiymatni-ozgartirish)
  * [Qiymat o'chirish](#qiymat-ochirish)
  * [Ko'p o'lchamli massiv](#kop-o--lchamli-massiv)
* [Ro'yxat generatori](#royxat-generatori)
  * [Ikki o'lchamli ro'yxat generatori](#ikki-olchamli-ro--yxat-generatori)
<!-- TOC -->

### Puffakchali tartiblash
Pufakchani t, agartiblash ular to'g'ri tartibda bo'lmasa, qo'shni elementlarni almashtirishni takrorlash orqali ishlaydigan oddiy mantiqdan foydalanadi. U bir vaqtning o'zida bir juftlikni taqqoslaydi va agar birinchi element ikkinchi elementdan katta bo'lsa, almashtiradi; aks holda, taqqoslash uchun keyingi elementlar juftligiga o'tadi

Keling misol orqali tushunishga harakat qilamiz

Misol -

Biz butun sonlarni saqlaydigan elementlar ro'yxatini yaratamiz

roʻyxat1 = [5, 3, 8, 6, 7, 2]

Bu yerda algoritm elementlarni tartiblaydi -

#### Birinchi iteratsiya

> [**5**, **3**, 8, 6, 7, 2]

U dastlabki ikkita elementni taqqoslaydi va bu yerda 5>3 sababli bir-biri bilan almashtiriladi. Endi biz yangi ro'yxatni olamiz -

> [**3**, **5**, 8, 6, 7, 2]

Ikkinchi taqqoslashda, 5 < 8 sababli hech narsa o'zgarmaydi

> [3, **5**, **8**, 6, 7, 2]

Uchinchi taqqoslashda, 8>6 sababli almashtirish sodir bo'ladi, natijada ro'yxat yangilanadi:

> [3, 5, **6**, **8**, 7, 2]

To'rtinchi taqqoslashda, 8>7 sababli almashtirish sodir bo'ladi, natijada ro'yxat yangilanadi:

> [3, 5, 6, **7**, **8**, 2]

Beshinchi taqqoslashda, 8>2 sababli almashtirish sodir bo'ladi, natijada ro'yxat yangilanadi:

> [3, 5, 6, 7, **2**, **8**]

Bu erda birinchi iteratsiya tugallandi va biz oxirida eng katta elementni olamiz. Endi ikkinchi iteratsiyaga o'tamiz. Iteratsiyalar len(ro'yxat1)-1 marta davom etadi

#### Ikkinchi iteratsiya


>
> [**3**, **5**, 6, 7, 2, 8] - > [**3**, **5**, 6, 7, 2, 8] bu yerda, 3<5, o'z o'rnida qoladi
>
> [3, **5**, **6**, 7, 2, 8] - > [3, **5**, **6**, 7, 2, 8] bu yerda, 5<6, o'z o'rnida qoladi
>
> [3, 5, **6**, **7**, 2, 8] - > [3, 5, **6**, **7**, 2, 8] bu yerda, 6<7, o'z o'rnida qoladi
>
> [3, 5, 6, **7**, **2**, 8] - > [3, 5, 6, **2**, **7**, 8] bu yerda 7>2, almashtirish amalga oshiriladi
>
> [3, 5, 6, 2, **7**, **8**] - > [3, 5, 6, 2, **7**, **8**] bu yerda 7<8, o'z o'rnida qoladi

#### Uchinchi iteratsiya


>
> [**3**, **5**, 6, 2, 7, 8] - > [**3**, **5**, 6, 2, 7, 8] bu yerda, 3<5, o'z o'rnida qoladi
>
> [3, **5**, **6**, 2, 7, 8] - > [3, **5**, **6**, 2, 7, 8] bu yerda, 5<6, o'z o'rnida qoladi
>
> [3, 5, **6**, **2**, 7, 8] - > [3, 5, **2**, **6**, 7, 8] bu yerda, 6>2, almashtirish amalga oshiriladi
>
> [3, 5, 2, **6**, **7**, 8] - > [3, 5, 2, **6**, **7**, 8] bu yerda 6<7, o'z o'rnida qoladi
>
> [3, 5, 2, 6, **7**, **8**] - > [3, 5, 2, 6, **7**, **8**] bu yerda 7<8, o'z o'rnida qoladi

#### To'rtinchi iteratsiya


>
> [**3**, **5**, 2, 6, 7, 8] - > [**3**, **5**, 2, 6, 7, 8]
> 
> [3, **5**, **2**, 6, 7, 8] - > [3, **2**, **5**, 6, 7, 8]
> 
> [3, 2, **5**, **6**, 7, 8] - > [3, 2, **5**, **6**, 7, 8]
> 
> [3, 2, 5, **6**, **7**, 8] - > [3, 2, 5, **6**, **7**, 8]
> 
> [3, 2, 5, 6, **7**, **8**] - > [3, 2, 5, 6, **7**, **8**]
> 

#### Beshinchi iteratsiya

> [**3**, **2**, 5, 6, 7, 8] - > [**2**, **3**, 5, 6, 7, 8]
> 

#### Python kodida amalga oshirish

Biz puffakchali tartiblash texnikasini tasvirlab berdik. Endi biz bu mantiqni Pythonda amalga oshiramiz

Bitta sonni hammasi bilan solishtirish


Kod:

```python
list1 = [5, 3, 8, 6, 7, 2]
print("Tartiblanmagan ro'yxat: ", list1)

# list1 ichida har juft sonlarni solishtir
for j in range(len(list1) - 1):
    # agar birinchi element keyingisidan katta bo'lsa
    if list1[j] > list1[j + 1]:
        # ikki elementni joyini o'zaro almashtirish
        list1[j], list1[j + 1] = list1[j + 1], list1[j]

print("Tartiblangan ro'yxat: ", list1)
```

Natija:

```text
Tartiblanmagan ro'yxat:  [5, 3, 8, 6, 7, 2]
Tartiblangan ro'yxat:  [3, 5, 6, 7, 2, 8]
```

Bu yerda har juft sonlarni solishtirib, almashish natijasida eng katta sonni, ya'ni 8 eng ohiriga joylashdi
Endi bu takrorlashni len(list1)-1 marta bajarsak, hamma sonlar taritbli bo'ladi

Kod:
```python
list1 = [5, 3, 8, 6, 7, 2]
print("Tartiblanmagan ro'yxat: ", list1)

# len(list1)-1 marta takrorla
for i in range(0, len(list1) - 1):
    # list1 ichida har juft sonlarni solishtir
    for j in range(len(list1) - 1):
        # agar birinchi element keyingisidan katta bo'lsa
        if list1[j] > list1[j + 1]:
            # ikki elementni joyini o'zaro almashtirish
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print("Tartiblangan ro'yxat: ", list1)
```

Natija:
```text
Tartiblanmagan ro'yxat:  [5, 3, 8, 6, 7, 2]
Tartiblangan ro'yxat:  [2, 3, 5, 6, 7, 8]
```

Endi kodimizni optimallashtiramiz

```python
list1 = [5, 3, 8, 6, 7, 2]
print("Tartiblanmagan ro'yxat: ", list1)

'''
almashdi - almashish sodir bo'lgani bilish uchun ishlatiladi
siklga kirish uchun True beramiz
'''
almashdi = True
# almashdi = False bo'lguncha takrorla
while almashdi:
    #  almashish sodir bo'lgani bilish uchun avval False qilib olamiz
    almashdi = False
    # list1 ichida har juft sonlarni solishtir
    for j in range(len(list1) - 1):
        # agar birinchi element keyingisidan katta bo'lsa
        if list1[j] > list1[j + 1]:
            # ikki elementni joyini o'zaro almashtirish
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
            # almashish sodir bo'ldi
            almashdi = True

print("Tartiblangan ro'yxat: ", list1)
```

Agar ichki for siklda bir marta to'liq takrorlanganib, hech qanday almashish yuzaga kelmasa, u holda sonlar tartiblangan bo'ladi. Unda keyingi tashqi siklni davom etishga hojat qolmaydi. Bu holatda sikldan chiqib ketish kodni optimallashishiga olib keladi
Shuning uchun biz qo'shimcha  almashdi o'zgaruvchisini ishlatdik

Avval almashdi = True qilganimizni sababi while sikliga kirib olishi uchun
Har gal for sikliga kirishdan avval uni almashdi = False qilamiz, sababi undan keyin True bo'ldimi yo'qmi shuni bilish uchun uni False ga tenglab olish zarur

Agar bir marta for sikli takrorlanganda biron marta almashish yuzaga kelmasa, u holda almashdi=False bo'ladi, natijada while sikli shart bajarilmaydi va sikldan chiqib ketadi


Vazifa:
Puffakchali tartiblashning ikki hil usulini ko'rdik: optimallashmagan va optimallashgan
Optimallashgan misolni takrorlanishlar sonini kam bo'layotganini ko'rsatib bering:

1. Ikkila kodni yozing
2. Shunda optimallashmagan kodni ishga tushirganda takrorlanishlar qancha bo'lganini ekranga chiqaring
3. Keyin optimallashgan kodni ishga tushirgib takrorlanishlar soni kamayganini ko'rsating


### Ro'yxat ichida ro'yxat

Ikki o'lchovli massiv massiv ichidagi massivdir. Bu massivlar massivi. Ushbu turdagi massivda ma'lumotlar elementining pozitsiyasi bitta indeks o'rniga ikkita indeks bilan ifodalanadi. Shunday qilib, u qatorlar va ustunlardan iborat bo'lgan jadvalni ifodalaydi.

Ikki o'lchovli massivning quyidagi misolida, har bir massiv elementining o'zi ham massiv ekanligini kuzating.

Har kuni kuniga 4 marta haroratni qayd etish misolini ko'rib chiqing. 4 kunlik bunday ma'lumotlar quyidagi kabi ikki o'lchovli massiv sifatida taqdim etilishi mumkin.

```text
Kun 1 - 11 12 5 2 
Kun 2 - 15 6 10 1
Kun 3 - 10 8 12 5 
Kun 4 - 12 15 8 6 
```

Yuqoridagi ma'lumotlar quyidagi kabi ikki o'lchovli massiv sifatida taqdim etilishi mumkin.

```python
kunlar = [
    [11, 12, 5, 2], 
    [15, 6, 10, 1], 
    [10, 8, 12, 5], 
    [12, 15, 8, 6]
]
```

#### Qiymatdan foydalanish
Tasavvur qiling bizda 4 kunlik ma'lumot bor. Har kuni 4 marta harorat o'lchanadi
- 0 - 6 vaqt oralig'idagi harorat (ertalabki)
- 6 - 12 vaqt oralig'idagi harorat (kunduzgi)
- 12 - 18 vaqt oralig'idagi harorat (tush payti)
- 18 - 24 vaqt oralig'idagi harorat (kechki payt)

Kod:
```python

kunlar = [[11, 12, 5, 2], [15, 6,10,1], [10, 8, 12, 5]]

# 1-kundagi haroratlar
print(kunlar[0])
# 2-kundagi tush paytidagi harorat
print(kunlar[1][2])
```

Natija:

```text
[11, 12, 5, 2]
10
```

Hamma elementlarni chiqarish

Kod:
```python
kunlar = [[11, 12, 5, 2], [15, 6,10, 1], [10, 8, 12, 5]]
for haroratlar in kunlar:
   for harorat in haroratlar:
      print(harorat,end = "\t ")
   print()
```

Natija:
```text
11	 12	 5	 2	 
15	 6	 10	 1	 
10	 8	 12	 5
```

#### Qiymat kiritish

4-kun haroratlarini kiritaylik

Kod:
```python
kunlar = [[11, 12, 5, 2], [15, 6,10, 1], [10, 8, 12, 5]]

#keyingi kun haroratlarini kiritish
kunlar.append([5, 11, 13, 6])

for haroratlar in kunlar:
   for harorat in haroratlar:
      print(harorat,end = "\t ")
   print()
```

Natija:
```text
11	 12	 5	 2	 
15	 6	 10	 1	 
10	 8	 12	 5	 
5	 11	 13	 6
```

#### Qiymatni o'zgartirish

2-kun tushlik payti 20 ga o'zgartiramiz

```python
kunlar = [[11, 12, 5, 2], [15, 6,10, 1], [10, 8, 12, 5]]

# 2-kun tushlik payti 20 gradus bo'lsin
kunlar[1][2] = 20

for haroratlar in kunlar:
   for harorat in haroratlar:
      print(harorat,end = "\t ")
   print()
```

Natija:
```text
11	 12	 5	 2	 
15	 6	 20	 1	 
10	 8	 12	 5
```

#### Qiymat o'chirish

Ohirgi kunni o'chiramiz

Kod:
```python
kunlar = [[11, 12, 5, 2], [15, 6,10, 1], [10, 8, 12, 5]]

# ohirgi kun o'chirilsin
del kunlar[-1]

for haroratlar in kunlar:
   for harorat in haroratlar:
      print(harorat,end = "\t ")
   print()
```

Natija:
```text
11	 12	 5	 2	 
15	 6	 10	 1
```

Vazifa:
1. Mehmonhona binosida 5 qavat bor. Har qavatda alohida 3 honadon bor. Qaysi hona bo'sh yoki bo'sh emasligini saqlovchi **honadonlar** nomli massiv yarating. Avvaliga hammasi bo'sh bo'lsin. 
Keyin 4 qavatda 3 honani kelayotgan mehmon uchun band qiling. 
Keyin 5 qavatda futbol jamoasi uchun hamma honadonni band qiling
Keyin natijani ekranga chiqaring

Natija:
```text
Avvalgi holat
False	False	False	
False	False	False	
False	False	False	
False	False	False	
False	False	False	


Keyingi holat
False	False	False	
False	False	False	
False	False	False	
False	False	True	
True	True	True
```

2. Yuqoridagi masalaga ozgina o'zgartirish qiling. True va False so'zlarini o'rniga **band** va **bo'sh** so'zlari bilan chiqaring. if ni qisqa ko'rinishidan foydalaning

Natija:
```text
Avvalgi holat
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	


Keyingi holat
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	bo'sh	
bo'sh	bo'sh	band	
band	band	band
```
#### Ko'p o'lchamli massiv
Huddi shunday 3,4,5 .. va hak n o'lchamli massivlar bo'lishi mumkin. 

Faraz qiling binolar soni 3 ta. Har bino 5 qavatdan, har bir qavatda 3 honadondan iborat. U holda bu honalarnind band yoki bo'sh ekanligini saqlash uchun bizga 3 o'lchamli massiv kerak bo'ladi.
O'ylab ko'ring buni qanday qilamiz. Bu vazifani o'zingiz yozib ko'ring. Hammasining qiymati False bo'lgan **binolar** nomli 3 o'lchamli massiv yarating

### Ro'yxat generatori

Ro'yxat generatori qoidasi 1:
```text
yangi_royxat = [ ifoda/element for element in royxat if shart ]
```

Misol 1. Ro'yxatdan elementlarni ko'chirib, yangi ro'yxat yaratish

Kod:
```python
# Sikl bo'ylab takrorlash uchun ro'yxat generatoridan foydalanish
royxat = [element for element in [1, 2, 3]]
 
# Roʻyxatni  koʻrsat
print(royxat)
```

Natija:
```text
[1, 2, 3]
```

Misol 2. Roy'xatdan (0-10 orasidagi sonlar) faqat juftlarini ko'chirib, yangi ro'yxat yaratish

Kod:
```python
royxat = [i for i in range(11) if i % 2 == 0]
print(royxat)
```

Natija:

```text
[0, 2, 4, 6, 8, 10]
```

Vazifa:
1. Ro'yxat generatori yordamida 0-10 oraliqdagi sonlar kvadratlaridan iborat ro'yxat yarating

Natija:
```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

2. Ro'yxat generatori yordamida 0-10 oraliqdagi **toq sonlar** kubidan iborat ro'yxat yarating

Natija:
```text
[1, 27, 125, 343, 729]
```

3. Quyidagi **fruits** ro'yxatida mevalar saqlanadi. Sizning vazifa tarkibida **n** harfi mavjud bo'lgan meva nomalridan tuzilgan yangi ro'yxat yaratib, ekranga chiqarish
Nartija:

```text
['apple', 'banana', 'mango']
```


Ro'yxat generatori qoidasi 2:

```text
[ifoda/element if shart else ifoda/element for element in royxat]
```

Misol. 0-10 oraliqdagi sonlardan juftini kvadratga, qolganini 3-darajaga oshirib, yangi ro'yxat hosil qiling

Kod:
```python
royxat = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(11) ]
print(royxat)
```

Natija:
```text
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100]
```

Vazifa: 
1. 1-10 orasidagi sonlarni 3 ga karralik sonlarni True qolganini esa False qilib chiqaring
Natija:
```text
Ro'yxat [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Yangi ro'yxat [False, False, True, False, False, True, False, False, True, False]
```

#### Ikki o'lchamli ro'yxat generatori

```python
# 3 qator va 3 ustundan iborat jadval kabi ro'yxat yaratish
royxat = [[int(f"{i}{j}") for i in range(3)] for j in range(3)]
print(royxat)
```

Vazifa:
1. Quyidagi ikki o'lchamli massivni ro'yxat generatori yordamida yarating:

```text
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

2. Endi yuqoridagi masalani ro'yxat generatori yordamida bajaramiz. 
Mehmonhona binosida 5 qavat bor. Har qavatda alohida 3 honadon bor. Avvliga hamma elementlari False bo'lgan **honadonlar** nomli massiv yarating.  
Keyin 4 qavatda 3 honani kelayotgan mehmon uchun band qiling. 
Keyin 5 qavatda futbol jamoasi uchun hamma honadonni band qiling
Keyin natijani ekranga chiqaring

3. Ro'yxat generatori yordamida quyidagi ikki o'lchamli massivni yarating

```text
[[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]]
```

4. Quyidagi kodni tahlil qilib, o'rganib chiqing. Nima ish qilyapti?

Matritsani transponirlash:

```python
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

print(f"Matritsa: {matrix}")

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(f"Transponirlangan matritsa: {transposed}")
```

Natija:
```text
Matritsa: [[1, 2, 3, 4], [4, 5, 6, 8]]
Transponirlangan matritsa: [[1, 4], [2, 5], [3, 6], [4, 8]]
```

5. Shu kodni ro'yxat generatori yordamida qayta yozing
