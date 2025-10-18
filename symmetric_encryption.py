from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """Decrypt a message using the provided key."""
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Generate a new encryption key
    key = generate_key()
    print(f"Generated key (keep this secret!): {key.decode()}")
    
    # Get the message to encrypt
    message = input("Enter a message to encrypt: ")
    
    # Encrypt the message
    encrypted = encrypt_message(message, key)
    print(f"\nEncrypted message (base64): {base64.b64encode(encrypted).decode()}")
    
    # Decrypt the message
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()