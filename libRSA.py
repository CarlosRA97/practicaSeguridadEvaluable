from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pss

class RSA_OBJECT:
    
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_KeyPair(self):
        key = RSA.generate(2048)
        self.private_key = key
        self.public_key = key.publickey()
    
    def save_PrivateKey(self, fichero, password):
        key_cifrada = self.private_key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
        with open(fichero, "wb") as file_out:
            file_out.write(key_cifrada)

    def load_PrivateKey(self, fichero, password):
        key_cifrada = open(fichero, "rb").read()
        self.private_key = RSA.import_key(key_cifrada, passphrase=password)

    def save_PublicKey(self, fichero):
        key_pub = self.public_key.export_key()
        with open(fichero, "wb") as file_out:
            file_out.write(key_pub)

    def load_PublicKey(self, fichero):
        keyFile = open(fichero, "rb").read()
        self.public_key = RSA.import_key(keyFile)

    def cifrar(self, cadena):
        try:
            datos = cadena
            engineRSACifrado = PKCS1_OAEP.new(self.public_key)
            cifrado = engineRSACifrado.encrypt(datos)
            return cifrado
        except (ValueError, TypeError):
            return None

    def descifrar(self, cifrado):
        try:
            engineRSADescifrado = PKCS1_OAEP.new(self.private_key)
            datos = engineRSADescifrado.decrypt(cifrado)
            cadena = datos
            return cadena
        except (ValueError, TypeError):
            return None

    def firmar(self, texto):
        # La firma se realiza sobre el hash del texto (h)
        try:
            h = SHA256.new(texto)
            signature = pss.new(self.private_key).sign(h)
            return signature
        except (ValueError, TypeError):
            return None

    def comprobar(self, texto, firma):
        # Comprobamos que la firma coincide con el hash (h)
        h = SHA256.new(texto)
        verifier = pss.new(self.public_key)
        try:
            verifier.verify(h, firma)
            return True
        except (ValueError, TypeError):
            return False
