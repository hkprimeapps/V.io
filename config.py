from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    INSTAGRAM_CLIENT_ID: str = os.getenv('INSTAGRAM_CLIENT_ID')
    INSTAGRAM_CLIENT_SECRET: str = os.getenv('INSTAGRAM_CLIENT_SECRET')
    REDIRECT_URI: str = os.getenv('REDIRECT_URI')
    ENCRYPTION_KEY: str = os.getenv('ENCRYPTION_KEY')
    API_KEY: str = os.getenv('API_KEY')
    # Other settings...

settings = Settings()

print(f"INSTAGRAM_CLIENT_ID: {settings.INSTAGRAM_CLIENT_ID}")
print(f"INSTAGRAM_CLIENT_SECRET: {settings.INSTAGRAM_CLIENT_SECRET}")
print(f"REDIRECT_URI: {settings.REDIRECT_URI}")
