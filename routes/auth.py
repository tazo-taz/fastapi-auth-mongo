from fastapi import APIRouter, Cookie
from schemas.auth import UserCreate, User, UserLogin
from services.auth import createNewUser, authentication, getAuthCookie, getMyUserFromToken
from utils.errors import handle_error
from fastapi import Response
from services.settings import settings

authRouter = APIRouter(
  prefix='/auth',
  tags=['Auth']
)

# username, email, password
@authRouter.post("/register", status_code=201, response_model=User)
async def register(data: UserCreate):
  try:
    return await createNewUser(data.email, data.username, data.password)
  except Exception as e:
    handle_error(e)

# email and password
@authRouter.post("/login")
async def login(response: Response, data: UserLogin):
  try:
    user = await authentication(data.email, data.password)

    cookie_params = getAuthCookie(user.id)  # returns dict of cookie parameters
    response.set_cookie(**cookie_params)
    return {
      "success": True
    }
  except Exception as e:
    handle_error(e)

@authRouter.post("/me", status_code=200, response_model=User)
async def getMyUser(access_token = Cookie(None, alias=settings.AUTH_COOKIE_NAME)):
  userModel = await getMyUserFromToken(access_token)
  return User(**userModel)

@authRouter.delete('/logout')
async def logout(response: Response):
  response.delete_cookie(settings.AUTH_COOKIE_NAME)
  return {
    "success": True
  }