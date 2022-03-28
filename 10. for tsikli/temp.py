num1 = int(input("1-sonni kiriting: "))
num2 = int(input("2-sonni kiriting: "))
num3 = int(input("3-sonni kiriting: "))
max1 = num1
max2 = num2

if max1 < max2:
    max1, max2 = max2, max1

if max2 < num3:
   max2 = num3

if max1 < max2:
    max1, max2 = max2, max1
print(max1, max2)