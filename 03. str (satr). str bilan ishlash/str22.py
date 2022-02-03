matn = input("Matn kiriting: ")
sozlar = []
print("Harflar soni")
for m in matn:
    if m not in sozlar:
        print(f"{m} - {matn.count(m)}")
        sozlar.append(m)