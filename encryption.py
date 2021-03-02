from S_BOX import sbox_fun
from KEY import make_key
from decryption import decrypt
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

def encrypt_32(val,k):

    Li,Ri = val[:32], val[32:]
    #Ri = Ri[::-1]
    #Li = Li[::-1]

    for i in range(1):
        X = int(Ri,2) + int(k[i%8],2)                       # integer
        X = X%pow(2,32)
        X = format(X,'032b')                                # binary string
        Y = sbox_fun(str(X))                                # string with f(x)(1-8) = sbox(x)(1-8)
        Y = leftshift11(Y)
        
        Li,Ri = Ri,str(format(int(Y,2)^int(Li,2),'032b'))

    """
    for i in range(24):
        X = int(Ri,2) + int(k[i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        Y = sbox_fun(str(X))
        Y = leftshift11(Y)
        
        Li = Ri
        Ri = str(format(int(Y,2)^int(Li,2),'032b'))

    for i in range(8):
        X = int(Ri,2) + int(k[7-i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        Y = sbox_fun(str(X))
        Y = leftshift11(Y)
                
        Li = Ri
        Ri = str(format(int(Y,2)^int(Li,2),'032b'))
    """
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
    key = "12345678123456781234567812345678"                                        #key is string-number
    #text = "00000000"
    #key = "0000000000000000000000000000000000000000000000000000000000000000"
    k = []
    k = make_key(key)                                                               #returns a list of 8 keys each of size 32 bits
    val = ""
    for x in text:
        val = val + format(ord(x),'08b')                                            #convert text to binary string

    Li,Ri = encrypt_32(val,k)

    #val = Ri[::-1] + Li[::-1]
    val = Li + Ri
    A = []
    for j in range(0, 64, 8):
        A.append( val[j:j+8] )                                                      #convert to binary chars
    #print(A)
    for i in range(len(A)):
        A[i] = chr(int(A[i],2))                                                     #convert to char

    print(A)
    print(val)

    print("would you like to decrypt? 1:Yes 2:Exit")
    choice = input()
    if choice == '1':
        decrypt(val,k)
    else:
        return