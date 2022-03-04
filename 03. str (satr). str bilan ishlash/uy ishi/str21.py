ism_sharif = input("Ism sharifingiz: ").split()
if 'ov' in ism_sharif[0]:
    ism, sharif = ism_sharif[1], ism_sharif[0]
    print(f"Ismingiz: {ism}\nSharifingiz: {sharif}")
elif 'ov' in ism_sharif[1]:
    ism, sharif = ism_sharif[0], ism_sharif[1]
    print(f"Ismingiz: {ism}\nSharifingiz: {sharif}")
else:
    print('Sharifingiz xato')


