# Project creation

1. Create Fast api instance, pass information about project, title, description and version
2. Pass lifespan that will connect to mongo
3. Create lifespan with @asynccontextmanager where first will connect to mongo then yield and then close mongo connection
4. Create connect to mongo and close mongo connection functions. use motor.motor_asyncio AsyncIOMotorClient to connect, create client and database variable, create get collection function to get any collection
5. Create config class that will have: mongodb_url, database_name
6. Create file for auth router 
7. Create register endpoint post request, in docs show be displayed what kind of data will be returned and status code should be 201
8. Create User class with id, email(should be email), username, is_active
9. Create UserCreate class so it will be for register endpoint body
10. validate that no email and username is like that, if all good then hash password and save doc also return user
11. Create login endpoint, it will have userLogin class(email,password), first it should validate user existance, create access_token, token should be 30min and should take userId and then set cookie to response, cookie name and expire cookie should be in settings
12. Create logout endpoint, which will remove cookie
13. Create me enpoint, which will returns user