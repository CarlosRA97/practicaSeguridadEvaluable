from libAES import AES_OBJECT
from libRSA import RSA_OBJECT
from Crypto.Cipher import AES

text = "Hola amigos y amigas de la seguridad"
text2 = "Adios amigos y amigas de la seguridad"

alice = RSA_OBJECT()
bob = RSA_OBJECT()
alice.load_PrivateKey("Pri_A", "alice")
bob.load_PublicKey("Pub_B")

K = AES_OBJECT.generarClave()
nonce = AES_OBJECT.generarIV()

cypherkey = bob.cifrar(K)
sign = alice.firmar(cypherkey)

aes = AES_OBJECT(K, AES.MODE_GCM)
cyphertext = aes.cifrar(text, nonce)
cyphertext2 = aes.cifrar(text2, nonce)

with open('cyphertext', 'wb') as f: 
    f.write(cyphertext)

with open('cyphertext2', 'wb') as f:
    f.write(cyphertext2)

with open('cypherkey', 'wb') as f:
    f.write(cypherkey)

with open('sign', 'wb') as f:
    f.write(sign)

with open('nonce', 'wb') as f:
    f.write(nonce)
