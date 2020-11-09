from libAES import cifrarAES, crear_AESKey, crear_AESSource
from libRSA import RSA_OBJECT

text = "Hola amigos y amigas de la seguridad"
text2 = "Adios amigos y amigas de la seguridad"

alice = RSA_OBJECT()
bob = RSA_OBJECT()
alice.load_PrivateKey("Pri_A", "alice")
bob.load_PublicKey("Pub_B")

K = crear_AESKey()

cypherkey = bob.cifrar(K)
sign = alice.firmar(cypherkey)

aes, nonce = crear_AESSource(K)
cyphertext, mac = cifrarAES(aes, text)
cyphertext2, mac2 = cifrarAES(aes, text2)

with open('cyphertext', 'wb') as f: 
    f.write(cyphertext)

with open('cyphertext2', 'wb') as f:
    f.write(cyphertext2)

with open('mac', 'wb') as f:
    f.write(mac)

with open('mac2', 'wb') as f:
    f.write(mac2)

with open('cypherkey', 'wb') as f:
    f.write(cypherkey)

with open('sign', 'wb') as f:
    f.write(sign)

with open('nonce', 'wb') as f:
    f.write(nonce)
