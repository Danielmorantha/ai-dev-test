from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    token = os.getenv("token")
    JWT_PRIVATE_KEY = os.getenv("JWT_PRIVATE_KEY").replace('\\n', '\n')
    JWT_PUBLIC_KEY = os.getenv("JWT_PUBLIC_KEY").replace('\\n', '\n')
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
