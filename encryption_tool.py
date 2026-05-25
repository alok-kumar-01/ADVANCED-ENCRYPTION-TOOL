from cryptography.fernet import Fernet

# Generate and save key
def generate_key():

    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("\n[+] Secret Key Generated Successfully")


# Load key
def load_key():

    return open("secret.key", "rb").read()


# Encrypt File
def encrypt_file():

    filename = input("\nEnter File Name to Encrypt: ")

    key = load_key()

    fernet = Fernet(key)

    try:

        with open(filename, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print("\n[+] File Encrypted Successfully")

    except:
        print("\n[-] Error Encrypting File")


# Decrypt File
def decrypt_file():

    filename = input("\nEnter File Name to Decrypt: ")

    key = load_key()

    fernet = Fernet(key)

    try:

        with open(filename, "rb") as enc_file:
            encrypted_data = enc_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(filename, "wb") as dec_file:
            dec_file.write(decrypted_data)

        print("\n[+] File Decrypted Successfully")

    except:
        print("\n[-] Error Decrypting File")


# Main Menu
while True:

    print("\n========== Advanced Encryption Tool ==========")

    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        encrypt_file()

    elif choice == "3":
        decrypt_file()

    elif choice == "4":
        print("\nExiting Program...")
        break

    else:
        print("\nInvalid Choice")