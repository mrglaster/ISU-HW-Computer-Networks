WIKIPEDIA_LINK = 'https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D0%BA%D0%B0_%D0%BF%D0%BE%D0%B4%D1%81%D0%B5%D1%82%D0%B8'

def calculate_mask(netlen):
    netlen = int(netlen)
    if netlen<0 or netlen > 33:
        print("Wrong number!")
        exit(-1)
    str_wholenum = '1'*netlen+'0'*(32-netlen)
    result = ''
    for i in range(4):
        result+=str(int(str_wholenum[:8],2))+'.'
        str_wholenum = str_wholenum[8:]
    result = result[:len(result)-1]
    return result

def main():
    print('Select mode: input by ur hands or set values automaticly (0/1)')
    answer = int(input())
    if not answer:
        print("Input amount of '1' bits")
        inputnum = int(input())
        print("mask is: ", calculate_mask(inputnum))
    else:
        for i in range(0, 33):
            print("For /"+str(i)+" answer is: ", calculate_mask(i))
        print()
        print('='*35)
        print("You can compare results with: ", WIKIPEDIA_LINK)



if __name__=='__main__':
    main()