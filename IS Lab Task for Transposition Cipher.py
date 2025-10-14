import random
import string
def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def generate_random_key(length):
    key_list = list(range(1, length + 1))
    random.shuffle(key_list)
    return ''.join(map(str, key_list))


def encode(key, plaintext):
   
    if not key:
        key = generate_random_key(len(plaintext))
        print(f"Generated Key: {key}")
    if len(plaintext) % len(key) != 0:
        padding_length = len(key) - (len(plaintext) % len(key))
        plaintext += ' ' * padding_length  

    order = {int(val): num for num, val in enumerate(key)}
    ciphertext = ''
    for part in split_len(plaintext, len(key)):
        for index in sorted(order.keys()):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                ciphertext += ' '
    return ciphertext

def decode(key, ciphertext):
    order = {int(val): num for num, val in enumerate(key)}
    key_order = sorted(order.keys())
    key_len = len(key)
    plaintext = ''

    for part in split_len(ciphertext, key_len):
        temp = [''] * key_len
        for i, index in enumerate(key_order):
            if i < len(part):
                temp[order[index]] = part[i]
        plaintext += ''.join(temp)
    return plaintext.strip()

def menu():
    while True:
        print("\n=== Transposition Cipher Menu ===")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key (leave blank for random key): ")
            ciphertext = encode(key, plaintext)
            print(f"Ciphertext: {ciphertext}")

        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ")
            plaintext = decode(key, ciphertext)
            print(f"Plaintext: {plaintext}")

        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

