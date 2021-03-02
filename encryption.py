from S_BOX import sbox_fun
from KEY import make_key
from decryption import decrypt
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

def encrypt_32(val,k):

    Ri,Li = val[:32], val[32:]
    Ri = Ri[::-1]
    Li = Li[::-1]

    for i in range(24):
        X = int(Ri,2) + int(k[i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        Y = sbox_fun(str(X))
        Y = leftshift11(Y)
        
        Li = Ri
        Ri = str(format(int(Y,2)^int(Li,2),'016b'))

    for i in range(8):
        X = int(Ri,2) + int(k[7-i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        Y = sbox_fun(str(X))
        Y = leftshift11(Y)
                
        Li = Ri
        Ri = str(format(int(Y,2)^int(Li,2),'016b'))
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

    #key = input("Enter 32 Character Key: ")
    key = "1234567812345678123456781234567812345678123456781234567812345678"
    k = []
    k = make_key(key)
    val = ''.join(bin(ord(x)) for x in text).replace('b','')
    val = "00000000"
    key = "0000000000000000000000000000000000000000000000000000000000000000"
    print(len(val),len(key))

    Li,Ri = encrypt_32(val,k)

    val = Ri[::-1] + Li[::-1]
    A = []
    for j in range(0, 64, 8):
        A.append( val[j:j+8] )
    #print(A)
    for i in range(len(A)):
        A[i] = chr(int(A[i],2))
    #print( ''.join(A))
    print(A)
    print(val)

    print("would you like to decrypt? 1:Yes 2:Exit")
    choice = input()
    if choice == '1':
        decrypt(val)
    else:
        return