from libAES import AES_OBJECT
from libRSA import RSA_OBJECT
from Crypto.Cipher import AES

alice = RSA_OBJECT()
bob = RSA_OBJECT()
alice.load_PublicKey("Pub_A")
bob.load_PrivateKey("Pri_B", "bob")

with open('cyphertext', 'rb') as f: 
    cyphertext = f.read()

with open('cyphertext2', 'rb') as f: 
    cyphertext2 = f.read()

with open('cypherkey', 'rb') as f:
    cypherkey = f.read()

with open('sign', 'rb') as f:
    sign = f.read()

with open('nonce', 'rb') as f:
    nonce = f.read()

if alice.comprobar(cypherkey, sign):
    K = bob.descifrar(cypherkey)
    aes = AES_OBJECT(K, AES.MODE_GCM)
    text = aes.descifrar(cyphertext, nonce)
    text2 = aes.descifrar(cyphertext2, nonce)
    print(text)
    print(text2)
else:
    print("La firma no es valida")

