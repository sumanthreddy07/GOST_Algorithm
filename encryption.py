from .S_BOX import sbox_fun
from .KEY import *

def encrypt_32(val):

    Ri,Li = val[:len(val)/2], val[len(val)/2:]
    Ri = Ri[::-1]
    Li = Li[::-1]

    for i in range(24):
        X = int(Ri,2) + int(k[i%8],2)
        X = "0:b".format(X%pow(2,32))
        Y = sbox_fun(X)

        Li = Ri
        Ri = "0:b".format(int(Y[:len(Y)/2],2)^int(Y[len(Y)/2:],2))

    for i in range(8):
        X = int(Ri,2) + int(k[7-i%8],2)
        X = "0:b".format(X%pow(2,32))
        Y = sbox_fun(X)

        Li = Ri
        Ri = "0:b".format(int(Y[:len(Y)/2],2)^int(Y[len(Y)/2:],2))

    return Li,Ri


def encrypt():

    """
    print("reading file...")
    with open('inputfile.txt') as f:
        lines = f.readlines()

    for line in lines:
        if len(line) > 8:

    block_size = 8
    """
    text = "abcdefgh"
    val = ''.join(format(ord(x), 'b') for x in text)
    Li,Ri = encrypt_32(val)

    val = Ri[::-1] + Li[::-1]

    print(val)

if __name__