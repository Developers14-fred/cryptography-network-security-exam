import os
import sys
import hashlib
from cryptography.fernet import Fernet

def generate_or_load_key():
    """Loads key from parent directory to ensure it is not committed to Git."""
    key_file = os.path.join("..", "secret.key")
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        return key

def encrypt_file(file_path, key):
    """Encrypts source file and saves as .enc."""
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file_to_encrypt:
            data = file_to_encrypt.read()
        encrypted_data = f.encrypt(data)
        out_path = file_path + ".enc"
        with open(out_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        print(f"[+] File encrypted successfully: {out_path}")
        return out_path
    except Exception as e:
        print(f"[-] Encryption error: {e}")
        return None

def decrypt_file(encrypted_file_path, original_file_path, key):
    """Decrypts file and verifies matching content with original."""
    try:
        f = Fernet(key)
        with open(encrypted_file_path, "rb") as ef:
            encrypted_data = ef.read()
        decrypted_data = f.decrypt(encrypted_data)

        with open(original_file_path, "rb") as of:
            original_data = of.read()

        if decrypted_data == original_data:
            print("[+] Decryption successful: Contents match the original file.")
            return True
        else:
            print("[-] Integrity warning: Decrypted content does not match original.")
            return False
    except Exception as e:
        print(f"[-] Decryption error: {e}")
        return False

def calculate_sha256(file_path):
    """Calculates and returns SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[-] Hash calculation error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python security_toolkit.py <student_file_path>")
        sys.exit(1)

    target_file = sys.argv[1]

    # Error handling for missing files
    if not os.path.exists(target_file):
        print(f"[-] Error: File '{target_file}' not found.")
        sys.exit(1)

    try:
        key = generate_or_load_key()

        # 1. Initial SHA-256 Hash
        initial_hash = calculate_sha256(target_file)
        print(f"[*] Original SHA-256 Hash: {initial_hash}")

        # 2. Encryption
        encrypted_file = encrypt_file(target_file, key)

        # 3. Decryption & Verification
        if encrypted_file:
            decrypt_file(encrypted_file, target_file, key)

        # 4. Tamper Detection Test
        current_hash = calculate_sha256(target_file)
        if initial_hash == current_hash:
            print("[+] Integrity confirmed: Source file has not been modified.")
        else:
            print("[!] ALERT: Source file integrity compromised!")

    except Exception as e:
        print(f"[-] Unexpected error: {e}")