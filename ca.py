from libRSA import RSA_OBJECT

alice = RSA_OBJECT()
bob = RSA_OBJECT()

alice.create_KeyPair()
bob.create_KeyPair()

alice.save_PublicKey("Pub_A")
alice.save_PrivateKey("Pri_A", "alice")

bob.save_PublicKey("Pub_B")
bob.save_PrivateKey("Pri_B", "bob")
