from fastapi import FastAPI
from contextlib import asynccontextmanager
from services.mongo import mongo
from routes.auth import authRouter

@asynccontextmanager
async def lifespan(app):
  print("connected")
  yield
  mongo.disconnect()
  print("disconnected")


app = FastAPI(
  title="Fastapi auth project",
  description="This is my first jwt auth project using fastapi",
  version="0.1.0",
  lifespan=lifespan
)

app.include_router(authRouter)