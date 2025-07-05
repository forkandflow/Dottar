import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password_input, hashed):
    return hash_password(password_input) == hashed