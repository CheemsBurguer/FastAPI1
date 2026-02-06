from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30

def crear_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None


