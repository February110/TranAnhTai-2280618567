from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self, key_size=2048, key_path='keys/'):
        self.key_size = key_size
        self.key_path = key_path
        if not os.path.exists(self.key_path):
            os.makedirs(self.key_path)

    def generate_keys(self):
        key = RSA.generate(self.key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(os.path.join(self.key_path, "private.pem"), "wb") as priv_file:
            priv_file.write(private_key)
        with open(os.path.join(self.key_path, "public.pem"), "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        try:
            with open(os.path.join(self.key_path, "private.pem"), "rb") as priv_file:
                private_key = RSA.import_key(priv_file.read())
            with open(os.path.join(self.key_path, "public.pem"), "rb") as pub_file:
                public_key = RSA.import_key(pub_file.read())
            return private_key, public_key
        except FileNotFoundError:
            raise Exception("Key files not found. Generate keys first.")

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        return encrypted_message

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')
        return decrypted_message

    def sign(self, message, private_key):
        h = SHA256.new(message.encode('utf-8'))
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode('utf-8'))
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
