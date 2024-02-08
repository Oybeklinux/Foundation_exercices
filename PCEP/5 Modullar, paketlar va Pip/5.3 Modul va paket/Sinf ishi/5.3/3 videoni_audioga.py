from moviepy.editor import *

def video_to_audio(video_file, audio_file):
    try:
        video = VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(audio_file)
        print(f"{video_file} fayli {audio_file} ga muvaffaqiyatli o'girildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


if __name__ == "__main__":
    video_file = input("O'girishni istagan video faylini kiriting: ")
    audio_file = input("Musiqaga o'girilgan fayl nomini kiriting (masalan: audio.mp3): ")
    video_to_audio(video_file, audio_file)
