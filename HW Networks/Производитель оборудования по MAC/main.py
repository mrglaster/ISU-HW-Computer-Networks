import os

MAC_DATABASE = 'MacVendors.txt'
SEPARATOR = ':'
MAC_DICT = {}
def read_macs():
    file = open(file=MAC_DATABASE, encoding='utf-8')
    for line in file:
        file_mac = line.split('\t')
        MAC_DICT[file_mac[0]] = file_mac[1].replace('\n','')
    file.close()


def main():
    if not os.path.exists(MAC_DATABASE):
        print("File not flound!")
        exit(-1)
    read_macs()
    adress = input()
    if not SEPARATOR in adress:
        print("Wrong MAC adress format!")
        return None
    manuf = adress.replace(SEPARATOR,'')
    manuf = manuf[:len(manuf)-6]
    print(MAC_DICT[manuf])






if __name__=='__main__':
    main()
