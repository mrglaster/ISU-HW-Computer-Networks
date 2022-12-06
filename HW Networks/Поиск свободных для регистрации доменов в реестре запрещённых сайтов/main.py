import requests
import pandas as pd

REGISTER_FILE = 'register.txt'
SEPARATOR = ';'
URL = "http://api.whois.vu/"
def webpages_finder():
    dataframe = pd.read_csv(REGISTER_FILE, sep=SEPARATOR, on_bad_lines='skip')
    col_one_list = dataframe['1-best-muzon.cc'].tolist()
    print("Domains available for buying: ")
    for i in col_one_list:
        PARAM = {"q": i}
        r = requests.get(url=URL, params=PARAM)
        data = r.json()
        if data['available'] == 'yes':
            print(i)

if __name__ == '__main__':
    webpages_finder()