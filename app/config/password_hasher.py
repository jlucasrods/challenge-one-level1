import bcrypt


def salt() -> bytes:
    return bcrypt.gensalt()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), salt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
