<h6>Nazariya. Funksiya</h6>
1. Ekranga "Assalomu alaykum" degan yozuvni chiqarish


    print(Assalomu alaykum")
yoki funksiya yordamida chiqarish

    
    def salom_ber():
        print("Assalomu alaykum")
    

    salom_ber()
2. Funksiya haqida ma'lumot yozish


    def salom_ber():
    """
    Salom berish vazifasini bajaradi
    """
        print("Assalomu alaykum")

3. Salomdan keyin ismni ham chiqarish


    def salom_ber(ism): 
        print(f"Assalomu alaykum {ism}")
4. Sonni kvadratini hisoblash


    def kvadratini_hisobla(son): 
        print(son ** 2)
    

    kvadratini_hisobla(4) #16

5. Sonni kvadratini hisoblab, qaytarish


    def kvadratini_hisobla(son): 
        return son ** 2

    natija = kvadratini_hisobla(4)
    print(f"4 ning kvadrati {natija}")
6. Funksiyaga bir nechta qiymat berish


    def summa(a, b): 
        return a + b
 
    print(summa(4,5)) #9
    print(summa(4,15)) #19
7. Funksiyaga standart qiymat berish

    
    def summa(a, b=10): 
        return a + b
 
    print(summa(4,5)) #9
    print(summa(4)) #19
8. Funksiyaga qiymatlarni har hil tartibda va har hil usulda berish


    def summa(a, b=10): 
        return a + b
 
    print(summa(b=5, a=5)) #9
    print(summa(a=5, b=15)) #20
    print(summa(a=5)) #9
    print(summa(5)) #9
9. 3 ga karrali ekanini aniqlaydigan funksiya:


    def uchga_karralimi(son):
        return son % 3 == 0
    
    print(uchga_karralimi(4))
    print(uchga_karralimi(27))
natija

    False
    True
10. Yuqoridagi funksiyadan qaytgan qiymatga qarab tegishli habarni ekranga chiqarish


    son = 4
    if uchga_karralimi(son):
        print(f"{son} 3 ga karrali")
    else:
        print(f"{son} 3 ga karrali emas")
natija

    4 3 ga karrali emas
11. Berilgan son 3 ga karrali ekanini aniqlaydigan funksiyani ko'rib o'tdik, endi 3ni ham o'zgaruvchiga almashtiramiz. Funksiyamiz ikki parametrli bo'ladi. 


    def karralimi(son, karra):
        return son % karra == 0
    
    print(karralimi(10, 5))
    print(karralimi(34, 5))
natija

    True
    False
12. So'zda harf borligini aniqlovchi funksiyani yozing
    Funksiya True/False qiymatini qaytaradi. Ikkia (soz, harf) parametrdan iborat bo'ladi
    

    def harf_bormi(soz, harf):
        return harf in soz
    
    harf_bormi("dars", "s")
    harf_bormi("mashina", "p")
natija

    True
    False
<h6>Amaliyot. Funksiya</h6>
1. O'zingiz haqingizda ma'lumotni ekranga chiqaradigan funksiya yozing. Funksiya nomini men_haqimda() deb nomlang 
   E'tibor bering funksiya hech qanday  qiymat qaytarmaydi va hech qanday qiymat qabul qilmaydi. Funksiyani chaqirganda quyidagi ko'rinishda ma'lumot chiqsin


    Ismi: Oybek
    Familiyasi: Nuriddinov
    Tug'ilgan yili: 1987
    Tug'ilgan shahri: Toshkent
    Kasbi: Dasturchi 
     
2. Yuqoridagi funksiyani parametrli qiling. Funksiyani  haqida() deb nomlang   
   E'tibor bering funksiya hech qanday  qiymat qaytarmaydi, lekin ism, familiya, yil, t_shahar kabi parametrlari bo'ladi. Funksiyaga har hil qiymat berib chaqiring 


    men_haqimda("Anvar", "Otabekov", 1980, "Olmaliq", "Menejer")
natija

    Ismi: Anvar
    Familiyasi: Otabekov
    Tug'ilgan yili: 1980
    Tug'ilgan shahri: Olmaliq
    Kasbi: Menejer
3. Yuqoridagi funksiya natijasini return bilan qaytaradigan qiling. Natijani ekranga chiqarish funksiyadan tashqarida amalga oshiring.   
   E'tibor bering funksiya natijani qaytaradi, va ism, familiya, yil, t_shahar kabi parametrlari bo'ladi. Funksiyaga har hil qiymat berib chaqiring 


    anvar = men_haqimda("Anvar", "Otabekov", 1980, "Olmaliq", "Menejer")
    otabek = men_haqimda("Otabek", "Bekzodov", 1970, "Guliston", "Mexanik")
    print(otabek)
natija

    Ismi: Otabek
    Familiyasi: Bekzodov
    Tug'ilgan yili: 1970
    Tug'ilgan shahri: Guliston
    Kasbi: Mexanik
4. Yuqoridagi funksiyada yili nomli parametrga standart 1990 qiymatini bering   
    E'tibor bering funksiyani chaqirganda yilni yozmasa ham 1990 qiymatini ishlatadi

    
    otabek = men_haqimda("Otabek", "Bekzodov", "Guliston", "Mexanik")
    print(otabek)
natija

    Ismi: Otabek
    Familiyasi: Bekzodov
    Tug'ilgan yili: 1970
    Tug'ilgan shahri: Guliston
    Kasbi: Mexanik
5. Yuqoridagi qiymatlarni funksiyaga har hil tartibda bering. Ya'ni avval kasbi, so'ng, familiyasi, so'ng ismi va hak
    Natija bir hil bo'lsin:
   

    Ismi: Otabek
    Familiyasi: Bekzodov
    Tug'ilgan yili: 1970
    Tug'ilgan shahri: Guliston
    Kasbi: Mexanik
6. Ikki sonni yig'indisini qaytaradigan funksiya yozing. 
    Funksiya yig'indini qaytaradi, ikki parametrdan iborat bo'ladi
   

    natija = yig'indini_hisobla(12,34)
    print(natija) 
natija

    46
7. Uch sonni ko'paytmasini qaytaradigan funksiya yozing. 
    Funksiya son qaytaradi, uch parametrdan iborat bo'ladi
   

    natija = yig'indini_hisobla(3, 4, 5)
    print(natija) 
natija

    60
8. Ikki sondan kattasini qaytaradigan qaytaradigan funksiya yozing. 
    Funksiya son qaytaradi, ikki parametrdan iborat bo'ladi


    natija = kattasini_qaytar(34,3)
    print(natija)
natija

    34
9. Sonni musbatga o'girib qaytaradigan qaytaradigan funksiya yozing. 
    Funksiya son qaytaradi, bitta parametrdan iborat bo'ladi


    print(musbatga_ogir(-10))
    print(musbatga_ogir(20))
natija

    10
    20
10. Son juft bo'lsa, True, aks holda False qiymatini qaytaradigna funksiya yozing
    Funksiya True/False qiymatini qaytaradi, bitta parametrdan iborat bo'ladi
   

    print(toqmi(6))
    print(toqmi(17))
natija

    False
    True
11. Gap ichida so'z borligini aniqlaydigan funksiya yozing
    Funksiya True/False qiymatini qaytaradi, ikki(gap, soz) parametrdan iborat bo'ladi
    

    natija = soz_bormi("Bugun birinchi dars bo'ldi", "dars")
    print(natija)
    natija = soz_bormi("Dasturlash asoslari", "birinchi")
    print(natija)
natija

    True
    False
