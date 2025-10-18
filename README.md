# Symmetric & Asymmetric Encryption

A Python project demonstrating both symmetric (Fernet) and asymmetric (RSA) encryption methods using the `cryptography` library.

## Prerequisites

Install the required dependencies:

```bash
pip install cryptography
```

## Project Structure

- **`symmetric_encryption.py`** - Symmetric encryption using Fernet
- **`encrypt_rsa.py`** - RSA public key encryption
- **`decrypt_rsa.py`** - RSA private key decryption
- **`public.pem`** / **`private.pem`** - RSA key pairs (examples included)

---

## Symmetric Encryption (Fernet)

Symmetric encryption uses the same key for both encryption and decryption. The key must be kept secret and shared securely between parties.

### Usage

Run the interactive demo:

```bash
python symmetric_encryption.py
```

This will:
1. Generate a new encryption key
2. Prompt you to enter a message
3. Encrypt the message
4. Decrypt it back to verify

### Example

```
$ python symmetric_encryption.py
Generated key (keep this secret!): gAAAAABkX1Y2Z3...
Enter a message to encrypt: Hello World

Encrypted message (base64): Z0FBQUFBQmtYMVky...
Decrypted message: Hello World
```

### Using Fernet Functions in Your Code

```python
from symmetric_encryption import generate_key, encrypt_message, decrypt_message

# Generate a key (save this securely!)
key = generate_key()

# Encrypt
encrypted = encrypt_message("Secret message", key)

# Decrypt
decrypted = decrypt_message(encrypted, key)
```

---

## Asymmetric Encryption (RSA)

Asymmetric encryption uses a key pair: a **public key** for encryption and a **private key** for decryption. Anyone can encrypt with the public key, but only the holder of the private key can decrypt.

### Generating RSA Key Pairs

First, generate your own RSA key pair (if not using the included examples):

```bash
# Generate private key (with password protection)
openssl genrsa -aes256 -out private.pem 2048

# Generate public key from private key
openssl rsa -in private.pem -pubout -out public.pem

# Or without password protection:
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

### Encrypting with Public Key

Encrypt a message using the public key:

```bash
# Direct message
python encrypt_rsa.py "Hello, World!"

# With custom public key
python encrypt_rsa.py "Secret message" --pub public.pem

# From stdin
echo "Secret data" | python encrypt_rsa.py

# Save to file
python encrypt_rsa.py "Confidential" > ciphertext.b64
```

**Output:** Base64-encoded ciphertext

### Decrypting with Private Key

Decrypt a message using the private key:

```bash
# Direct ciphertext
python decrypt_rsa.py "base64_ciphertext_here"

# With custom private key
python decrypt_rsa.py "base64_ciphertext" --priv private.pem

# From stdin
cat ciphertext.b64 | python decrypt_rsa.py

# From file
python decrypt_rsa.py < ciphertext.b64

# With password-protected private key
export PRIVATE_KEY_PASSWORD="your_password"
python decrypt_rsa.py "base64_ciphertext"
```

### Complete Encryption/Decryption Example

```bash
# Encrypt
CIPHERTEXT=$(python encrypt_rsa.py "Hello RSA!")
echo "Encrypted: $CIPHERTEXT"

# Decrypt
PLAINTEXT=$(echo "$CIPHERTEXT" | python decrypt_rsa.py)
echo "Decrypted: $PLAINTEXT"
```

### Advanced Options

#### encrypt_rsa.py

```bash
python encrypt_rsa.py --help
```

Options:
- `message` - Message to encrypt (optional, reads from stdin if omitted)
- `--pub` - Path to RSA public key PEM (default: `public.pem`)

#### decrypt_rsa.py

```bash
python decrypt_rsa.py --help
```

Options:
- `ciphertext_b64` - Base64 ciphertext (optional, reads from stdin if omitted)
- `--priv` - Path to RSA private key PEM (default: `private.pem`)
- `--pass-env` - Environment variable name containing private key password (default: `PRIVATE_KEY_PASSWORD`)

---

## When to Use Each Method

### Use Symmetric Encryption (Fernet) when:
- ✅ Both parties can securely share the same key
- ✅ You need fast encryption/decryption
- ✅ Encrypting large amounts of data
- ✅ Both parties trust each other with the shared secret

### Use Asymmetric Encryption (RSA) when:
- ✅ You need to share encrypted messages without sharing keys
- ✅ The sender only needs the public key (no secret sharing required)
- ✅ You want to ensure only the private key holder can decrypt
- ✅ Implementing digital signatures or key exchange protocols

**Note:** RSA is slower and limited in message size. For large data, use RSA to encrypt a symmetric key, then use that symmetric key to encrypt the actual data (hybrid encryption).

---

## Security Notes

⚠️ **Important Security Considerations:**

1. **Never commit private keys to version control**
2. **Keep private keys secure** - Use strong passwords and proper file permissions
3. **The included key pairs are examples only** - Generate your own for production use
4. **RSA message size limit** - Cannot encrypt messages larger than key size minus padding (typically ~190 bytes for 2048-bit keys)
5. **Use password-protected private keys** for sensitive applications
6. **Store keys securely** - Consider using key management services or hardware security modules (HSMs) for production

---

## License

This project is for educational purposes demonstrating encryption techniques.
