from core.config import FERNET

def encrypt(value: str) -> str:
    return FERNET.encrypt(value.encode()).decode()

def decrypt(token: str) -> str:
    return FERNET.decrypt(token.encode()).decode()
