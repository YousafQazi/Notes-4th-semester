"""
Task 3: Digital Signature
Note: Install with: pip install cryptography
"""

import sys
import hashlib
import binascii

# Try to import, guide installation if missing
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    from cryptography.exceptions import InvalidSignature
    print(" Cryptography library is installed")
except ImportError:
    print("\n Cryptography library is not installed!")
    print("Please install it using: pip install cryptography")
    print("Then run this script again.")
    sys.exit(1)

def generate_keys():
    """Generate RSA keys for signing."""
    print("\n1. Generating RSA key pair...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def create_hash(message):
    """Create SHA256 hash of message."""
    print("\n2. Creating hash of message...")
    sha256_hash = hashlib.sha256(message.encode()).digest()
    print(f"   Message: '{message}'")
    print(f"   SHA256 Hash (hex): {binascii.hexlify(sha256_hash).decode()}")
    return sha256_hash

def sign_message(message, private_key):
    """Sign message with private key."""
    print("\n3. Signing message...")
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(f"   Signature (hex): {binascii.hexlify(signature).decode()}")
    return signature

def verify_signature(message, signature, public_key):
    """Verify signature with public key."""
    print("\n4. Verifying signature...")
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("    SIGNATURE IS VALID")
        return True
    except InvalidSignature:
        print("    SIGNATURE IS INVALID")
        return False

def main():
    print("=" * 50)
    print("TASK 3: DIGITAL SIGNATURE")
    print("=" * 50)
    
    # Generate keys
    private_key, public_key = generate_keys()
    
    # Get message
    message = input("\nEnter message to sign: ").strip()
    if not message:
        message = "Important document needs signing"
    
    # Create hash
    message_hash = create_hash(message)
    
    # Sign message
    signature = sign_message(message, private_key)
    
    # Verify signature (should pass)
    print("\n" + "-" * 50)
    print("TEST 1: Verify with original message")
    print("-" * 50)
    verify_signature(message, signature, public_key)
    
    # Test with tampered message (should fail)
    print("\n" + "-" * 50)
    print("TEST 2: Verify with tampered message")
    print("-" * 50)
    tampered_message = message + "!"  # Add one character
    print(f"   Tampered message: '{tampered_message}'")
    print(f"   (Added '!' at the end)")
    
    # Create hash of tampered message
    tampered_hash = hashlib.sha256(tampered_message.encode()).digest()
    print(f"   Tampered hash (hex): {binascii.hexlify(tampered_hash).decode()}")
    
    # Try to verify tampered message
    verify_signature(tampered_message, signature, public_key)
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    print("1. Original message signature: VALID")
    print("2. Tampered message signature: INVALID")
    print("3. Digital signature ensures message integrity")
    print("=" * 50)

if __name__ == "__main__":
    main()