import os
import time
import argparse
from encryption import encrypt
from decryption import decrypt

def main(args):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    print("would you like to encrypt or decrypt?:")
    opt = int(input("1.Encrypt 2.Decrypt: "))

    if opt==1:
        encrypt(os.path.join(__location__, args.orig_file))
    else:
        decrypt()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Main Script to run the code')

    parser.add_argument('--main_file', type=str, default='original.txt', 
            help='the name of the file to be encrypted. This file must be placed in the data folder.')
    parser.add_argument('--key_file', type=str, default='key.txt', 
            help='the key for encryption, with size = 32 Characters. This file must be placed in the data folder.')
    parser.add_argument('--encrypted_file', type=str, default='encrypted.txt', 
            help='the name of the file to be decrypted. This file must be placed in the data folder.')

    args = parser.parse_args()
    
    main(args)