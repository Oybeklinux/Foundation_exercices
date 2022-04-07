def fibonachi(tartibi=0):
    # if a == 0:
    #     return 0
    # if a == 1:
    #     return 1
    # return fibonachi(a-2) + fibonachi(a-1)
    sum = 0
    a1=0
    a2=1
    k = [a1, a2]

    for i in range(2, tartibi+1):
        sum = a1 + a2
        a1, a2 = a2, sum
        k.append(sum)
        print(k)
        if i+1 == tartibi:
            return sum

    return k


k = int(input("Tartib raqamini kiriting: "))
print(fibonachi(k))