#import section

import os
from S_BOX import sbox_fun
from key import make_key
from pad import depadding

# left shifts the binary sting by 11 bits
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y


# decrypting a 64 bit block
def decrypt_32(val, k):

    Ri, Li = val[:32], val[32:]
    Ri = Ri[::-1]
    Li = Li[::-1]

    for i in range(8):
        X = int(Ri, 2) + int(k[i], 2)
        X = X % pow(2, 32)
        X = format(X, '032b')
        X = sbox_fun(str(X))
        X = leftshift11(X)

        Li, Ri = Ri, str(format(int(X, 2) ^ int(Li, 2), '032b'))

    for i in range(24):
        X = int(Ri, 2) + int(k[7-i % 8], 2)
        X = X % pow(2, 32)
        X = format(X, '032b')
        X = sbox_fun(str(X))
        X = leftshift11(X)

        Li, Ri = Ri, str(format(int(X, 2) ^ int(Li, 2), '032b'))

    return Li[::-1], Ri[::-1]


def decrypt(encryptedfile, keyfile, decryptedfile, k=None):

    if k is None:
        with open(keyfile, 'r') as f:
            key = f.read()

        k = list(make_key(key))
        f.close()
    
    if not os.path.isfile(encryptedfile):
        print("No Encrypted file found. Exiting")
        exit()
    
    with open(encryptedfile, 'r') as f:
        lines = f.read()

    binstring = ''.join(format(ord(i), '08b') for i in lines)
    f.close()

    decstr = ""
    for x in range(len(binstring)//64):
        Li, Ri = decrypt_32(binstring[x*64:(x+1)*64], k)
        decstr = decstr + Ri + Li

    #padding is removed
    decstr = depadding(decstr)

    with open(decryptedfile, 'w') as dnc:
        for j in range(0, len(decstr), 8):
            dnc.write(chr(int(decstr[j:j+8], 2)))

    dnc.close()


def decrypt_cbc(vectorfile, encryptedfile, keyfile, decryptedfile, k=None):
    if k is None:
        with open(keyfile, 'r') as f:
            key = f.read()

        k = list(make_key(key))
        f.close()

    if not os.path.isfile(encryptedfile):
        print("No Encrypted file found. Exiting")
        exit()

    with open(encryptedfile, 'r') as f:
        lines = f.read()

    binstring = ''.join(format(ord(i), '08b') for i in lines)
    f.close()

    decstr = ""

    ini_vect = ""

    with open(vectorfile, 'r') as f:
        ini_vect = f.read()
    init_vect = ''.join(format(ord(x), '08b') for x in ini_vect)

    for x in range(len(binstring)//64):
        block = binstring[x*64:(x+1)*64]
        Li, Ri = decrypt_32(block, k)
        val = Ri+Li

        XOR_res = [int(init_vect[j], 2) ^ int(val[j], 2) for j in range(64)]
        XOR_resl = ''.join(str(e) for e in XOR_res)

        decstr = decstr + XOR_resl
        init_vect = block

    #padding is removed
    decstr = depadding(decstr)

    with open(decryptedfile, 'w') as dnc:
        for j in range(0, len(decstr), 8):
            dnc.write(chr(int(decstr[j:j+8], 2)))

    dnc.close()