import os
from S_BOX import sbox_fun
from key import make_key
from decryption import decrypt
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

def encrypt_32(val,k):

    Li,Ri = val[:32], val[32:]
    Ri = Ri[::-1]
    Li = Li[::-1]

    for i in range(24):
        X = int(Ri,2) + int(k[i%8],2)                       # integer
        X = X%pow(2,32)
        X = format(X,'032b')                                # binary string
        X = sbox_fun(str(X))                                # string with f(x)(1-8) = sbox(x)(1-8)
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))
    
    for i in range(8):
        X = int(Ri,2) + int(k[7-i],2)                       # integer
        X = X%pow(2,32)
        X = format(X,'032b')                                # binary string
        X = sbox_fun(str(X))                                # string with f(x)(1-8) = sbox(x)(1-8)
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))

    return Li,Ri


def encrypt():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'original.txt'),'r') as f:
        lines = f.read()

    print(lines)
    binstring = ''.join(format(ord(i), '08b') for i in lines)
    
    #key = input("Enter 32 Character Key: ")
    key = "12345678123456781234567812345678"                                        #key is string-number
    k = []
    k = make_key(key)                                                               #returns a list of 8 keys each of size 32 bits

    Li,Ri = encrypt_32(binstring,k)

    val = Li[::-1] + Ri[::-1]
    
    A = []
    for j in range(0, 64, 8):
        A.append( val[j:j+8] )                                                      #convert to binary chars
    #print(A)
    with open(os.path.join(__location__, "encrypted.txt"),'a') as enc:
        for i in (A):
            enc.write(chr(int(i,2)))                                                     #convert to char
        enc.close()

    #print(A)

    print("would you like to decrypt? 1:Yes 2:Exit")
    choice = input()
    if choice == '1':
        decrypt(val,k)
    else:
        return