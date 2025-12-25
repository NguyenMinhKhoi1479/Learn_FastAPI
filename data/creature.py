import sqlite3
from model.creature import Creature
from data.init_db import conn, curs, IntegrityError
from error import Missing, Duplicate 

curs.execute("""create table if not exists creature(
    name text primary key,
    description text,
    country text,
    area text,
    aka text)""")

def row_to_model(row: tuple) -> Creature:
    name, des, country , area , aka = row
    return Creature(name=name,description = des,country= country,area= area,aka= aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.dict()

def get_one(name:str) -> Creature:
    qry = """select * from creature where name = :name"""
    param = {"name" : name}
    row = curs.execute(qry,param).fetchone()
    if row is None:
        raise Missing(msg=f"{name} not found")
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = """select * from creature"""
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]
    
def create(creature: Creature):
    qry = """insert into creature values(:name, :description, :country, :area, :aka)"""
    param = model_to_dict(creature)

    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Duplicate(f"{creature.name} already exists")
    return get_one(creature.name)

def modify(name: str,creature: Creature) -> Creature:
    qry = """update creature
             set country = :country,
                 name = :name,
                 description = :description,
                 area = :area,
                 aka = :aka
             where name = :org_name"""
    param = model_to_dict(creature)
    param['org_name'] = name
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Missing(f"{name} not found")
    return get_one(creature.name)

def delete(name: str) -> bool:
    qry = """delete from creature where name =:name"""
    param = {"name" : name}
    
    try:
        curs.execute(qry,param)
    except IntegrityError:
        raise Missing(f"{name} not found")
    return None

