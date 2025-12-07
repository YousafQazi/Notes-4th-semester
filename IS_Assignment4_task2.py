"""
Task 2: RSA with PyCryptodome
Note: Install with: pip install pycryptodome
"""

import sys

# Try to import, guide installation if missing
try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii
    print(" PyCryptodome is installed")
except ImportError:
    print("\n PyCryptodome is not installed!")
    print("Please install it using: pip install pycryptodome")
    print("Then run this script again.")
    sys.exit(1)

def generate_keys():
    """Generate 2048-bit RSA keys."""
    print("\n1. Generating 2048-bit RSA key pair...")
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def encrypt_message(message, public_key):
    """Encrypt message with public key."""
    print("\n2. Encrypting message...")
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted, private_key):
    """Decrypt message with private key."""
    print("\n3. Decrypting message...")
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode()

def main():
    print("=" * 50)
    print("TASK 2: RSA WITH PyCryptodome")
    print("=" * 50)
    
    # Generate keys
    private_key, public_key = generate_keys()
    
    # Show key info
    print(f"   Modulus (n): {public_key.n}")
    print(f"   Public exponent (e): {public_key.e}")
    print(f"   Key size: {public_key.size_in_bits()} bits")
    
    # Get message
    message = input("\nEnter message to encrypt: ").strip()
    if not message:
        message = "Hello RSA from PyCryptodome!"
    
    # Encrypt
    encrypted = encrypt_message(message, public_key)
    print(f"\n   Original message: '{message}'")
    print(f"   Encrypted (hex): {binascii.hexlify(encrypted).decode()}")
    
    # Decrypt
    decrypted = decrypt_message(encrypted, private_key)
    print(f"\n   Decrypted message: '{decrypted}'")
    
    # Verify
    print(f"\n4. Verification:")
    if message == decrypted:
        print("    SUCCESS: Encryption/Decryption works!")
    else:
        print("    FAILURE: Something went wrong!")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()