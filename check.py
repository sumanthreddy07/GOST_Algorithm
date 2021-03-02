char_key = "12345678123456781234567812345678"

bin_key = ''.join(format(ord(x),'08b') for x in char_key)
    A = []
    for j in range(0, 256, 8):
        A.append( bin_key[j:j+8] )
    
    return A