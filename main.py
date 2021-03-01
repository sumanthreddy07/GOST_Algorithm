from .encryption import encrypt_main
from .decryption import decrypt_main

def main():

    print("would you like to encrypt or decrypt?:")
    opt = int(input("1.Encrypt 2.Decrypt: \n"))

    if opt==1:
        encrypt_main()
    else:
        decrypt_main()



if __name__ == "__main__":
    main()