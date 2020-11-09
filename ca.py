from libRSA import crear_RSAKey, guardar_RSAKey_Privada, guardar_RSAKey_Publica

alice_key = crear_RSAKey()
bob_key = crear_RSAKey()

guardar_RSAKey_Publica("Pub_A", alice_key)
guardar_RSAKey_Privada("Pri_A", alice_key, "alice")

guardar_RSAKey_Publica("Pub_B", bob_key)
guardar_RSAKey_Privada("Pri_B", bob_key, "bob")
