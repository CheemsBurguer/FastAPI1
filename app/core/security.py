from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30

def crear_token(sub: str, es_admin: bool):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    data = {
        "sub": sub,
        "exp": expire,
        "es_admin": es_admin
    }
    return jwt.encode(data, SECRET_KEY, ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)