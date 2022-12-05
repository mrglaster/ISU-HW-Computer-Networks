import socket
import pandas as pd
from urllib.parse import urlparse

REGISTER_FILE = 'register.txt'
SEPARATOR = ';'
def get_clear_domain(url):
    """Returns clear webpage domain"""
    result = urlparse(url).netloc
    if len(result) == 0:
        return None
    return result

def get_ip(domain):
    """Returns IP of domain"""
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def webpage_check():
    url = input()
    domain = get_clear_domain(url)
    ip = get_ip(domain)
    dataframe = pd.read_csv(REGISTER_FILE, sep=SEPARATOR, on_bad_lines='skip')

    has_url = len(dataframe[dataframe.eq(url).any(1)]) >= 1
    has_domain = len(dataframe[dataframe.eq(domain).any(1)]) >= 1
    has_ip = len(dataframe[dataframe.eq(ip).any(1)]) >= 1

    if has_url:
        print(f"Url was found in forbidden pages list: {url}")
    if has_domain:
        print(f"Domain was found in forbidden pages list: {domain}")
    if has_ip:
        print(f"IP was found in forbidden pages list: {ip}")

    if not has_ip and not has_url and not has_domain:
        print("Input website is clear! It's not forbidden!")



if __name__ == '__main__':
    webpage_check()