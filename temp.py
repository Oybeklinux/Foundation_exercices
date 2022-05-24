def fun(a:int):
    if a not in [1,2,3,4]:
        raise ValueError
    else:
        a + a

try:
    f = 2 + 23
    d = {}
    f = []
    fun(23)
except TypeError as e:
    print("Ma'lumot turida xatolik",e)
except KeyError as e:
    print("Katlitda xatolik", e)
except IndexError as e:
    print("Indeksda xatolik", e)
except ZeroDivisionError:
    print("0 bo'lish xatoligi")
except FileNotFoundError:
    print("Fayl mavjud emas")
except FileExistsError:
    print("Fayl mavjud")
except ValueError:
    print("Qiymatda xatolik")
else:
    print("Ishladi")
finally:
    print("Dastur tugadi")


