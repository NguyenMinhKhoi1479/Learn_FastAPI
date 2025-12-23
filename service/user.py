from datetime import timedelta, datetime
import os
from jose import jwt
from model.user import User

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data
    
#auth 
from passlib.context import CryptContext

#set secret key
SECRET_KEY = "1479"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["argon2"], deprecated = "auto")

def hash_pwd(pwd: str) -> str:
    return pwd_context.hash(pwd)

def verify_pwd(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd,hashed_pwd)

def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token=token,key = SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except jwt.JWTError:
        return None
    return username

def get_current_user(token: str) -> User | None:
    #check for the existed of username
    if not (username := get_jwt_username(token=token)):
        return None
    if not (user := lookup_user(username=username)):
        return user
    return None
    
def lookup_user(username: str) -> User | None:
    if (user := data.get_one(username)):
        return user
    return None

def auth_user(name: str, plain: str) -> User | None:
    #get user with username = name
    if not (user := lookup_user(name)):
        return None
    #check for password
    if not verify_pwd(plain,user.hashed_pwd):
        return None
    return user

def create_access_token(data: dict, expires: timedelta | None = None):
    #thành phần tạo nên token là sub = ai là người request ? và expires thời gian hết hạn là bao nhiêu ?
    src = data.copy()
    #thời gian hiện tại 
    now = datetime.utcnow()
    if not expires:
        expires = timedelta(minutes = 15)
    #thời điểm hết hạn token là từ thời điểm hiện tại + thời gian hết hạn
    src.update({"exp" :now + expires})
    encode_jwt = jwt.encode(src,SECRET_KEY,ALGORITHM)
    return encode_jwt

#CRUD để thông qua data

def get_all() -> list[User]:
    return data.get_all()
def get_one(name: str) -> User:
    return data.get_one(name)
def create(user: User) -> User:
    user.hashed_pwd = hash_pwd(user.hashed_pwd)
    return data.create(user)
def modify(name: str, user: User) -> User:
    return data.modify(name,user)
def delete(name: str) -> None:
    return data.delete(name)
    
