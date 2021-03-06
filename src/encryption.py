#import section

from S_BOX import sbox_fun
from key import make_key
from decryption import decrypt
from pad import padding 

#left shifts the binary sting by 11 bits
def leftshift11(Y):
    Y = Y[11:]+Y[:11]
    return Y

#encrypting a 64 bit block 
def encrypt_32(val,k):

    Li,Ri = val[:32], val[32:]
    Ri = Ri[::-1]
    Li = Li[::-1]
    
    for i in range(24):
        X = int(Ri,2) + int(k[i%8],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        X = sbox_fun(str(X))
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))
    
    for i in range(8):
        X = int(Ri,2) + int(k[7-i],2)
        X = X%pow(2,32)
        X = format(X,'032b')
        X = sbox_fun(str(X))
        X = leftshift11(X)
        
        Li,Ri = Ri,str(format(int(X,2)^int(Li,2),'032b'))

    return Li[::-1],Ri[::-1]


def encrypt(mainfile,keyfile,encryptedfile,decryptedfile):
    
    with open(keyfile,'r') as f:
        key = f.read()
    
    k = list(make_key(key))
    f.close()
    
    with open(mainfile,'r') as f:
        lines = f.read()
    
    binstring = ''.join(format(ord(i), '08b') for i in lines)
    f.close()

    #padding to avoid partially filled blocks
    binstring = padding(binstring)

    with open(encryptedfile,'w') as enc:
        for x in range(len(binstring)//64):
            Li,Ri = encrypt_32(binstring[x*64:(x+1)*64],k)

            val = Li + Ri
        
            for j in range(0, 64, 8):
                enc.write(chr(int(val[j:j+8],2)))
    enc.close()

    print("would you like to decrypt?")
    print("1.Yes 2.Exit: ")
    
    choice = input()
    if choice == '1':
        decrypt(encryptedfile,keyfile,decryptedfile,k)
    else:
        return