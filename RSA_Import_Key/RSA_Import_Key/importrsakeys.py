# Need to run the following commands if you get errors
# pip3 uninstall pycrypto
# pip3 install -U pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# Generate a public/private key pair
private_key = RSA.generate(1024)

# Get the private key
public_key = private_key.publickey()

# The private key bytes to print
privKeyBytes = private_key.exportKey(format='PEM') 


# The public key bytes to print
pubKeyBytes = public_key.exportKey(format='PEM') 

#print(privKeyBytes)
#print(pubKeyBytes)

# Save the private key
with open ("private.pem", "wb") as prv_file:
    prv_file.write(privKeyBytes)

# Save the public key
with open ("public.pem", "wb") as pub_file:
    pub_file.write(pubKeyBytes)


####################################################
# Now let's load those keys

# The public key and the private key
puKey = None
prKey = None

# Load the public key
with open ("private.pem", "rb") as prv_file:
	
	contents = prv_file.read()
	prKey = RSA.importKey(contents)


# Load the public key
with open ("public.pem", "rb") as pub_file:
	contents = pub_file.read()
	puKey = RSA.importKey(contents)

#puKey.encrypt("hello", 'x')

# Initielize the cipher with the key and encrypt
cipher = PKCS1_v1_5.new(puKey)
ciphertext = cipher.encrypt("hello".encode())
print("Ciphertext: ", ciphertext)

cipher = PKCS1_v1_5.new(prKey)
plaintext = cipher.decrypt(ciphertext, 1000)
print("Decrypted: ", plaintext)

