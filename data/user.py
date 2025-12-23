from model.user import User
from init_db import conn, curs, IntegrityError
from error import Missing, Duplicate


curs.execute("""create table if not exists User(
        username text primary key
        hashed_pwd text)""")

curs.execute("""create table if not exists xUser(
        username text primary key
        hashed_pwd text)""")

def row_to_model(row: tuple) -> dict:
    username, hashed_pwd = row
    return User(username= username, hashed_pwd = hashed_pwd)

def model_to_dict(user: User) -> dict:
    return user.dict()

def get_one(username: str, table: str = "User") -> User:
    qry = f"""SELECT * FROM {table} WHERE USERNAME = :username"""
    param = {"username" : username}
    curs.execute(qry,param)
    row = curs.fetchone()
    if not row:
        raise Missing(f"user {username} not found")
    return row_to_model(row=row)

def get_all(table: str = "User"):
    qry = f"""SELECT * FROM {table}"""
    curs.execute(qry)
    return [row_to_model(row=row) for row in curs.fetchall()]

def create(user: User, table: str = "User") -> User:
    qry = f"""insert into {table}(username,hashed_pwd) values(:username,:hashed_pwd)"""
    param = model_to_dict(user=user)
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Duplicate(f"user {user.name} already exists")
    return get_one(user.username)

def modify(name: str, user: User, table: str = "User"):
    qry = f"""update {table} set
                name = :username
                hashed_pwd = :hashed_pwd
                where name = :username"""
                
    param = model_to_dict(user=user)
    param.update({"name" : name})
    
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Missing(msg=f"user {name} not found")
        
    return get_one(user.username)

def delete(name: str):
    user = get_one(user)
    qry = f"""delete from User where username = :username"""
    param = {"username" : name}
    
    curs.execute(qry,param)
    
    if curs.rowcount != 1:
        raise Missing(msg=f"user {name} not found")
    create(user=user,table="xUser")
    
    
        
    
    
    