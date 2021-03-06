#padding the text to remove partially filled blocks
#padding with 00100000, ie ASCII code 32 (space) 

def padcode():
    return "00100000"

#adds the appropriate number of characters to fill the last block
def padding(string):
    padwith = padcode() #space

    num = len(string)%64
    if (num!=0):
        pad = (64 - num)//8
        string = string + padwith*pad

    return string

#padding is removed
def depadding(string):
    padwith = padcode()
    padwith = padwith[::-1]
    string = string[::-1]

    while (string[:8]==padwith):
        string = string[8:]

    return string[::-1]