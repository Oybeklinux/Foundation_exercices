import os.path
from sys import stdout, stdin


file_name = "talabalar"

def init():
    """
    Agar fayl bo'lmasa, 2ta talabalarni yoz
    :return:
    """
    if not os.path.exists(file_name):
        talabalar = [
            {
                "ismi": "Otabek",
                "yoshi": 25,
            },
            {
                "ismi": "Anvar",
                "yoshi": 30,
            }
        ]
        write(talabalar)


def write(talabalar: dict):
    file = open(file=file_name, mode='w')
    for talaba in talabalar:
        qator = f"{talaba['ismi']}|{talaba['yoshi']}\n"
        # print(qator, file=file)
        file.write(qator)


def read() -> list:
    file = open(file=file_name, mode='r')
    talabalar = []
    for talaba in file.readlines():
        qatorlar = talaba.split("|")
        # print(qatorlar)
        print(f"{qatorlar[0]}\t\t{qatorlar[1].strip()}")
        talabalar.append(
            {
                "ismi": qatorlar[0],
                "yoshi": int(qatorlar[1])
            }
        )
    return talabalar


def update(eski_ismi, yangi_ismi):
    pass


def search(ismi: str = None, yoshi: int = None):
    if not ismi and not yoshi:
        return

# faylni yaratib, talabalarni kiritish
init()
# talabalarni dict ga o'girish va ekranga chiqarish
talabalar = read()
print(talabalar)
# talaba qo'shish
# talabalar.append(
#     {
#         "ismi": input("Ismini kiriting: "),
#         "yoshi": int(input("Yoshini kiriting: "))
#     }
# )
# write(talabalar)
# read()


"""

Mahsulotlar bo'yicha qaysi amaliyotni tanlaysiz?:
    1. Qo'shish
    2. Ko'rish
    3. O'chirish
    4. Qidirish
    5. O'zgartirish
    


Jadval ko'rinishi:
Nomi narxi  soni
"""