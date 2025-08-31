from motor.motor_asyncio import AsyncIOMotorClient
from services.settings import settings

class MongoService():
  def __init__(self):
    self.client = AsyncIOMotorClient(settings.MONGODB_URL)
    self.db = self.client[settings.DATABASE_NAME]
    
  def disconnect(self):
    self.client.close()

  def getCollection(self, name: str):
    return self.db[name]
  
  @property
  def usersCollection(self):
    return self.getCollection("users")

mongo = MongoService()