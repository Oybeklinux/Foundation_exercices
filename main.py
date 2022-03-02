import os
import sys
import platform

def menu(habar, lst):
    birinchi = True
    for e in lst:
        print(e)

    while True:
        if birinchi:
            tanlov = input(habar)
            birinchi = False
        else:
            tanlov = input("Xato qayta kiriting: ")
        if tanlov == "x":
            return None

        if tanlov.isdigit():
            for e in lst:
                if e.lstrip("0").startswith(tanlov.lstrip("0")):
                    return e


def clear_screen():
    system = platform.system().lower()
    if system == "windows":
        os.system("cls")
    elif system == "linux":
        os.system("clear -x")
    else:
        os.system("clear screen")


def enter_to_coninute():
    input("Davom etish uchun Enter ni bosing")


if __name__ == "__main__":
    # Papkalarni ro'yxatini chiqarish
    dirs = [file for file in os.listdir(".") if os.path.isdir(file) and not file.startswith(".") ]
    while True:
        clear_screen()
        mavzu = menu("Papka raqamini kiriting yoki chiqish uchun x ni bosing: ", dirs)
        # chiqish uchun
        if not mavzu:
            sys.exit()
        mavzu = os.path.join(mavzu, "sinf ishi")

        if os.path.exists(mavzu):
            # papka ichidagi .py fayllarni chiqarish
            files = [file for file in os.listdir(mavzu) if file.endswith(".py")]
            if len(files):
                mashq = menu("Mashq raqamini kiriting yoki orqaga qaytish uchun x ni bosing: ", files)
                # asosiy menyuga qaytish
                if not mashq:
                    continue
                mashq = os.path.join(mavzu, mashq)
                if os.path.exists(mashq):
                    clear_screen()
                    os.system(f"python \"{mashq}\"")
            else:
                print("Mashqlar mavjud emas")
        else:
            print("Bunday papka mavjud emas")
        enter_to_coninute()

