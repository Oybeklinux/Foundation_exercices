def daraja_5mi(a):
    daraja = 1
    while True:
        daraja *= 5
        if daraja == a:
            return True
        elif daraja > a:
            return False


for i in range(0,1000):
    if daraja_5mi(i):
        print(i)