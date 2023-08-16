from random import choice


def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param 
        None - hech narsa qaytarmaydi
    :return 
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    pass


def doskani_korsat(doska):
    """
    Doskani ekranga chiqaradi
    :param 
        doska
    :return
        None - hech narsa qaytarmaydi
    """
    for qator in doska:
        print('+-------+-------+-------+')
        for i in range(3):
            if i == 1:
                print(f"|   {qator[0]}   |   {qator[1]}   |   {qator[2]}   |")
            else:
                print(f"|       |       |       |")
    print('+-------+-------+-------+')


def foydalanuvchi_tanlasin(doska):
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    raqam = int(input("Raqam kiriting: "))
    for i in range(len(doska)):
        for j in range(len(doska[i])):
            if doska[i][j] == raqam:
                doska[i][j] = '0'
                return


def bosh_maydonlar(doska):
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi 
    :param 
        doska
    :return 
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    royxat = []
    for qator in doska:
        for son in qator:
            if son not in ['X', '0']:
                royxat.append(son)
    return royxat


def golib_bormi(doska, belgi):
    """
    G'olib borligini aniqlaydi
    :param 
        doska
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """
    for qator in doska:
        if qator[0] == qator[1] == qator[2] == belgi:
            return True
    for i in range(len(doska)):
        if doska[0][i] == doska[1][i] == doska[2][i] == belgi:
            return True

    if doska[0][0] == doska[1][1] == doska[2][2] == belgi:
        return True
    if doska[0][2] == doska[1][1] == doska[2][0] == belgi:
        return True
    return False


def kompyuter_tanlasin(doska):
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    belgilanmaganlari = bosh_maydonlar(doska)
    raqam = choice(belgilanmaganlari)
    for i in range(len(doska)):
        for j in range(len(doska[i])):
            if doska[i][j] == raqam:
                doska[i][j] = 'X'
                return
    # Funktsiya kompyuterning harakatini chizadi va chizmani yangilaydi.


doska = bosh_doska_hosil_qil()
doska[1][1] = 'X'
doskani_korsat(doska)

while bosh_maydonlar:
    foydalanuvchi_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, '0'):
        print("Siz yutdingiz")
        break
    kompyuter_tanlasin(doska)
    doskani_korsat(doska)
    if golib_bormi(doska, 'X'):
        print("Kompyuter yutdi")
        break
