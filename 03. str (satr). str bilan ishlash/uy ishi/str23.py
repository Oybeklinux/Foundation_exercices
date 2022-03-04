matn = input("Matn kiriting: ")
harflar = 0
belglar = 0
for m in matn:
    if m.isalpha():
        harflar += 1
    else:
        belglar += 1

print(f"Harflar soni {harflar}\nBelgilar soni: {belglar}")
