import speech_recognition as sr
# pip install pipwin
# pipwin install pyaudio


def audio_tanish():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Iltimos, gapiring...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Ovoz tanindi. Matn hisoblanmoqda...")
        tan_olingan_matn = recognizer.recognize_google(audio, language='uz-UZ')
        print("Tan olingan matn:", tan_olingan_matn)
        return tan_olingan_matn
    except sr.UnknownValueError:
        print("Ushbu ovozni taniy olmadim")
        return ""
    except sr.RequestError as e:
        print("Google API uchun so'rov amalga oshmadi; {0}".format(e))
        return ""

def audio_tekshirish(matn):
    print("Ovozni tanish: ", matn)

if __name__ == "__main__":
    tan_olingan_matn = audio_tanish()
    if tan_olingan_matn:
        audio_tekshirish(tan_olingan_matn)
