from encryption import encrypt
from decryption import decrypt

def main():

    print("would you like to encrypt or decrypt?:")
    opt = int(input("1.Encrypt 2.Decrypt: "))

    if opt==1:
        encrypt()
    else:
        decrypt()

if __name__ == "__main__":
    main()