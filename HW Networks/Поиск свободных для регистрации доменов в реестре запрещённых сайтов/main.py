import requests
import sockets
import pandas as pd

REGISTER_FILE = 'register.txt'
SEPARATOR = ';'
URL = "http://api.whois.vu/"

def get_ip(domain):
    """Returns IP of domain"""
    try:
        return socket.gethostbyname(domain)
    except:
        return None
   
def webpages_finder():
    """Finds such pages in the register, which are allowed for buying"""
    dataframe = pd.read_csv(REGISTER_FILE, sep=SEPARATOR, on_bad_lines='skip')
    col_one_list = dataframe['1-best-muzon.cc'].tolist()
    print("Domains available for buying: ")
    for i in col_one_list:
        ip_adress =get_ip(i)
        if ip_adress is None:
            PARAM = {"q": i}
            r = requests.get(url=URL, params=PARAM)
            data = r.json()
            if data['available'] == 'yes':
                print(i)

if __name__ == '__main__':
    webpages_finder()
