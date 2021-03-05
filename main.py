import os
import time
from encryption import encrypt
from decryption import decrypt

def main():

    print("would you like to encrypt or decrypt?:")
    opt = int(input("1.Encrypt 2.Decrypt: "))

    if opt==1:
        """
        print("encrypting",end='')
        for _ in range(3):
            time.sleep(1)
            print('.',end='')
        print('\n')
        """
        encrypt()
    else:
        decrypt()

if __name__ == "__main__":
    main()