from S_BOX import sbox_fun
from key import make_key
from pad import depadding
import os
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

def decrypt_32(val,k):

    Ri,Li = val[:32], val[32:]
    Ri = Ri[::-1]
    Li = Li[::-1]

    for i in range(8):
        X = int(Ri,2) + int(k[i],2)                       # integer
        X = X%pow(2,32)
        X = format(X,'032b')                                # binary string
        X = sbox_fun(str(X))                                # string with f(x)(1-8) = sbox(x)(1-8)
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))

    for i in range(24):
        X = int(Ri,2) + int(k[7-i%8],2)                       # integer
        X = X%pow(2,32)
        X = format(X,'032b')                                # binary string
        X = sbox_fun(str(X))                                # string with f(x)(1-8) = sbox(x)(1-8)
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))


    return Li,Ri

def decrypt(binstring,k):

    A = []
    decstr = ""
    for x in range(len(binstring)//64):
        Li,Ri = decrypt_32(binstring[x*64:(x+1)*64],k)

        val = Ri[::-1] + Li[::-1]
        decstr = decstr + val
        #print(A)
    print(decstr, len(decstr))
    decstr = depadding(decstr)
    print(decstr, len(decstr))
    for j in range(0, len(decstr), 8):
        A.append( decstr[j:j+8] )
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    print(len(A))
    with open(os.path.join(__location__, "decrypted.txt"),'w') as enc:
        for i in (A):
            enc.write(chr(int(i,2)))                                                     #convert to char
    enc.close()
    #print( ''.join(A))
    print(A)