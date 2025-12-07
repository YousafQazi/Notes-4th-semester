"""
Task 1: Simple RSA Implementation (Without Libraries)
"""

import random

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """Find greatest common divisor."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Find modular inverse using extended Euclidean algorithm."""
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys():
    """Generate RSA keys with small primes."""
    # Small primes for demonstration
    primes = [p for p in range(11, 50) if is_prime(p)]
    p, q = random.sample(primes, 2)
    
    n = p * q
    phi = (p-1) * (q-1)
    
    # Choose e (public exponent)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    
    # Calculate d (private exponent)
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n), p, q

def encrypt(msg, public_key):
    """Encrypt message using public key."""
    e, n = public_key
    # Convert string to number
    m = int(''.join(str(ord(c)).zfill(3) for c in msg))
    if m >= n:
        # Take only first 2 characters if too large
        m = int(''.join(str(ord(c)).zfill(3) for c in msg[:2]))
    # RSA encryption: c = m^e mod n
    c = pow(m, e, n)
    return c

def decrypt(cipher, private_key):
    """Decrypt cipher using private key."""
    d, n = private_key
    # RSA decryption: m = c^d mod n
    m = pow(cipher, d, n)
    
    # Convert number back to string
    m_str = str(m).zfill(6)  # Ensure 6 digits
    result = ""
    for i in range(0, len(m_str), 3):
        num = int(m_str[i:i+3])
        if 32 <= num <= 126:  # Printable ASCII
            result += chr(num)
    return result

def main():
    print("=" * 50)
    print("TASK 1: SIMPLE RSA IMPLEMENTATION")
    print("=" * 50)
    
    # Generate keys
    public_key, private_key, p, q = generate_keys()
    print(f"\n1. Key Generation:")
    print(f"   Prime p: {p}")
    print(f"   Prime q: {q}")
    print(f"   n = p*q: {p*q}")
    print(f"   Public Key (e, n): {public_key}")
    print(f"   Private Key (d, n): {private_key}")
    
    # Encrypt
    message = "Hi"
    print(f"\n2. Encryption:")
    print(f"   Original message: '{message}'")
    cipher = encrypt(message, public_key)
    print(f"   Encrypted cipher: {cipher}")
    
    # Decrypt
    print(f"\n3. Decryption:")
    decrypted = decrypt(cipher, private_key)
    print(f"   Decrypted message: '{decrypted}'")
    
    # Verification
    print(f"\n4. Verification:")
    if message == decrypted:
        print("    SUCCESS: Messages match!")
    else:
        print("    FAILURE: Messages don't match!")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()