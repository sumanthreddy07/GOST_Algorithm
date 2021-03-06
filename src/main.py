#import section

import os
import argparse
from encryption import encrypt,encrypt_cbc
from decryption import decrypt,decrypt_cbc

#locate function returns the path for the txt files in the data folder
def locate(filename):
    __location__ = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
    return os.path.join(__location__,'data',filename)

def main(args):
    print("would you like to encrypt or decrypt?")
    opt = int(input("1.Encrypt 2.Decrypt: 3:EncryptCBC 4:DecryptCBC: "))

    if opt==1:
        encrypt( locate(args.main_file),locate(args.key_file),locate(args.encrypted_file),locate(args.decrypted_file))
    elif opt==2:
        decrypt( locate(args.encrypted_file),locate(args.key_file),locate(args.decrypted_file))
    elif opt==3:
        encrypt_cbc(locate(args.vector_file), locate(args.main_file),locate(args.key_file),locate(args.encrypted_file),locate(args.decrypted_file))
    else:
        decrypt_cbc(locate(args.vector_file), locate(args.encrypted_file),locate(args.key_file),locate(args.decrypted_file))



if __name__ == "__main__":
    
    #parser arguments
    parser = argparse.ArgumentParser(description='Main Script to run the code')

    parser.add_argument('--main_file', type=str, default='original.txt', 
            help='The name of the file to be encrypted. This file must be placed in the data folder.')
    
    parser.add_argument('--key_file', type=str, default='key.txt', 
            help='The key for encryption, with size = 32 Characters. This file must be placed in the data folder.')
    
    parser.add_argument('--encrypted_file', type=str, default='encrypted.txt', 
            help='The name of the file to be decrypted. This file must be placed in the data folder.')
    
    parser.add_argument('--decrypted_file', type=str, default='decrypted.txt', 
            help='The name of the file in which decrypted data is written. This file must be placed in the data folder.')

    parser.add_argument('--vector_file', type=str, default='vector.txt', 
            help='The initialization vector in string format .')

    args = parser.parse_args()
    
    main(args)