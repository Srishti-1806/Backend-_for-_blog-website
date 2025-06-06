from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuthPasswordBearer

oauth2_scheme = OAuthPasswordBearer(tokenUrl = "login")

# Secret key to encode and decode JWT tokens
SECRET_KEY = "mlmg654g64r6t4g84df4gtfv5c46e4r8df4g4r4df4f79r798a65r4t3ser54gt8e748r7g45er421g3r65+65+er5g6"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

access_token = create_access_token(data={"user_id": "user.id"})
return {"access_token": access_token, "token_type": "bearer"}

def verify_access_token(token: str, credentials_exception):
  try: 
      payload= jwt.decode(token, SECRET_KEY, algorithm= ALGORITHM)
      id: str =payload.get("user_id")
      
      if id is None:
        raise(credentials_exception)
      token_data = schema.TokenData(id=id)
    access_token = create_access_token(data = {"user_id": user.id})
  except JWTError:
    raise credentials_exception

def get_current_user(token: str = Depends(oauth2_scheme)):
  credentials_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"couldnt", headers={"www-authenticate": "bearer"})
  return verify_access_token(token, credentials)

