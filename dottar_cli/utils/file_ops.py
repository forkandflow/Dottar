from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_blob(data, password):
    f = Fernet(generate_key(password))
    return f.encrypt(data)

def decrypt_blob(data, password):
    f = Fernet(generate_key(password))
    return f.decrypt(data)
