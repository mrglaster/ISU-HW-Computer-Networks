import math
import random
import base64
MINPRIME = 1
MAXPRIME = 200


def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True




def encrypt_textmessage(text_message, e, n):
    letters = []
    for i in text_message:
        current_num = ord(i)
        newer_num = rsa_encrypt(current_num, e, n)
        letters.append(base64.b64encode(chr(newer_num).encode('utf-8')))
    return letters

def decrypt_textmessage(encoded_message, d, n):
    letters = []
    for i in encoded_message:
        msg_bytes = base64.b64decode(i)
        curchar = msg_bytes.decode('utf-8')
        curnum = ord(curchar)
        rnum = rsa_decrypt(curnum, d, n)
        letters.append(chr(rnum))
    for i in letters:
        print(i, end='')
    return letters



cached_primes = []
def generate_random_primes():
    global cached_primes
    for i in range(MINPRIME, MAXPRIME):
        if is_prime(i):
            cached_primes.append(i)
    first = random.randint(0, len(cached_primes))
    second = random.randint(0, len(cached_primes))
    if first == second:
        if first + 2 >= len(cached_primes):
            second = first - 1
        else:
            second = first + 1
    return cached_primes[first], cached_primes[second]


def fastPow(number, argument):
    if argument<=0:
        return 1
    return number*fastPow(number, argument-1)

def generate_e(n, fi):
    global cached_primes
    position = random.randint(0, len(cached_primes))
    if cached_primes[position]<n:
        return cached_primes[position]
    return generate_e(n,fi)

def generate_d(fi,e):
    i =1
    while e*i%fi!=1:
        i+=1
    return i



def rsa_encrypt(message, e, n):
    return (message**e)%n

def rsa_decrypt(encrypted, d, n):
    return (encrypted**d)%n


def main():
    p, q = generate_random_primes()
    print(f"P={p}, Q={q}")
    n = p*q
    print(f"N={n}")
    fi = (p-1)*(q-1)
    print(f"Fi={fi}")
    e = generate_e(n, fi)
    d = generate_d(fi, e)
    print(f"E={e}, D={d}")

    print("\nTesting time!!!\n")
    for i in range(10,50):
        encrypted = rsa_encrypt(i, e, n)
        print(f"{i} -> {encrypted} -> {rsa_decrypt(encrypted, d, n)}")
    print("="*30+'\n')

    decrypt_textmessage(encrypt_textmessage("42 РєР°Рє СЃРјС‹СЃР» Р¶РёР·РЅРё ", e, n), d, n)
    decrypt_textmessage(encrypt_textmessage("РџСЂРѕРІРµСЂРєР° С€РёС„СЂРѕРІР°РЅРёСЏ-РґРµС€РёС„СЂРѕРІР°РЅРёСЏ! ", e, n), d, n)
    decrypt_textmessage(encrypt_textmessage("256РљР± С…РІР°С‚РёС‚ РІСЃРµРј! ", e, n), d, n)
if __name__=='__main__':
    main()
