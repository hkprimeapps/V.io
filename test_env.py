from dotenv import load_dotenv
import os

load_dotenv()

print(f"INSTAGRAM_CLIENT_ID: {os.getenv('INSTAGRAM_CLIENT_ID')}")
print(f"INSTAGRAM_CLIENT_SECRET: {os.getenv('INSTAGRAM_CLIENT_SECRET')}")
print(f"REDIRECT_URI: {os.getenv('REDIRECT_URI')}")
print(f"ENCRYPTION_KEY: {os.getenv('ENCRYPTION_KEY')}")
