mijozlar = (('Anvar', 'Bortirov', 49), ('Otabek', 'Fazliddinov', 55), ('Jasur', 'Murodov', 39), ('Bekzod', 'Muslimov', 33))

for mijoz in mijozlar:
    ismi = mijoz[0]
    sharifi = mijoz[1]
    yoshi = mijoz[2]
    print(f"{ismi.center(10)}{sharifi.center(20)}{str(yoshi).center(10)}")