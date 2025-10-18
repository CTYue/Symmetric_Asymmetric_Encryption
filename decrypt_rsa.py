import os
import sys
import base64
import argparse
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

def load_private_key(path: str, password: bytes | None):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=password)

def decrypt_with_private_key(ciphertext: bytes, private_key) -> bytes:
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None)
    )

def main():
    parser = argparse.ArgumentParser(description="Decrypt with RSA private key (OAEP-SHA256).")
    parser.add_argument("ciphertext_b64", nargs="?", help="Base64 ciphertext. If omitted, reads from stdin.")
    parser.add_argument("--priv", default="private.pem", help="Path to RSA private key PEM (default: private.pem)")
    parser.add_argument("--pass-env", default="PRIVATE_KEY_PASSWORD",
                        help="Env var name containing private key password (default: PRIVATE_KEY_PASSWORD)")
    args = parser.parse_args()

    pw_env = os.getenv(args.pass_env)
    password = pw_env.encode() if pw_env else None

    b64 = args.ciphertext_b64 if args.ciphertext_b64 is not None else sys.stdin.read()
    ct = base64.b64decode(b64.strip())
    priv = load_private_key(args.priv, password=password)
    pt = decrypt_with_private_key(ct, priv)
    sys.stdout.write(pt.decode())

if __name__ == "__main__":
    main()