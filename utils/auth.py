from fastapi import HTTPException

def conflictException(field, value):
    return HTTPException(
    status_code=409,
    detail=f"User with {field}:{value} already exists"
  )