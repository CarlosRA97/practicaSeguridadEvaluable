from libAES import AES_OBJECT
from Crypto.Cipher import AES
from libRSA import RSA_OBJECT

text = "Hola amigos de la seguridad"

alice = RSA_OBJECT()
alice.load_PrivateKey("Pri_A", "alice")
bob = RSA_OBJECT()
bob.load_PublicKey("Pub_B")

K = AES_OBJECT.generarClave()
nonce = AES_OBJECT.generarIV()

cypherkey = bob.cifrar(K)
sign = alice.firmar(cypherkey)

aes = AES_OBJECT(K, AES.MODE_GCM)
cyphertext = aes.cifrar(text, nonce)

with open('cyphertext', 'wb') as f: 
    f.write(cyphertext)

with open('cypherkey', 'wb') as f:
    f.write(cypherkey)

with open('sign', 'wb') as f:
    f.write(sign)

with open('nonce', 'wb') as f:
    f.write(nonce)
