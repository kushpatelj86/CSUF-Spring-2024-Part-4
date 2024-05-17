### To install the pycryptodome library ####
# sudo apt install python3-pip
# sudo pip3 install pycryptodomex
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Cryptodome.Cipher import AES

######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes)


masterkey = open("alicemasterkey.txt","r")

lines = masterkey.readlines()

key = lines[0].strip()

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes

file = open("msg2a.txt",'rb')
cipherText = encCipher.encrypt(file)

print("Cipher text: ", cipherText)

file = open("msg2a.txt.enc", "wb").write(cipherText)



