from model.creature import Creature

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

def get_by_name(name:str) -> Creature:
    for creature in _Creatures:
        if creature.name == name:
            return creature

def create(creature: Creature):
    return creature

def modify(creature: Creature):
    return creature

def replace(creature: Creature):
    return creature

def delete(name: str):
    return None