# Harajatingiz: 100000
# Hizmatchi haqqi foizda 10, 15, 20: 15
# Nechchi kishidan iboratsiz? 5
# Hammasi:  115000.0
# Har biringizga  23000.0 so'mdan tushar ekan

harajat = input("Harajatingiz: ")
foiz = input("Hizmatchi haqqi foizda 10, 15, 20: ")
kishi_soni = input("Nechchi kishidan iboratsiz? ")
hammasi = int(harajat) + int(harajat) * int(foiz) / 100
har_biriga =  hammasi // int(kishi_soni)
print("Hammasi: ", hammasi)
print("Har biringizga ", har_biriga ,"so'mdan tushar ekan")
