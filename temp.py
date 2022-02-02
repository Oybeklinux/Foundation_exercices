# ustun = 15
# print("Ism".center(ustun), "Sharifi".center(ustun))
# ism = 'Otabek'
# sharifi = "Anvarov"
# print(ism.center(ustun), sharifi.center(ustun))
# ism = 'Anvar'
# sharifi = "Bekzodov"
# print(ism.center(ustun), sharifi.center(ustun))
# ism = 'Sherzod'
# sharifi = "Oybekov"
# print(ism.center(ustun), sharifi.center(ustun))
soz = "Buxoro shahrining tarixiy markazida"
alfa = 0
sign = 0
for harf in soz:
    if harf.isalpha():
        alfa += 1
    else:
        sign += 1
print(f"Harflar soni {alfa}\nBelgilar soni: {sign}")