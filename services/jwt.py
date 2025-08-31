import jwt
from services.settings import settings
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"

class JWTService():
  def __init__(self, secret: str):
    self.secret = secret

  def encode(self, payload: dict, expMin) -> str:
    newPayload = {**payload}

    if not expMin == None:
      newPayload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=30)
      
    return jwt.encode(payload, self.secret, algorithm=ALGORITHM)

  def decode(self, token):
    return jwt.decode(token, self.secret, algorithms=[ALGORITHM])

jwtService = JWTService(settings.JWT_SECRET)