import bcrypt

class HashService():
  def hash(self, value: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(value.encode(), salt)
    return hashed.decode()
  
  def verify_password(self, value: str, hashed_value: str) -> bool:
    return bcrypt.checkpw(value.encode(), hashed_value.encode())
  

hashService = HashService()