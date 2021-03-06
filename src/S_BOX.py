#sbox matrix of the size 8X16 
def get_sbox():
    S_BOX=[
    [ 4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3 ],
    [ 14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9 ],
    [ 5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11 ],
	[ 7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3 ],
	[ 6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2 ],
    [ 4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14 ],
    [ 13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12 ],
    [ 1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12 ]]

    return S_BOX

#splits the 32 bit string (X) into 8 parts and replaces each one with its respective number from the sbox
def sbox_fun(X):

    A = []
    for j in range(0, 32, 4):
        A.append( int(X[j:j+4],2) )

    S_BOX = get_sbox()
    for j in range(8):
        A[j] = S_BOX[j][A[j]]
        A[j] = format(A[j],'04b')

    return ''.join(A)
