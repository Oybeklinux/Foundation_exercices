import qrcode
# https://www.canva.com/design/DAF00NElow8/rZ46bh4GoDX8hIcpGwgnzA/edit?utm_content=DAF00NElow8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
def qr_kodni_yaratish(matn, fayl_nomi):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(matn)
    qr.make(fit=True)

    rasm = qr.make_image(fill_color="black", back_color="white")
    rasm.save(fayl_nomi)
    print(f"QR kod muvaffaqiyatli yaratildi va {fayl_nomi} nomi bilan saqlandi.")

if __name__ == "__main__":
    matn = input("QR kodingizga kiritiladigan matnni kiriting: ")
    fayl_nomi = input("Fayl nomini kiriting (masalan: qr_code.png): ")
    qr_kodni_yaratish(matn, fayl_nomi)
