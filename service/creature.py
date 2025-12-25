import os
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as data
else:
    from data import creature as data

from model.creature import Creature

def get_all() -> list[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature):
    return data.create(creature=creature)

def modify(name: str,creature: Creature):
    return data.modify(name,creature=creature)

def replace(name,creature: Creature):
    return data.replace(name,creature=creature)

def delete(name: str):
    return data.delete(name)