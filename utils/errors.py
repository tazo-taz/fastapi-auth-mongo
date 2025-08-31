from fastapi import HTTPException, status

class CustomException(Exception):
    def __init__(self, detail: str, status_code: int = 400):
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)

def handle_error(e: Exception):
    if isinstance(e, CustomException):
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    else:
        # Fallback for unexpected errors
        print(f"Unexpected error: {e}")  # optional logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

class ConflictError(CustomException):
    def __init__(self, field: str, value: str):
        detail = f"Document {field}:'{value}' already exists"
        super().__init__(detail, status_code=409)

class NotFoundError(CustomException):
    def __init__(self, field: str, value: str):
        detail = f"Document {field}:'{value}' not found"
        super().__init__(detail, status_code=404)

class InvalidCredentialsError(CustomException):
    def __init__(self):
        detail = "Invalid credentials"
        super().__init__(detail, status_code=401)  # 401 Unauthorized
