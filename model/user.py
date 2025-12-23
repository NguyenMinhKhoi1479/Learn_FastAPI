from pydantic import BaseModel

class User(BaseModel):
    username: str
    hashed_pwd: str
    