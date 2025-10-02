import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./websites.db")
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY missing. Generate it with : "
        "python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'"
    )

FERNET = Fernet(SECRET_KEY.encode())
