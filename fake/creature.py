from model.creature import Creature
from error import Missing, Duplicate
#     name: str
#     country: str
#     area: str
#     description: str
#     aka: str

_Creatures = [
    Creature(
        name="cat",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    ),
    Creature(
        name="cat",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    ),
    Creature(
        name="dog",
        country='US',
        area = "str",
        description=' meow',
        aka = "stinky"
    ),
    Creature(
        name="ghoti",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    )
]         

def get_all() -> list[Creature]:
    return _Creatures

def get_one(name:str) -> Creature:
    for creature in _Creatures:
        if creature.name == name:
            return creature
    raise Missing(f"Missing")

def create(creature: Creature):
    for crea in _Creatures:
        if creature.name == crea.name:
            raise Duplicate(f"Duplicate")
    return creature

def modify(name: str,creature: Creature):
    for crea in _Creatures:
        if creature.name == name:
            return creature
    raise Missing(f"Missing")

def replace(creature: Creature):
    return creature

def delete(name: str):
    for creature in _Creatures:
        if creature.name == name:
            return None
    raise Missing(f"Missing")