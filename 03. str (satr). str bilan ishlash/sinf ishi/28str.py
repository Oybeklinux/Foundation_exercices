"""
Matn metodlarini birma-bir ko'rib chiqamiz
"""
text = "mening ismim Otabek"
print('capitalize() -', text.capitalize())
print('title() -', text.title())
print('split(" ") -', text.split(' '))
print('center(30):')
print(text.center(30))
print('Otabek'.center(30)) # 30 ta simvolli joy ajratib o'rtaga joylashtiradi
print('count("i") -',text.count('i')) # matndagi belgilar soni
print('endswith("bek") -', text.endswith('bek')) # ohiri berilgan ketma-ketlikka tugashiga tekshiradi
text = text.replace(" ", "\t") # probelni tab ga almashtiradi
print('replace(" ", "\t") -', text)
print("expandtabs(10) -", text.expandtabs(10)) #tab - probellar soniga almashtiradi
print("find('ism') -", text.find('ism')) # topsa indeksini, topmasa -1 ni qaytaradi