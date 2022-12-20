import requests
import os
from random import randrange
from pathlib import Path

IAM_TOKEN = 'USE YOUR OWN'
FOLDER_ID = 'USE YOUR OWN'
URL_TRANSLATION = "https://translate.api.cloud.yandex.net/translate/v2/translate"
URL_LANGUAGES  = "https://translate.api.cloud.yandex.net/translate/v2/languages"
TARGET_TEST_LANGS = None



"""Returns codes of supported languages"""
def get_supported_langs():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    body = {
        "folderId": FOLDER_ID
    }
    try:
        response = requests.post(URL_LANGUAGES, json=body, headers=headers)
        objects = (response.json())["languages"]
        supported_langs = []
        for i in objects:
            supported_langs.append(i['code'])
        return supported_langs
    except:
        raise ConnectionError("Unable to connect to Yandex Services!")


"""Translates sentence"""
def translate_text(text, dist_lang, DEBUG=0):

    if len(text) == 0:
        raise ValueError("Unable to translate empty text!")
    if len(dist_lang) >= 3 or len(dist_lang) < 2:
        raise ValueError("Wrong Language!")
    if DEBUG:
        print(f"Got Params: {text} -> {dist_lang} ")

    body = {
        "targetLanguageCode": dist_lang,
        "texts": text.split(),
        "folderId": FOLDER_ID,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    try:
        response = requests.post(URL_TRANSLATION, json=body, headers=headers)
        respa = response.json()
        result = ''
        print(respa)
        for text in respa["translations"]:
            result += text['text'] + " "
        if DEBUG:
            print(f"{text} - {dist_lang} - {result}")
        return result
    except:
        raise ConnectionError("Something went wrong during text translation!")

"""Translates every line of text file to random supported languages and writes result to OLDNAME_new.txt"""
def translate_random_ffile(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error! File {filepath} doesn't exist!")
    lines_array = []
    with open(filepath, encoding='utf-8') as my_file:
        for line in my_file:
            lines_array.append(line)
    new_file = Path(filepath).stem
    file_translated = open(f"{new_file}_translated.txt", "a", encoding="utf-8")
    cntr = 0
    for i in lines_array:
        random_num = randrange(0, len(TARGET_TEST_LANGS))
        local_result = translate_text(i, TARGET_TEST_LANGS[random_num])
        cntr+=1
        file_translated.write(local_result+'\n')
    print("Translation was done!")
    print(f"Translated Lines: {cntr}")


def main():
    TARGET_TEST_LANGS = get_supported_langs()
    translate_random_ffile('testfile.txt')

if __name__ == '__main__':
    main()