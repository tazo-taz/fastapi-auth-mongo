from services.mongo import mongo
from utils.errors import ConflictError, NotFoundError, InvalidCredentialsError
from services.hash import hashService
from schemas.auth import User, Token
from datetime import datetime, timezone
from models.auth import UserModel
from services.jwt import jwtService
from services.settings import settings
from bson import ObjectId
async def createNewUser(email, username, password):
  # check if email exists
  emailFound = await mongo.usersCollection.find_one({ "email": email })
  if emailFound:
    raise ConflictError("username", username)
    
  # check if username exists
  usernameFound = await mongo.usersCollection.find_one({ "username": username })
  if usernameFound:
    raise ConflictError("username", username)

  # all good, hash password
  hashed_password = hashService.hash(password)

  # insert document
  userToInsert = UserModel.for_insert(email, username, hashed_password)
  user = await mongo.usersCollection.insert_one(userToInsert)

  return User(
      id=str(user.inserted_id),
      created_at=datetime.now(timezone.utc),
      **userToInsert
    )

async def authentication(email: str, password: str):
  # find by email
  user = await mongo.usersCollection.find_one({"email": email})

  if not user:
    raise NotFoundError("email", email)
  
  userModel = UserModel.from_mongo(user)

  # check password to hashed one
  if not hashService.verify_password(password, userModel.hashed_password):
    raise InvalidCredentialsError()
  
  return userModel

def getAuthCookie(id: str):
      # Create JWT token with expiration
    token = jwtService.encode({
          "id": id,
    }, 
    expMin=settings.AUTH_COOKIE_EXP)

    # Return all cookie parameters
    return {
        "key": settings.AUTH_COOKIE_NAME,
        "value": f"Bearer {token}",
        "max_age": settings.AUTH_COOKIE_EXP * 60,
        "expires": settings.AUTH_COOKIE_EXP * 60,
        "path": "/",
        "secure": True,
        "httponly": True,
        "samesite": "lax"
    }

async def getMyUserFromToken(token: str):
  # decode token
  token = token.replace("Bearer ", "")
  print(token)
  res = jwtService.decode(token)
  validatedToken = Token(**res)

  # fetch user
  user = await mongo.usersCollection.find_one({ "_id": ObjectId(validatedToken.id) })
  return UserModel.from_mongo(user).to_dict()