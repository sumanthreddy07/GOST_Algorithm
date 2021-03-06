#key function converts the 32 character text into a 256 bit binary string and then into 32 bit strings (8 subkeys)

#char_key = 32 Characters
#bin_key = 256 bits
#K is a list containing K[0]=bin_key[0:32], K[1]=bin_key[32:64] ... K[7]=bin_key[224:256]

def make_key(char_key):
    if len(char_key)!=32:
        print("Wrong Key Size. Exiting...")
        exit()
    
    bin_key = ''.join(format(ord(x),'08b') for x in char_key)
    K = []
    for j in range(0, 256, 32):
        K.append( bin_key[j:j+32] )
    
    return K