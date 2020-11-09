from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_OBJECT:
    BLOCK_SIZE_AES = 16 # AES: Bloque de 128 bits
    def __init__(self, key, mode=AES.MODE_CBC):
        """Inicializa las variables locales"""
        self.key = key
        self.mode = mode

    @staticmethod
    def generarClave():
        return get_random_bytes(AES_OBJECT.BLOCK_SIZE_AES)

    @staticmethod
    def generarIV():
        return get_random_bytes(AES_OBJECT.BLOCK_SIZE_AES)

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (de tipo String) con una IV específica, y
        devuelve el texto cifrado binario"""
        return self.aes_factory(self.mode, IV).encrypt(pad(cadena.encode("utf-8"), self.BLOCK_SIZE_AES))

    def descifrar(self, cifrado, IV):
        """Descifra el parámetro cifrado (de tipo binario) con una IV específica, y
        devuelve la cadena en claro de tipo String"""
        return unpad(
                self.aes_factory(self.mode, IV).decrypt(cifrado),
                self.BLOCK_SIZE_AES
            ).decode("utf-8","ignore")

    def aes_factory(self, mode, IV):
        if mode == AES.MODE_ECB:
            return AES.new(self.key, mode)
        elif mode == AES.MODE_CBC:
            return AES.new(self.key, mode, IV)
        elif mode == AES.MODE_CTR:
            return AES.new(self.key, mode, nonce=IV)
        elif mode == AES.MODE_OFB or AES.MODE_CFB:
            return AES.new(self.key, mode, IV)
        elif mode == AES.MODE_GCM:
            return AES.new(self.key, mode, nonce=IV, mac_len=self.BLOCK_SIZE_AES)
