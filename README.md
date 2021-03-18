# GOST Algorithm

>Symmetric key block ciphers are the most common encryption methods in cryptographic systems. These ciphers are used as main blocks for the Random Number Generators, Hash Functions and Message Authentication Codes(MAC). GOST is an abbreviation of **"Gosudarstvennyi Standard"** or **"Government Standard"**, a cryptography algorithm made in Russia. This algorithm is a rival of the DES algorithm created by the United States. Structurally, this algorithm is very similar to the DES algorithm. The algorithm is simple encryption algorithm which has some processes as many as 32 rounds and uses 64-bit block cipher with 256-bit key. GOST method also uses the S-Box 8 pieces of permanent and XOR operations and Rotate Left Shift.

## GOST Structure

>1. Key Store Unit (KSU) stores 256-bit string by 32-bit register (K0, K1, …, K7).
>2. Two of 32 bit register (R1, R2)
>3. 32 bit adder modulo 232 (CM1)
>4. Bitwise Adder XOR (CM2)
>5. Substitusion block (S), an eight of 64 bit SBox.
>6. Left rotation shift register (R),11 bit.

<p align="center">
<img src="images/basic_steps.png">
</p>
<p align="center">
Basic Steps of GOST Algorithm
</p>

## Encryption and Decryption Block Formulas
>In this structure n is the length of the block, n length block is divided into the L and R blocks which’s length is n/2.
```
L(i) = R(i-1)
R(i) = L(i-1)^ƒ( [R(i-1)+K(i)]%2³² )
```
>The main advantage of this structure is that it makes the algorithm reversible, means that encryption and decryption is the same function.
```
L(i-1) ^ ƒ( [R(i-1)+K(i)]%2³² ) ^ ƒ( [R(i-1)+K(i)]%2³² ) = L(i-1)
```
<p align="center">
<img src="images/one_round_encryption.png">
</p>
<p align="center">
One Round Encryption
</p>

<p align="center">
<img src="images/subkey_sequence.png">
</p>
<p align="center">
Subkey Sequence
</p>

## Usage

- Place the text to be encrypted in a file (default file is 'encrypted.txt' but can be changed by using the optional arguments)
- Place the 32 charcter key text in the key.txt file

### Run
```bash
$ python3 src/main.py <optional arguments>
```

### Optional Arguments
```
--main_file = nameofthefile.txt
--encrypted_file = nameofthefile.txt
--key_file = nameofthefile.txt
--decrypted_file = nameofthefile.txt

for more info: python3 src/main.py --help
```
## References

>1. Muhammad Iqbal, Yudi Sahputra, Andysah Putera Utama Siahaan, ***The Understanding of GOST Crytography Technique***, 2016
>2. H. AKTAŞ, ***Implementation of GOST 28147-89 Encryption and Decryption Algorithm on FPGA***, 2018
