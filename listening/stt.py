import os
import pydub
from pydub import AudioSegment
import speech_recognition as sr

# def mp3_to_wav(mp3_filepath):
#     """
#     这是MP3文件转化成WAV文件的函数
#     :param mp3_path: MP3文件的地址
#     :param wav_path: WAV文件的地址
#     """
#     fp, ext = os.path.splitext(mp3_filepath)
#     wav_filepath = f"{fp}.wav"
#     # pydub.AudioSegment.converter = "D:\\ffmpeg\\bin\\ffmpeg.exe"            #说明ffmpeg的地址
#     mp3_file = AudioSegment.from_mp3(file=mp3_filepath)
#     # mp3_file.export(wav_filepath, format="wav")
#     print(mp3_file.duration_seconds)
#

def audio_to_text(wav_filepath):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(wav_filepath)
    with audio_file as source:
        audio = r.record(source)
    # r.recognize_google(audio)#, language="en-US", show_all=True)
    # r.recognize_bing(audio, show_all=False)
    r.recognize_sphinx(audio)
    # r.recognize_google()


if __name__ == '__main__':
    audio_to_text("../data/boost_listening/test.wav")
#     mp3_filepath = "../data/boost_listening/Boost Listening - IELTS Listening Lesson 1.mp3"
#     mp3_to_wav(mp3_filepath=mp3_filepath)