from model.user import User
from error import Duplicate, Missing

Users = [
    User(username="khoi",hashed_pwd="123"),
    User(username="meo",hashed_pwd="456")
    ]

def find(name:str) -> User | None:
    for user in Users:
        if user.name == name:
            return user
    return None

def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"user {name} not found")
    
def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"user {name} already exists")
    
def get_all() -> list[User]:
    return Users

def get_one(name: str) -> User:
    check_missing(name)
    return find(name=name)

def create(user: User) -> User:
    check_duplicate(user.username)
    return user

def modify(name: str, user: User) -> User:
    check_missing(name=name)
    return user

def delete(name: str) -> None:
    check_missing(name)
    return None

