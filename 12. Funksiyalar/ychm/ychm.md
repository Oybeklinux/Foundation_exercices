### 5 Rekursiya
1-masala. Ro'yxat summasi
```python
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])


royxat = [2, 4, 5, 6, 7]
print(f"Berilgan ro'yxat: {royxat}")
print(f"Natija: {list_sum(royxat)}")

```

2-masala. 10 likdan boshqa sanoq tizimiga o'girish

```python
def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

test_malumot = [(2835,16), (100, 8), (45, 16)]
test_natija = ['B13', '144', '2D']
for i in range(len(test_malumot)): #test in test_malumot:
    if to_string(test_malumot[i][0],test_malumot[i][1]) == test_natija[i]:
        print("To'g'ri")
    else:
        print('XATO')
```

3. Ro'yxat elementlarini yig'indisini rekursiv hisoblaydigan rekursiv funksiya

```python
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))
```

4. Sonlar yig'indisini hisoblovchi funksiya
```python
def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))


test_malumot = [12345, 5642, 23545]
test_natija = [15, 17, 19]

for i in range(len(test_malumot)):
	if sumDigits(test_malumot[i]) == test_natija[i]:
		print("To'g'ri")
	else:
		print("XATO")

```

5. Formulani hisoblaydigan dastur
```python
def summa(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (summa(n - 1))


test_malumot = [1, 2, 3,4]
test_natija = [1, 1.5, 1.8333333333333333, 2.083333333333333]

for i in range(len(test_malumot)):
	if summa(test_malumot[i]) == test_natija[i]:
		print("To'g'ri")
	else:
		print("XATO")
```