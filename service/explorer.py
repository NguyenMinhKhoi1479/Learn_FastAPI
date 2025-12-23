from model.explorer import Explorer
import data.explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name=name)

def create(explorer: Explorer):
    return data.create(explorer)

def modify(name,explorer: Explorer):
    return data.modify(name,explorer)

def replace(name,explorer: Explorer):
    return data.replace(name,explorer)

def delete(name: str):
    return data.delete(name)