"""
14. Shar hajmini aniqlaydigan kod yozing.
pi o'zgarmas sondan iborat bo'lib, uni 3.14 deb olamiz, ya'ni pi=3.14. Radius R ni esa foydalanuvchi kiritsin. Shar hajmi formulasi: <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\inline&space;V=\frac{4}{3}\pi&space;R^{3}" title="\inline V=\frac{4}{3}\pi R^{3}" />

Shar radiusini kiriting: 9
Sharning hajmi 3052.08

"""
pi = 3.14
r = int(input("Shar radiusini kiriting: "))
v = 4/3 * pi * r ** 3
print("Sharning hajmi", v)