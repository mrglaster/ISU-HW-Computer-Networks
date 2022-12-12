import os
import speech_recognition as sr
import requests
from speechkit import Session, SpeechSynthesis
from google_speech import Speech
from pydub import AudioSegment

FOLDER_ID = "USE YOUR OWN"
IAM_TOKEN = "USE YOUR OWN"
def google_speech_to_text(path, lang):
    """Speech to text translation using Google"""
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
        s = r.recognize_google(audio, language=lang)
        return s


def google_text_to_speech(text, lang, mode=1):
    """Text to Speech using Google"""
    if len(text) == 0:
        raise ValueError("Unable to work with text whos length is 0! ")
    speech = Speech(text, lang)
    if mode == 1:
        speech.play()
    else:
        filename = f"{text.replace(' ', '_')}.mp3"
        speech.save(filename)


def yandex_speech_to_text(filepath, lang):
    """Converts speech from .OGG file to text with Yandex Services"""
    if not filepath.endswith('.ogg'):
        raise ValueError(f"File reading error! Expected .ogg file. Got: {filepath}")
    with open(filepath, "rb") as f:
        name_guest = f.read()
    URL = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize/"
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN} '
    }
    params = {
        'lang': lang,
        'folderId': FOLDER_ID,
        'sampleRateHertz': 48000,
        'url': f'{filepath}'
    }
    try:
        return requests.post(URL, headers=headers, params=params, data=name_guest, stream=True).json()["result"]
    except:
        raise ConnectionError("Something went wrong during yandex service conection or your data is a crap!")


def yandex_process_synth(text, lang):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN} '
    }

    data = {
        'text': text,
        'lang': lang,
        'voice': 'jane',
        'folderId': FOLDER_ID,
        'format': 'mp3',
        'sampleRateHertz': 48000,
    }
    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


def yandex_text_to_speech(text, lang):
    """Voices speech with Yandex Services"""
    with open(f'{text.replace(" ", "_")}.mp3', "wb") as f:
        for audio_content in yandex_process_synth(text, lang):
            f.write(audio_content)



def main():
    google_text_to_speech("Hello Google World", 'en-US', 2)
    print(f"Transcribed by Google: {google_speech_to_text('test.wav', 'en')}")
    print(f"Transcribed by Yandex: {yandex_speech_to_text('test.ogg', 'en-US')}")
    yandex_text_to_speech("Hello Yandex World", 'en-US')


if __name__ == '__main__':
    main()
