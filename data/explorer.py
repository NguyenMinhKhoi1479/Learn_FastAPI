import sqlite3
from model.explorer import Explorer
from data.init_db import curs, IntegrityError
from error import Missing , Duplicate

curs.execute("""create table if not exists explorer(
    name text primary key,
    description text,
    country text)""")

def row_to_model(row: tuple) -> Explorer:
    name, des, country = row
    return Explorer(name = name,description=des,country=country)

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict()

def get_one(name:str) -> Explorer:
    qry = """select * from explorer where name = :name"""
    param = {"name" : name}
    curs.execute(qry,param)
    row = curs.fetchone()
    if not row:
        raise Missing(msg=f"your explorer {name} not found")
    return row_to_model(row)

def get_all() -> list[Explorer]:
    qry = """select * from explorer"""
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]
    
def create(explorer: Explorer):
    qry = """
    INSERT INTO explorer (name, description, country)
    VALUES (:name, :description, :country)"""
    param = model_to_dict(explorer)
    
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Duplicate(msg=f"{explorer.name} already exists")
    return get_one(explorer.name)

def modify(name: str,explorer: Explorer) -> Explorer:
    qry = """update explorer
             set country = :country,
                 name = :name,
                 description = :description
             where name = :org_name"""
    param = model_to_dict(explorer)
    param['org_name'] = name
    
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Missing(msg=f"{name} not found")
    return get_one(explorer.name)

def delete(name: str):
    qry = """delete from explorer where name =:name"""
    param = {"name" : name}
    
    curs.execute(qry,param) #dù có hay không thì vẫn ko trả về exception
    if curs.rowcount == 0:
        raise Missing(msg=f"{name} not found")
    return None
