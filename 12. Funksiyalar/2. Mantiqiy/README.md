<h6>Amaliyot. Funksiya</h6>
1. Ikki parametrli (soz, harf) funkisya yozing. Agar harf sozni ichida bo'lsa, u holda sozdagi pozitsiyasini qaytarsin, bo'lmasa -1 qiymatini qaytarsin
Funksiya son qaytaradi, ikki(soz, harf) parametrdan iborat
   
    
    harf = "h"
    soz = "Mashina"
    tartibi = harf_indeksi(soz, harf)
    if tartibi != -1:
        print(f"'{harf}'  '{soz}'da {tartibi}-o'rinda kelgan")
    
natija

    'h'  'Mashina'da 4-o'rinda kelgan
