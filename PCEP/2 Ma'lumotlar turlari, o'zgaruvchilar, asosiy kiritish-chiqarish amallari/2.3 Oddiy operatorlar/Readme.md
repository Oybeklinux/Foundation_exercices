<!-- TOC -->
* [2.3 Oddiy operatorlar](#21-pythonda-birinchi-dastur)
  * [Amaliyot. Sinf ishi](#amaliyot-sinf-ishi)
  * [Savollar](#savollar)
  * [Amaliyot. Uy ishi](#amaliyot-uy-ishi)
  * [Lug'at](#lugat)
  * [Savollarga javob](#savollarga-javob)
  * [Amaliyot. Uy ishi javobi](#amaliyot-uy-ishi-javobi)
<!-- TOC -->
# 2.3 Oddiy operatorlar

## Amaliyot. Sinf ishi

1. Ekranga nechchi chiqadi?

```python
print(2 - 4)
```
```python
print(2 - 1.)
```
```python
print(2. - 1)
```
```python
print(3. - 2.)
```
```python
print(1. - 1.)
```

2. Ekranga nechchi chiqadi?

```python
print(2 + 4)
```
```python
print(2 + 1.)
```
```python
print(2. + 1)
```
```python
print(3. + 2.)
```
```python
print(1. + 1.)
```

```python
print(1. + -1.)
```

```python
print(1. + --1.)
```

3. Ekranga nechchi chiqadi?

```python
print(2 * 4)
```
```python
print(2 * 1.)
```
```python
print(2. * 1)
```
```python
print(3. * 2.)
```
```python
print(1. * 1.)
```

```python
print(4. * -5.)
```

```python
print(-5. * -6.)
```
4. Ekranga nechchi chiqadi?

```python
print(2 / 4)
```
```python
print(2 / 1.)
```
```python
print(2. / 1)
```
```python
print(3. / 2.)
```
```python
print(1. / 1.)
```

```python
print(4. / -5.)
```

```python
print(-15. / -3.)
```
```python
print(-100 / 50 / -1)
```

5. Ekranga nechchi chiqadi?

```python
print(2 // 4)
```
```python
print(2 // 1.)
```
```python
print(2. // 1)
```
```python
print(3. // 2.)
```
```python
print(10. // 4.)
```

```python
print(23. // -5.)
```

```python
print(-15. // -3.)
```

```python
print(-15. // -3.2)
```

```python
print(-6.9 // -2.2)
```
```python
print(100 // 5 // 4)
```
```python
print(100. // 5 // 4)
```

5. Ekranga nechchi chiqadi?

```python
print(9 % 4)
```
```python
print(8 % 4)
```
```python
print(2 % 4)
```
```python
print(3. % 2.)
```
```python
print(10. % 4.)
```




## Savollar

1. Operator nima?
2. Ifoda nima?
3. Operatorlarga qaysilar kiradi?
4. Yuqoridagi operatorlar natijasi qaysi holatda int bo'ladi?
5. `-` operatori unarmi yoki binarmi?
6. Assotsiativlik nima? Qaysi operatorlar qanday assotsiativlikka ega?
7. Ustunlik ro'yxatini tartib bo'yicha aytib bering
8. Operator ustunligini o'zgartirish mumkinmi?

## Amaliyot. Uy ishi
1. operator
2. ifoda
3. ustunlik ro'yxati
4. assotsiativlik

## Lug'at
1. operator - operator
2. ifoda - expression
3. Darajaga oshirish(eksponentsiya) - exponentiation
4. Ko'paytirish - multiplication
5. * asterisk
6. Bo'lish - division
7. Bo'linuvchi - dividend
8. Bo'luvchi - divisor
9. yaxlitlangan - rounded
10. qoldiq (modul) - remainder (modulo)
11. Qo'shish - addition
12. Ayirish - subtraction
13. unar operator - unary operator
14. binar operator - binary operator
15. operator ustunliklari - operator priorities
16. o'ngdan o'qish - right-sided binding
17. chapdan o'qish - left- sided binding
18. Qavs - parentheses


## Savollarga javob

1. Operator nima?

**Javob:**

`Operator` - qiymat bilan ishlaydigan belgi

2. Ifoda nima?

**Javob:**

`Ifoda` - qiymat(ma'lumot) bilan operator birlashmasi
3. Operatorlarga qaysilar kiradi?

**Javob:**

Operatorlar:
- `+`  - qo'shish
- `-`  - ayirish
- `*`  - ko'paytirish
- `/`  - bo'lish
- `//` - bolib, butun qismini olish
- `%`  - bolib, qoldig'ini olish
- `**` - darajaga oshirish

4. Yuqoridagi operatorlar natijasi qaysi holatda int bo'ladi

**Javob:**

Ikkala argument int bo'lsa, `*`, `-`, `+`, `//`, `%`, `**` amallar natijasi int, qolgan holatda float bo'ladi:
Bo'lishda `/` esa har doim float bo'ladi

5. `-` operatori unarmi yoki binarmi?

**Javob:**

Agar `-` operatori bitta argument bilan kelgan bo'lsa, `unar`, aks holda `binar` operator bo'ladi

Unar operatorga misol: -2, -4.5
Binar operatorga misol- 2 - 4, 4 - 9

6. Assotsiativlik nima? Qaysi operatorlar qanday assotsiativlikka ega?

**Javob:**

Assotsiativlik - ketma-ket bir xil ifodalarning bajarilish ketma-ketligini bildiradi

Ikki xil assotsiativlik mavjud: chap va o'ng

Chap assotsiativlikka: `*`, `-`, `+`, `//`, `%`, `/`

O'ng assotsiativlikka: `**`

Misol:

Chap assotsiativlikka: 

`2 ** 2 ** 3 = 512`

O'ng assotsiativlikka: 

`8 / 4 / 2 = 1.0`

`9 % 6 % 2 = 1`

7. Ustunlik ro'yxatini tartib bo'yicha aytib bering

**Javob**

1. `+`, `-` - unar
2. `**`
3. `*, /, %, //`
4. `+, -`


8. Operator ustunligini o'zgartirish mumkinmi?

**Javob**

Qavslar yordamida operator ustunliginini o'zgartirish mumkin

Misol

(15 * ((34 % 13) + 100) / (2 * 13)) // 2

## Amaliyot. Uy ishi javobi


