import sys
import base64
import argparse
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

def load_public_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def encrypt_with_public_key(message: bytes, public_key) -> bytes:
    return public_key.encrypt(
        message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None)
    )

def main():
    parser = argparse.ArgumentParser(description="Encrypt with RSA public key (OAEP-SHA256).")
    parser.add_argument("message", nargs="?", help="Message to encrypt. If omitted, reads from stdin.")
    parser.add_argument("--pub", default="public.pem", help="Path to RSA public key PEM (default: public.pem)")
    args = parser.parse_args()

    data = args.message.encode() if args.message is not None else sys.stdin.buffer.read()
    pub = load_public_key(args.pub)
    ct = encrypt_with_public_key(data, pub)
    print(base64.b64encode(ct).decode())

if __name__ == "__main__":
    main()