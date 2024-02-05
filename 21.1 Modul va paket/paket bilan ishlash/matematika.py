
def qosh(a, b):
    global __hisoblagich
    __hisoblagich += 1
    print(f"{a} + {b} = {a + b}")
    return a + b

def ayir(a, b):
    print(f"{a} - {b} = {a - b}")
    return a - b

def kopaytir(a, b):
    print(f"{a} * {b} = {a * b}")
    return a * b

def bolish(a, b):
    if b == 0:
        print("0 ga bo'lish mumkin emas")
        return None
    print(f"{a} / {b} = {a / b}")
    return a / b

if qosh(10,10) != 20:
    print("Qo'shishda XATO")
if kopaytir(3,4) != 12:
    print("Ko'paytirishda XATO")
if ayir(3,4) != -1:
    print('Ayirishda XATO')
if bolish(8,4) != 2:
    print("Bo'lishda XATO")
