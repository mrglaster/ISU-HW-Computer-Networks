import os
DATA_FILE = 'ips.txt'

def main():
    if not os.path.exists(DATA_FILE):
        print("File with IP addresses wasn't found!")
        return -1
    cntr = 0
    file = open(DATA_FILE)
    while True:
        line = file.readline()
        if not line:
            break

        curline = line.strip()
        number = int(curline[curline.find('\\')-1:])
        amount = 2**(32-number)
        print("For curline: "+line.strip()+" were banned "+ str(amount)+" ID address(s)")
        cntr+=amount
    print("===============================================================================")
    print("")
    print("In general: ", cntr)
    return 0




if __name__=='__main__':
    main()