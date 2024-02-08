from PIL import Image
import os

def rasmni_webpga_ogirish(rasm_nom):
    try:
        im = Image.open(rasm_nom)
        webp_nom = os.path.splitext(rasm_nom)[0] + ".webp"
        im.save(webp_nom, "WEBP")
        print(f"{rasm_nom} fayli {webp_nom} ga muvaffaqiyatli o'girildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


if __name__ == "__main__":
    rasm_nom = input("O'girishni istagan rasm faylini kiriting: ")
    rasmni_webpga_ogirish(rasm_nom)
