def fibonachi(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)

for i in range(0,10):
    print(f"{i}-tartibi: {fibonachi(i)}")