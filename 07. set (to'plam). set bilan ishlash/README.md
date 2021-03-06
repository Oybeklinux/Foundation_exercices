# Mavzu 7: set(to'plam). set bilan ishlash 
 
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
- sariq dev
  - [#15 LUG'AT ELEMENTLARI BILAN ISHLASH](https://python.sariq.dev/dictionary/15-dictionary-sets)
- w3schools
  - [Sets](https://www.w3schools.com/python/python_sets.asp)

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 Sintaksis](#21-sintaksis)
- [2.2 Elementlardan foydalanish](#22-elementlardan-foydalanish)
- [2.3 Element qo'shish](#23-element-qoshish)
- [2.4 Element o'chirish](#24-element-ochirish)
- [2.5 Tsiklda ishlatilishi](#25-tsiklda-ishlatilishi)
- [2.6 To'plamlarni birlashtirish](#26-toplamlarni-birlashtirish)
- [2.7 Set metodlari](#27-set-metodlari)

### 2.1 Sintaksis
```python

```
### 2.2 Elementlardan foydalanish
- To'plam - bitta o'zgaruvchida bir nechta elementlarni saqlash uchun ishlatiladi
- To'plam - tartiblanmagan (indeks mavjud emas)
- To'plamda elementni o'zgartirib bo'lmaydi, lekin element qo'shish yoki olib tashlash mumkin
- Duplikat qiymatlar bo'lmaydi
- Alohida bitta elementidan foydalanib bo'lmaydi

1. Bo'sh to'plam e'lon qilish:
```python
toplam = set()
```
2. Bo'sh bo'lmagan toplam e'lon qilish
```python
toplam = {'olma', 'nok', 'sabzi', 'nok'}
print(toplam)
```
```text
{'olma', 'nok', 'sabzi'}
```
3. To'plam uzunligini ekranga chiqarish
```python
toplam = {'olma', 'nok', 'sabzi', 'nok'}
print(f"{len(toplam)} meva bor ekan")
```
```text
3 meva bor ekan
```
4. To'plamda turli toifali ma'lumotlarni saqlash
```python
toplam1 = {'olma', 'nok', 'sabzi', 'nok'}
toplam2 = {2,3,4,5,4,2}
toplam3 = {True, False, True, False}
print(f"1-to'plam:{toplam1} uzunligi {len(toplam1)}")
print(f"2-to'plam:{toplam2} uzunligi {len(toplam2)}")
print(f"3-to'plam:{toplam3} uzunligi {len(toplam3)}")
```
```text
1-to'plam:{'olma', 'nok', 'sabzi'} uzunligi 3
2-to'plam:{2, 3, 4, 5} uzunligi 4
3-to'plam:{False, True} uzunligi 2
```
5. Aralash toifali ma'lumotlarni saqlash
```python
toplam = {1,2,3,3,True, True, "a", "b", "a","a"}
print(f"To'plam:{toplam} uzunligi {len(toplam)}")
```
```text
To'plam:{1, 2, 3, 'a', 'b'} uzunligi 5
```
6. To'plamga o'girish (konvertatsiya)
```python
# int -> set. XATO
# toplam = set(1) 
# None -> set. XATO
# toplam = set(None)
# bool -> set. XATO
# toplam = set(False) 
# float -> set. XATO
# toplam = set(1.3)
# str -> set
toplam_str = set("123")  #{'2', '3', '1'}
# list -> set
toplam_list = set([1,2,3]) #{1, 2, 3}
# tuple -> set
toplam_tuple = set((1,2,3)) #{1, 2, 3}
# dict -> set
toplam_dict = set({"olma": 5000, "nok": 10_000, "banan": 20_000}) #{'olma', 'banan', 'nok'}
print(f"str -> set: {toplam_str}")
print(f"list -> set: {toplam_list}")
print(f"tuple -> set: {toplam_tuple}")
print(f"dict -> set: {toplam_dict}")
```
```text
str -> set: {'2', '3', '1'}
list -> set: {1, 2, 3}
tuple -> set: {1, 2, 3}
dict -> set: {'olma', 'banan', 'nok'}
```
7. Hamma elementlarni ekranga chiqarish
```python
mevalar = {'olma', 'nok','banan'}
for meva in mevalar:
    print(meva)
```
8. {'olma', 'nok','banan'} to'plami berilgan. Birichi elementini chiqaring
To'plamda tartib yo'q, shuning uchun biz faqat tsiklda birinchi uchragan elementni chiqarishimiz mumkin
```python
mevalar = {'olma', 'nok','banan'}
for meva in mevalar:
    print(meva)
    break
```
```text
olma
```
9. To'plamdan ohirgi elementni chiqarish
```python
mevalar = {'olma', 'nok','banan'}
i = 0
for meva in mevalar:
    i = i + 1
    if len(mevalar) == i:
        print(i, meva)
        break
```
```text
3 nok
```
Agar to'plamda tartib bo'lganida edi, u holda nok emas banan yozuvi chiqar edi, to'plamda tartib bo'lmagani uchun biz qaysi element qayerda joylashganini bila olmaymiz<br>
10. Element to'plamda mavjudligini tekshirish
```python
mevalar = {'olma', 'nok','banan'}
print("banan" in mevalar)
```
```text
True
```
11. To'plamdagi olma ni anorga almashtiring
```python
mevalar = {'olma', 'nok','banan'}
print(f"Boshlang'ich holati: {mevalar}")
mevalar = list(mevalar)
index = mevalar.index('olma')
mevalar[index] = 'anor'
mevalar = set(mevalar)
print(f"O'zgargan holati: {mevalar}")
```
```text
Boshlang'ich holati: {'olma', 'banan', 'nok'}
O'zgargan holati: {'banan', 'nok', 'anor'}
```
### 2.3 Element qo'shish
Elementlarni qo'shish ikki metod yordamida amalga ochiriladi:
- add(element)
- update(set)
<br>

12. {1,2,3,4} to'plamiga 5,6 sonini qo'shish

```python
sonlar = {1,2,3,4}
sonlar.add(5)
sonlar.add(6)
print(sonlar)
```
yoki

```python
sonlar = {1,2,3,4}
sonlar = sonlar | {5,6}
print(sonlar)
```
13. Quyida ikki kun davomida kelgan mevalar ro'yxati berilgan *(kun1_mevalar, kun2_mevalar)*. Siz ikki kun davomida kelgan hamma mevalarni qaytarilmagan holda ro'yxatini ekranga chiqaring
```python
kun1_mevalar = ['olma','qulupnay', 'nok'] 
kun2_mevalar = ['banan', 'olma', 'nok']
hammasi = set(kun1_mevalar + kun2_mevalar)
print(f"2 kun davomida kelgan mevalar ro'yxati: {hammasi}")
```
```text
2 kun davomida kelgan mevalar ro'yxati: {'olma', 'banan', 'nok', 'qulupnay'}
```
14. {10,20,30,40} to'plamini {50, 60, 70, 80} to'plami bilan birlashtiring
```python
sonlar1 = {10,20,30,40}
sonlar2 = {50, 60, 70, 80}
sonlar1.update(sonlar2)
print(f"sonlar1: {sonlar1}")
print(f"sonlar2: {sonlar2}")
```
yoki
```python
sonlar1 = {10,20,30,40}
sonlar2 = {50, 60, 70, 80}
sonlar1 = sonlar1 | sonlar2
print(f"sonlar1: {sonlar1}")
print(f"sonlar2: {sonlar2}")
```
Natija bir hil bo'ladi
```text
sonlar1: {70, 40, 10, 80, 50, 20, 60, 30}
sonlar2: {80, 50, 60, 70}
```
15. {1,3,5,7} toq sonlar to'plamiga {2,4,6,8} juft sonlar to'plamini qo'shing
```python
sonlar = {1,3,5,7}
juft_sonlar = {2,4,6,8}
sonlar.update(juft_sonlar)
print(f"Toq va juft sonlar: {sonlar}")
```
```text
Toq va juft sonlar: {1, 2, 3, 4, 5, 6, 7, 8}
```
### 2.4 Element o'chirish
Elementni o'chirish bo'yicha quyidagi metodlar mavjud:
- remove(element) - qiymat qaytarmaydi, elementni topsa o'chiradi, aks holda xatolik beradi
- discard(element) - o'chiradi, agar mavjud bo'lmasa xatolik bermaydi
- del - to'plamni to'lig'icha o'chiradi
- clear() - hamma elementlarni o'chiradi, ya'ni bo'shatib qo'yadi
- pop() - ohirgi elementni o'chiradi

16. Bizda ikki savat bor. Birida {'ruchka','qalam', "o'chirg'ich", "chizg'ich"} bo'lsa, ikknchisida {'ruchka','qalam','daftar', 'kitob', 'papka'} kabilar bor.  Umuman olganda bizda qanday o'quv qullari mavjud?
```python
savat1 =  {'ruchka','qalam', "o'chirg'ich", "chizg'ich"} 
savat2 =  {'ruchka','qalam','daftar', 'kitob', 'papka'}
savat = savat1 | savat2
print(f"Bizda {savat} mahsulotlari bor")
```
```text
Bizda {'qalam', 'ruchka', 'papka', 'daftar', "o'chirg'ich", 'kitob', "chizg'ich"} mahsulotlari bor
```
17. {1,2,3,4,5, "olma"} ortiqcha elementni o'chirib tashlang?
```python
sonlar = {1,2,3,4,5, "olma"}
sonlar.remove("olma")
print(sonlar)
```
yoki
```python
sonlar = {1,2,3,4,5, "olma"}
sonlar.discard("olma")
print(sonlar)
```
18. discard bilan removeni farqini tushunish uchun bitta misol ko'ramiz
```python
sonlar = {1,2,3,4,5,6}
sonlar.remove(7)
```
```text
Traceback (most recent call last):
  File "<input>", line 2, in <module>
KeyError: 7
```
```python
sonlar = {1,2,3,4,5,6}
sonlar.discard(7)
```
19. {1,2,3,4,10} to'plamidan ohirgi elementni o'chirib, o'chirilgan elementni ekranga chiqaring:
```python
sonlar = {1,2,3,4,10}
son = sonlar.pop()
print(f"O'chirilgan son: {son}")
```
```text
O'chirilgan son: 1
```
20. To'plamni o'chirmasdan elementlarini o'chirish
```python
sonlar = {1, 2, 3, 4}
print(f"Sonlar: {sonlar}. Uzunligi: {len(sonlar)}")
sonlar.clear()
print(f"Elementlar o'chirldi\nSonlar: {sonlar}. Uzunligi: {len(sonlar)}")
```
21. To'plamni o'chirish
```python
sonlar = {1, 2, 3, 4}
print(f"Sonlar: {sonlar}. Uzunligi: {len(sonlar)}")
del sonlar
# Quyidagi kod xato, chunki sonlar xotiradan o'chirildi
# print(sonlar)
```
### 2.5 Tsiklda ishlatilishi
22. {1,2,3,4,5} to'plamdagi har bir elementni alohida qatorda chiqaring:
```python
toplam = {1,2,3,4,5}
for son in toplam:
    print(son)
```
```text
1
2
3
4
5
```
23. {1,2,3,4,5} to'plamdagi har bir elementni alohida qatorda ikkiga ko'paytirib chiqaring:
```python
toplam = {1,2,3,4,5}
for son in toplam:
    print(son * 2)
```
```text
1
4
6
8
10
```
24. {1,2,3,4,5} to'plamdagi har bir elementni ikkiga ko'paytirib, boshqa to'plamni hosil qiling, so'ng ekranga chiqaring:
```python
toplam = {1,2,3,4,5}
toplam_2 = set()

for son in toplam:
    toplam_2.add(son * 2)
print(f"Birinchi to'plam: {toplam}")
print(f"Ikkinchi to'plam: {toplam_2}")
```
```text
Birinchi to'plam: {1, 2, 3, 4, 5}
Ikkinchi to'plam: {2, 4, 6, 8, 10}
```
### 2.6 To'plamlarni birlashtirish
To'plamga [elementni qo'shishni](#23-element-qoshish) ko'rib o'tdik. Endi to'plamlarni birlashtirishni ko'rib o'tamiz. To'plamlarni birlashtirish metodlari:
1. Hamma elementlarni birlashtiradigan metodlar:
- union() - bir nechta to'plamlarni birlashtirib, hosil bo'lgan to'plamni qaytaradi
- update() - union() metodiga o'xshash, lekin u qaytarmaydi, balki to'plamlarni qo'shib, to'plamni o'zgartirib qo'yadi
2. Faqat dublikatlarni qoldiradigan metodlar:
- intersection_update() - hamma to'plamlarda mavjud elementlarni saqlaydi
- intersection() - hamma to'plamlarda mavjud elementlar to'plamini qaytaradi
3. Faqat farqli elementlarni qoldiradigan metodlar:
- difference_update - 1-to'plamda bor, lekin qolganlarida yo'q bo'lgan elementlarni saqlaydi  
- difference() - 1-to'plamda bor, lekin qolganlarida yo'q bo'lgan elementlarni qaytaradi
- difference_update - 1-to'plamda bor, lekin qolganlarida yo'q bo'lgan elementlarni saqlaydi  
- difference() - 1-to'plamda bor, lekin qolganlarida yo'q bo'lgan elementlarni qaytaradi
- symmetric_difference_update() - hamma to'plamda farqli bo'lgan elementlarni saqlaydi 
- symmetric_difference() - hamma to'plamda farqli bo'lgan elementlarni qaytaradi


25. {1,2,3,4,5} va {"a", "b" , "c"} to'plamlarni birlashtiring. Berilgan to'plamlarni va hosil bo'lgan to'plamni ekranga chiqaring:
```python
toplam_1 = {1,2,3,4,5}
toplam_2 = {"a", "b" , "c"}
natija = toplam_1.union(toplam_2)
print(f"1-to'plam: {toplam_1}")
print(f"2-to'plam: {toplam_2}")
print(f"Hosil bo'lgan to'plam: {natija}")
```
```text
1-to'plam: {1, 2, 3, 4, 5}
2-to'plam: {'a', 'b', 'c'}
Hosil bo'lgan to'plam: {1, 2, 3, 4, 5, 'a', 'b', 'c'}
```
26. {1,2,3,4,5}, {True, False} va {"a", "b" , "c"}  to'plamlarni birlashtiring. Berilgan to'plamlarni va hosil bo'lgan to'plamni ekranga chiqaring:
```python
toplam_1 = {1,2,3,4,5}
toplam_2 = {'olma', 'banan'}
toplam_3 = {"a", "b" , "c"}
natija = toplam_1.union(toplam_2, toplam_3)
print(f"1-to'plam: {toplam_1}")
print(f"2-to'plam: {toplam_2}")
print(f"3-to'plam: {toplam_3}")
print(f"Hosil bo'lgan to'plam: {natija}")
```
```text
1-to'plam: {1, 2, 3, 4, 5}
2-to'plam: {'olma', 'banan'}
3-to'plam: {'a', 'b', 'c'}
Hosil bo'lgan to'plam: {'olma', 1, 2, 3, 4, 5, 'a', 'b', 'c', 'banan'}
```
27. sonlar = {1,3,5,7,9} va juft_sonlar = {2,4,6,8,10} to'plamlari berilgan. sonlar to'plamiga juft_sonlar ni ham qo'shing:
```python
sonlar = {1,3,5,7,9} 
juft_sonlar = {2,4,6,8,10}
print(f"Sonlar: {sonlar}")
print(f"Juft sonlar: {juft_sonlar}")
sonlar.update(juft_sonlar)
print(f"O'zgartirilgan keyingi sonlar: {sonlar}")
```
```text
Sonlar: {1, 3, 5, 7, 9}
Juft sonlar: {2, 4, 6, 8, 10}
O'zgartirilgan keyingi sonlar: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
28. sotilgan_1kun = {'Mi', 'Sumsung'}, sotilgan_2kun = {'Sumsung'} va sotilgan_3kun = {'Apple', 'Hp'} to'plamlari berilgan. Bular 3 kun davomida sotilgan mahsulotlar tashkilotlaridir. Siz 3 kun davomida sotilgan mahsulotlar tashkilotining to'plamini hosil qiling:
```python
sotilgan_1kun = {'Mi', 'Sumsung'}
sotilgan_2kun = {'Sumsung'}
sotilgan_3kun = {'Apple', 'Hp'}
natija = sotilgan_1kun
natija.update(sotilgan_2kun, sotilgan_3kun)
print(f"3-kun davomida: {natija}")
print(f"1-kun: {sotilgan_1kun}")
print(f"2-kun: {sotilgan_2kun}")
print(f"3-kun: {sotilgan_3kun}")
```
```text
3-kun davomida: {'Hp', 'Sumsung', 'Apple', 'Mi'}
1-kun: {'Hp', 'Sumsung', 'Apple', 'Mi'}
2-kun: {'Sumsung'}
3-kun: {'Hp', 'Apple'}
```
29. {1,2,3,4,56,7,8,9,10} va {6,8,10,12,14} to'plamlari berilgan. Ikkala to'plamda ham berilgan elementlarni ekranga chiqaring:
```python
toplam1 = {1,2,3,4,56,7,8,9,10}
toplam2 = {6,8,10,12,14}
print(f"1-to'plam: {toplam1}")
print(f"2-to'plam: {toplam2}")
toplam1.intersection_update(toplam2)
print(f"Ikkalasida mavjud elementlar: {toplam1}")
```
```text
1-to'plam: {1, 2, 3, 4, 7, 8, 9, 10, 56}
2-to'plam: {6, 8, 10, 12, 14}
Ikkalasida mavjud elementlar: {8, 10}
```
30. Yuqoridag masalani qayta bajaring, faqat natijaviy to'plam alohida to'plamda saqlansin, boshlang'ich ikki to'plamga ta'sir qilmasin:
```python
toplam1 = {1,2,3,4,56,7,8,9,10}
toplam2 = {6,8,10,12,14}
natija = toplam1.intersection(toplam2)
print(f"Ikkalasida mavjud elementlar: {natija}")
print(f"1-to'plam: {toplam1}")
print(f"2-to'plam: {toplam2}")
```
```text
Ikkalasida mavjud elementlar: {8, 10}
1-to'plam: {1, 2, 3, 4, 7, 8, 9, 10, 56}
2-to'plam: {6, 8, 10, 12, 14}
```
31. a={1,2,3,4,5} va b={4,5,6,7} to'plami berilgan. Farqli elementlarni ekranga chiqaring:<br>
- a to'plamda bor , b to'plamda yo'q
- b to'plamda bor , a to'plamda yo'q
- ikkala to'plamda farqli bo'lgan elementlar
- 
```python
a = {1,2,3,4,5}
b = {4,5,6,7}

print(f"1-to'plam: {a}")
print(f"2-to'plam: {b}")
c = a.difference(b)
print(f"1-to'plamda bor, 2-to'plamda yo'q elementlar: {c}")
c = b.difference(a)
print(f"2-to'plamda bor, 1-to'plamda yo'q elementlar: {c}")
c = b.symmetric_difference(a)
print(f"Ikki to'plamda uchramaydigan elementlar: {c}")
```
```text
1-to'plam: {1, 2, 3, 4, 5}
2-to'plam: {4, 5, 6, 7}
1-to'plamda bor, 2-to'plamda yo'q elementlar: {1, 2, 3}
2-to'plamda bor, 1-to'plamda yo'q elementlar: {6, 7}
Ikki to'plamda bir paytda uchramaydigan elementlar: {1, 2, 3, 6, 7}
```
### 2.7 Set metodlari
set toifasiga tegishli yana boshqa metodlar ham bor:
- a.clear()	- a to'plamni hamma elementlarini o'chiradi
- a.copy() - a to'plamdan nusxa oladi
- a.isdisjoint(b)	- a to'plam bilan b to'plam orasida kesishmaydigan qiymatlar bo'lsa, True aks holda False qaytadi
- a.issubset(b)	- a to'plam b to'plam ichida yotsa True, ak holda False qaytadi
- a.issuperset(b) - a to'plamda b to'plam yotsa True, aks holda False qaytadi

32. a = {1,2,3,4,5} to'plamni b to'plamga o'zlashtiramiz, natijada xotiradan bir marta joy ajratilganiga guvoh bo'lamiz, faqat nomi ikkita bo'ladi
```python
a = {1,2,3,4,5}
b = a
b.add(6)
print(f"a: {a}")
print(f"b: {b}")
```
```text
a: {1, 2, 3, 4, 5, 6}
b: {1, 2, 3, 4, 5, 6}
```
33. Endi esa a = {1,2,3,4,5} to'plamdan b to'plamga nusxa oling. So'ng a to'plani elementlarini hammasini o'chirib tashlang (b to'plam a to'plamga ta'sir qilmasin):
```python
a = {1,2,3,4,5}
b = a.copy()
a.clear()
b.add(6)
print(f"a: {a}")
print(f"b: {b}")
```
```text
a: set()
b: {1, 2, 3, 4, 5, 6}
```
34. Bozorda {'olma', 'nok', 'banan', 'bodring', 'sabzi'} mahsulotlari bor. Siz {'anor', 'olma'} mahsulotlarini bozordan olmoqchisiz? Quyidagilarni aniqlang:
- Sizning ro'yxatingizdagi hamma mahsulotlarni bozorda bormi?

```python
bozor = {'olma', 'nok', 'banan', 'bodring', 'sabzi'}
print(f"Bozordagi mahsulotlar: {bozor}")
royhat = set(input("Bozordan nima olasiz? Bittada ',' bilan kiriting: ").split(","))
if bozor.issuperset(royhat):
    print("Hamma mahsulotlar bozorda bor")
else:
    if bozor.isdisjoint(royhat):
        print("Ro'yhatdagi mahsulotlarning bittasi ham bozorda yo'q")
    else:
        print("Ro'yxatdagi ba'zi mahsulotlar bozorda bor ekan")
```
```text
Bozordagi mahsulotlar: {'olma', 'nok', 'sabzi', 'banan', 'bodring'}
Bozordan nima olasiz? Bittada ',' bilan kiriting: >? olma,banan
Hamma mahsulotlar bozorda bor
```
```text
Bozordagi mahsulotlar: {'olma', 'nok', 'sabzi', 'banan', 'bodring'}
Bozordan nima olasiz? Bittada ',' bilan kiriting: >? olma,qalampir
Ro'yxatdagi ba'zi mahsulotlar bozorda bor ekan
```
```text
Bozordagi mahsulotlar: {'olma', 'nok', 'sabzi', 'banan', 'bodring'}
Bozordan nima olasiz? Bittada ',' bilan kiriting: >? lavlagi, hurmo
Ro'yhatdagi mahsulotlarning bittasi ham bozorda yo'q
```
## 3. Amaliyot. O'quvchi 
1. Bo'sh to'plam e'lon qiling. So'ng uni va uning toifasini ekranga chiqaring
```text
To'plam: set(). Toifasi: <class 'set'>
```
2. Sonlardan 1-10 sonlardan iborat to'plam e'lon qiling. So'ng ekranga chiqaring
```text
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
3. Aralash toifali va duplikat elementlardan iborat to'plam tuzing, so'ng ekrancha chiqaring
```text
{'olma', True, 2, 3, 'nok'}
```
4. Quyidagilarni har birini alohida o'zgaruvchida saqlang, so'ng mana shu o'zgaruvchini va uning toifasini ekranga chiqaring. So'ng ularni har birini to'plamga o'girib, hosil bo'lgan to'plamni ekranga chiqaring:
- {"car": "moshina", "rabit": "quyon"}
- [10,20,20,30,30,40]
- (100,100,200,200,300,300,300)
- "abcdefg"
```text
Toifasi: <class 'dict'>: 
Elementlar: {'car': 'moshina', 'rabit': 'quyon'}
To'plam: {'rabit', 'car'}

Toifasi: <class 'list'>: 
Elementlar: [10, 20, 20, 30, 30, 40]
To'plam: {40, 10, 20, 30}

Toifasi: <class 'tuple'>: 
Elementlar: (100, 100, 200, 200, 300, 300, 300)
To'plam: {200, 100, 300}

Toifasi: <class 'str'>: 
Elementlar: abcdefg
To'plam: {'b', 'a', 'f', 'g', 'c', 'e', 'd'}
```
5. {2,3,4,5,6,7,True, "olma"} to'plamining hamma elementlarini quyidagicha chiqaring:
```text
0-element: olma
1-element: True
2-element: 2
3-element: 3
4-element: 4
5-element: 5
6-element: 6
7-element: 7
```
6. {100,200,300,400,500} to'plamining birinchi va ohirgi uchragan elementini ekranga chiqaring
```text
1-element: 400
5-element: 300
```
7. {'olma', 'nok','banan'} to'plamiga 'qulupnay', 'olcha' mevalarini qo'shing, so'ng boshlang'ich va o'zgargan holatini ekranga chiqaring
```text
Boshlang'ich holat: {'olma', 'nok','banan'}
O'zgargan holat: {'olma', 'olcha', 'qulupnay', 'banan', 'nok'}
```
8. {'olma', 'nok', 'banan'} mevalarni {'sabzi', 'bodring', 'turup'} sabzavotlar bilan birlashtiring, mevalarni alohida, sabzavotlarni alohida, so'ng ikkalasini birlashmasidan hosil bo'lgan to'plamni ekranga chiqaring
```text
Mevalar: {'olma', 'nok', 'banan'}
Sabzavotlar: {'sabzi', 'bodring', 'turup'}
Hammasi: {'olma', 'turup', 'bodring', 'sabzi', 'banan', 'nok'}
```
9. {'olma', 'turup', 'bodring', 'sabzi'} mahsulotlari ichida 'nok' borligini ekranga chiqaring
```text
False
```
10. moshinalar = {'yer', 'yupiter', 'pluton', 'bulut'} to'plamdan ohirgi elementni o'chiring, ekranga boshlang'ich va hosil bo'lgan to'plamni chiqaring
```text
Boshlang'ich to'plam: {'yer', 'yupiter', 'pluton', 'bulut'}
O'zgargan to'plam: {'yer', 'yupiter', 'pluton'}
O'chirilgan element: bulut
```
11. yosh = {22,23,24,25,70,26,27} to'plamidan 70 ni o'chiring. Ekranga boshlang'ich va hosil bo'lgan to'plamni chiqaring
```text
Boshlang'ich to'plam: {22,23,24,25,70,26,27}
O'zgargan to'plam: {22,23,24,25,26,27}
```
12. toplam = {34,45} to'plamini xotiradan o'chiring
13. sonlar = {1,2,3,4,5} to'plamini bo'shatib, foydalanuvchi kiritgan sonni qo'shing
```text
Sonlar: {1,2,3,4,5}
O'chirildi: set()
Son kiriting: 14
Sonlar: {14}
Son kiriting: 55
Sonlar: {14, 55}
```
14. sonlar = {1,2,3,4,5,60,70} to'plamidan ohirgi ikki elementni qiymatini ishlatmasdan o'chiring
```text
Sonlar: {1,2,3,4,5,60,70}
O'chirildi: {1,2,3,4,5}
```
15. {10,20,30,40,50} to'plamini har bir elementini alohida qatorda ekranga chiqaring
```text
10
20
30
40
50
```
16. {'a','b','c','d'} to'plamini har bir elementini alohida qatorda ekranga chiqaring
```text
a
b
c
d
```
17. {10,20,30,40,50} to'plami yordamida for tsiklidan foydalanib, quyidagini ekranga chiqaring. To'plam elementlaridan quyidagi qiymatni qanday hosil qilamiz? O'ylab ko'ring
```text
2
4
6
8
10
```
18. {'a','b','c','d'} to'plami yordamida for tsiklidan foydalanib, quyidagini ekranga chiqaring. To'plam elementlaridan quyidagi qiymatni qanday hosil qilamiz? O'ylab ko'ring<br>*Yordam:* Tsiklni sanab turish uchun yana bitta qo'shimcha o'zgaruvchi ishlatib, har tsiklda 1 ni qo'shib boramiz. Keyin uni satrga ....
```text
a
bb
ccc
dddd
```
19. {10,20,30,40,50} to'plami yordamida for tsiklidan foydalanib, quyidagini ekranga chiqaring. To'plam elementlaridan quyidagi qiymatni qanday hosil qilamiz? O'ylab ko'ring
```text
10
21
32
43
54
```
20. Yuqoridagi natijani alohida to'plamda saqlab, keyin ekranga ikkala to'plani chiqaring:
```text
Birinchi to'plam: {10,20,30,40,50}
Ikkinchi to'plam: {10,21,32,43,54}
```
21. oquv_markazi1 = {'ingliz tili', 'matematika'}, oquv_markazi2 = {'ingliz tili', 'nemis tili', 'turk tili'}, oquv_markazi3 = {'mobil dasturlash', 'web dasturlash'} to'plamlar berilgan. Ya'ni 3 o'quv markazida har hil yo'nalishda dars beriladi. Siz hamma yo'nalishni bitta to'plamda chiqaring:
```text
1-o'quv markazidagi yo'nalishlar: {'ingliz tili', 'matematika'}
2-o'quv markazidagi yo'nalishlar: {'ingliz tili', 'nemis tili', 'turk tili'}
3-o'quv markazidagi yo'nalishlar: {'mobil dasturlash', 'web dasturlash'}
Hamma yo'nalishlar:  {'turk tili', 'web dasturlash', 'ingliz tili', 'mobil dasturlash', 'nemis tili', 'matematika'}
```
22. O'quv markazi faqat til yo'nalishida dars beradi. yonalishlar = {'ingliz', 'turk', 'rus', 'nemis', 'arab'}. Endi bu yo'nalishlar qatoriga yana qoshimcha = {'matematika', 'fizika', 'adabiyot'} fanlarini ham qo'shish kerak. *yonalishlar* to'plamiga *qoshimcha* ni qo'shib o'zgartiring:
```text
O'quv markazda avvalgi yo'nalishlar: {'ingliz', 'turk', 'rus', 'nemis', 'arab'}
O'quv markazida joriy yo'nalishlar: {'ingliz', 'turk', 'rus', 'nemis', 'arab', 'matematika', 'fizika', 'adabiyot'}
```
23. Bozorda {'olma', 'nok', 'banan', 'bodring', 'sabzi'} mahsulotlari bor. Sizning ro'yxatda {'anor', 'olma', 'bodring', 'banan', 'qalampir'} mahsulotlari bor. Bozorda sizning ro'yxatingizdan nima mahsulotlar bor?
```text
Bozordagi mahsulotlar: {'olma', 'nok', 'banan', 'bodring', 'sabzi'}
Ro'yxatingizdagi mahsulotlar: {'anor', 'olma', 'bodring', 'banan', 'qalampir'}
Ro'yxatdan {'olma', 'banan', 'bodring'} mahsulotlari bozorda bor
```
24. O'zbekistondan chet davlatlariga uchayotgan reyslarni tahlil qilish kerak. Bizda quyidagi ma'lumotlar bor:
- kun_1 = {'Turkiya', 'AQSH', 'Avstraliya'}
- kun_2 = {'AQSH', 'Nigeriya','Hindiston', 'Turkiya'}
- kun_3 = {'Turkmaniston', 'Hindiston', 'Avstraliya', 'AQSH', 'Turkiya'}
Sizning vazifangiz odamlar har kuni uchayotgan davlatlar ro'yxatini chiqarish
```text
Eng ommabop reyslar: {'Turkiya', 'AQSH'}
```
25. Yuqoridagi masalani davom ettiramiz. Endi 3 kun davomida faqat bir marta uchilgan davlatlar ro'yxatini chiqaring. <br>*Yordam*. difference() metodidan 3 marta foydalanib, natijani union bilan birlashtirib ekranga chiqarasiz
```text
Kuniga bir marta uchilgan reyslar ro'yxati:
{'Nigeriya', 'Turkmaniston'}
```
26. davlatlar = {"O'zbekiston", "Qozog'iston", "Qirg'iziston", "Turkmaniston", "Tojikiston"} O'rta Osiyo davlatlari berilgan. Mazkur to'plamdan bitta nusha olib, 2 Osiyo davlatlarini qo'shing,so'ng ikkalasini ekranga chiqaring:
```text
O'rta Osiyo davlatlari: {"O'zbekiston", "Qozog'iston", "Qirg'iziston", "Turkmaniston", "Tojikiston"}
Osiyo davlatlari: {"O'zbekiston", "Qozog'iston", "Qirg'iziston", "Turkmaniston", "Tojikiston", "Pokiston", "Hindiston"}
```
27. uz = {"qog'oz",'qalam', 'ruchka'}, en = {'paper', 'pencil', 'pen', 'qalam'} o'zbekcha va inglizcha so'zlar to'plami berilgan. Ingliz so'zlari ichida o'zbekcha so'zlari , yoki aksincha o'zbekcha so'zlar ichida inglizcha so'zlar aralshib ketmaganmi tekshirib ko'ring. Agar aralashgan bo'lsa, u holda usha so'zni ekranga chiqaring. <br>
*Yordam: * Avval isdisjoint bilan tekshiring, so'ng agar bor bo'lsa, usha soz'ni ekranga chiqaring
```text
O'zbekcha so'zlar:{"qog'oz",'qalam', 'ruchka'}
Inglizcha so'zlar: {'paper', 'pencil', 'pen', 'qalam'}
O'zbekcha so'zlar ichida inglizcha so'zlar yo'q
Inglizcha so'zlar ichida o'zbekcha so'zlar: {'qalam'}
```
28. toq_sonlar = {3,5,7,9} va sonlar = {1,2,3,4,5,6,7,8,9} sonlar to'plami berilgan. *toq_sonlar* to'plami *sonlar* to'plamida yotishini tekshiring:
```text
Toq sonlar: {3,5,7,9}
Sonlar: {1,2,3,4,5,6,7,8,9}
Toq sonlar sonlar ichida yotadi
```
29. Restoran menyusida {'osh', 'mastava', 'chuchvara', 'dimlama'} ovqatlari mavjud. Mijoz ekrandan buyurtma uchun ovqatlarni ro'yxatini kiritishi kerak, dastur esa yo'q/borligini, aynan qaysi ovqat borligini borligini aniqlash kerak
```text
Menyu: {'osh', 'mastava', 'chuchvara', 'dimlama'} 
Nima ovqat buyurtma berasiz. Har birini ',' bilan yozing: 
qozon kabob,osh,shashlik,chuchvara

Kechirasiz qozon {'kabob','shashlik'} bizda yo'q
{'osh', 'chuchvara'} bizda bor
```
30. Magazinda {"Hadis va Hayot", "'Atom odatlar',"Qo'rqma"} kitoblari mavjud. Mijozning ekranga kiritgan bir nechta kitobdan qaysi bor , yoki yo'qligini ekranga chiqaring
```text
Mavjud kitoblar: {"Hadis va Hayot", "'Atom odatlar',"Qo'rqma"}
Qaysi kitoblarni olmoqchisiz (',' bilan ajrating): Million dollarlik xatolik,Zukkolar va landovurlar
Bu kitoblar do'konimizda umuman yo'q
```
```text
Mavjud kitoblar: {"Hadis va Hayot", 'Atom odatlar',"Qo'rqma"}
Qaysi kitoblarni olmoqchisiz (',' bilan ajrating): "Hadis va Hayot", 'Atom odatlar'
Bu kitoblar hammasi bizda bor
```
```text
Mavjud kitoblar: {"Hadis va Hayot", 'Atom odatlar',"Qo'rqma"}
Qaysi kitoblarni olmoqchisiz (',' bilan ajrating): "Hadis va Hayot", 'Imomning maniken qizi'
{"Hadis va Hayot"} kitob(lar)i bor
{'Imomning maniken qizi'} kitob(lar)i yo'q
```