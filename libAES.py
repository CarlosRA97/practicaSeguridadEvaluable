from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

class AES_OBJECT:
    BLOCK_SIZE_AES = 16 # AES: Bloque de 128 bits
    def __init__(self, key, mode, IV):
        """Inicializa las variables locales"""
        self.key = key
        self.mode = mode
        self.IV = IV

    @staticmethod
    def generarClave():
        return get_random_bytes(AES_OBJECT.BLOCK_SIZE_AES)

    @staticmethod
    def generarIV():
        return get_random_bytes(AES_OBJECT.BLOCK_SIZE_AES)

    def cifrar(self, cadena):
        """Cifra el parámetro cadena (de tipo String) con una IV específica, y
        devuelve el texto cifrado binario"""
        return self.aes_factory().encrypt_and_digest(pad(cadena.encode("utf-8"), self.BLOCK_SIZE_AES))

    def descifrar(self, cifrado, mac):
        """Descifra el parámetro cifrado (de tipo binario) con una IV específica, y
        devuelve la cadena en claro de tipo String"""
        return unpad(
                self.aes_factory().decrypt_and_verify(cifrado, mac),
                self.BLOCK_SIZE_AES
            ).decode("utf-8","ignore")

    def aes_factory(self):
        if self.mode == AES.MODE_ECB:
            return AES.new(self.key, self.mode)
        elif self.mode == AES.MODE_CBC:
            return AES.new(self.key, self.mode, self.IV)
        elif self.mode == AES.MODE_CTR:
            return AES.new(self.key, self.mode, nonce=self.IV)
        elif self.mode == AES.MODE_OFB or AES.MODE_CFB:
            return AES.new(self.key, self.mode, self.IV)
        elif self.mode == AES.MODE_GCM:
            return AES.new(self.key, self.mode, nonce=self.IV, mac_len=self.BLOCK_SIZE_AES)

def crear_AESKey():
    """Devuelve un número aleatorio de 16 bytes - 128 bits"""
    return AES_OBJECT.generarClave()

def crear_AESSource(key_16):
    """Crea un objeto aes junto con el nonce inicial para enviar datos. """
    # INCLUIR CODIGO AQUI
    return aes_object, nonce_16_ini
def crear_AESDestination(key_16, nonce_16_ini):
    """Crea un objeto aes para recibir datos"""
    # INCLUIR CODIGO AQUI
    return aes_object
def cifrarAES(aes_cifrado, cadena):
    """Cifra el parametro cadena (de tipo String), y devuelve el texto cifrado binario
    Y el mac"""
    # INCLUIR CODIGO AQUI
    return datos_cifrado, mac_cifrado
def descifrarAES(aes_descifrado, datos, mac):
    """Descifra el parametro datos (de tipo binario), y devuelve la cadena en claro de
    tipo String.
    También comprueba si el mac es correcto"""
    # INCLUIR CODIGO AQUI con un try...except -> return datos_claro o return false