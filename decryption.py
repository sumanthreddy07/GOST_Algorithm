from S_BOX import sbox_fun
from KEY import make_key

def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

def decrypt_32(val,k):

    Ri,Li = val[:32], val[32:]
    #Ri = Ri[::-1]
    #Li = Li[::-1]

    for i in range(1):
        X = int(Ri,2) + int(k[i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        Y = sbox_fun(str(X))
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

def decrypt(val,k):

    Li,Ri = decrypt_32(val,k)

    val = Ri + Li
    #val = Li[::-1] + Ri[::-1]
    A = []
    for j in range(0, 64, 8):
        A.append( val[j:j+8] )
    #print(A)
    for i in range(len(A)):
        A[i] = chr(int(A[i],2))
    #print( ''.join(A))
    print(A)
    print(val)