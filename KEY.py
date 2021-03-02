def make_key(char_key):
    bin_key = ''.join(format(ord(x),'08b') for x in char_key)
    A = []
    for j in range(0, 64, 8):
        A.append( bin_key[j:j+8] )
    
    return A