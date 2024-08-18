from supabase import create_client, Client
import os
from security.cryptography import encrypt_password, decrypt_password
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_user(email: str, password: str):
   encrypted_password = encrypt_password(password)
   response = supabase.table('users').insert({
      'email': email,
      'password': encrypted_password,
   }).execute()
   return response


def get_user_with_email(email: str) -> dict:
   response = supabase.table('users').select('email', 'password').eq('email', email).execute()
   return response.data[0]


def get_password(email: str):
   response = get_user_with_email(email)
   retrieved_password = response['password']

   if retrieved_password is None:
      return None
   else:
      decrypted_password = decrypt_password(retrieved_password)
      return decrypted_password
   

if __name__ == "__main__":
   email = os.getenv("EMAIL")
   password = os.getenv("PASSWORD")

   add_user(email, password)

   retrieved_password = get_password(email)
   if retrieved_password is None:
      print("User added but password retrieval failed!")

   elif password == retrieved_password:
      print("User added and password retrieved successfully!")
   
   else:
      print("user added but password retrieval failed!")