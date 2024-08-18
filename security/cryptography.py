from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()


encryption_key = os.getenv("ENCRYPTION_KEY")
cipher_suite = Fernet(encryption_key.encode())


def encrypt_password(password: str) -> str:
   encrypted_password = cipher_suite.encrypt(password.encode())
   return encrypted_password.decode()


def decrypt_password(encrypted_password: str) -> str:
   decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
   return decrypted_password.decode()


if __name__ == "__main__":
   password = "password123"
   encrypted_password = encrypt_password(password)
   
   if password == decrypt_password(encrypted_password):
      print("Encryption and decryption successful!")