import os
import math
import matplotlib.pyplot as plt
import pandas as pd
FILENAME = 'ManyPings.txt'

def read_data():
    if not os.path.exists(FILENAME):
        print("File not flound!")
        return -1

    with open(FILENAME) as my_file:
        data = []
        for line in my_file:
            try:
                value = float(line)
                if value>900.0:
                    value/=10.0
                data.append(value)
            except:
                pass
    return data


def main():
    data = read_data()
    fields = {}
    for i in range(1, 31):
        fields[i*10] = 0
    for i in data:
        curval = int(i)
        if curval>300:
            while curval>300:
                curval=int(curval/10)
        if curval%10 !=0:
            curval = int(math.ceil(curval/10)*10)

        fields[curval]+=1
    plt.bar(list(fields.keys()), fields.values(), color='g')
    plt.show()




if __name__=='__main__':
    main()
