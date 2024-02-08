from gtts import gTTS

# Мы должны глубоко осваивать новые знания и инновационные технологии. Это позволит идти по кратчайшему пути прогресса.
def matn_audioya(matn, fayl_nomi):
    try:
        tts = gTTS(text=matn, lang='ru')
        tts.save(fayl_nomi)
        print(f"{fayl_nomi} fayli muvaffaqiyatli yaratildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    matn = input("O'girishni istagan matnni kiriting: ")
    fayl_nomi = input("Ovozga o'girilgan MP3 fayl nomini kiriting (masalan: audio.mp3): ")
    matn_audioya(matn, fayl_nomi)
