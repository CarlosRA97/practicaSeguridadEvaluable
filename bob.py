from libAES import crear_AESDestination, descifrarAES
from libRSA import RSA_OBJECT

alice = RSA_OBJECT()
bob = RSA_OBJECT()
alice.load_PublicKey("Pub_A")
bob.load_PrivateKey("Pri_B", "bob")

with open('cyphertext', 'rb') as f: 
    cyphertext = f.read()

with open('cyphertext2', 'rb') as f: 
    cyphertext2 = f.read()

with open('mac', 'rb') as f: 
    mac = f.read()

with open('mac2', 'rb') as f: 
    mac2 = f.read()

with open('cypherkey', 'rb') as f:
    cypherkey = f.read()

with open('sign', 'rb') as f:
    sign = f.read()

with open('nonce', 'rb') as f:
    nonce = f.read()

if alice.comprobar(cypherkey, sign):
    K = bob.descifrar(cypherkey)
    aes = crear_AESDestination(K, nonce)
    text = descifrarAES(aes, cyphertext, mac)
    text2 = descifrarAES(aes, cyphertext2, mac2)
    print(text)
    print(text2)
else:
    print("La firma no es valida")

