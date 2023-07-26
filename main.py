def mening_funksiyam(royxat_1):
    print("#1:", royxat_1)
    print("#2:", royxat_2)
    royxat_1.pop("2")  # Bu yerga ahamiyat bering
    print("#3:", royxat_1)
    print("#4:", royxat_2)


royxat_2 = {"2": 3}
mening_funksiyam(royxat_2)
print("#5:", royxat_2)