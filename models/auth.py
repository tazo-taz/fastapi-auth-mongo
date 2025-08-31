from datetime import datetime, timezone
from pydantic import EmailStr

class UserModel:
    def __init__(self, id: str, email: EmailStr, username: str, hashed_password: str,
                 created_at: datetime, updated_at: datetime):
        self.id = str(id)
        self.email = email
        self.username = username
        self.hashed_password = hashed_password
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_mongo(cls, doc: dict):
        """Parse Mongo document to User instance"""
        return cls(
            id=str(doc["_id"]),
            email=doc["email"],
            username=doc["username"],
            hashed_password=doc["hashed_password"],
            created_at=doc.get("created_at", datetime.now(timezone.utc)),
            updated_at=doc.get("updated_at", datetime.now(timezone.utc)),
        )

    @classmethod
    def for_insert(cls, email: str, username: str, hashed_password: str):
        """Prepare a dict ready to insert into Mongo"""
        return {
            "email": email,
            "username": username,
            "hashed_password": hashed_password,
        }

    def to_dict(self):
        """Convert the User instance back to dict (JSON response)"""
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
