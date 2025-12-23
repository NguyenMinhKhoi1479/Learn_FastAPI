from model.explorer import Explorer

_Explorers = [
    Explorer(
        name="cat",
        country='japan',
        description='meow meow'
    ),
    Explorer(
        name="dog",
        country='us',
        description='bar bar'
    ),
    Explorer(
        name="lion",
        country='indian',
        description='grrr'
    ),
    Explorer(
        name="big Nose",
        country='norway',
        description='oyo'
    )
]         

def get_all() -> list[Explorer]:
    return _Explorers

def get_by_name(name:str) -> Explorer:
    for explorer in _Explorers:
        if explorer.name == name:
            return explorer

def create(explorer: Explorer):
    return explorer

def modify(explorer: Explorer):
    return explorer

def replace(explorer: Explorer):
    return explorer

def delete(name: str):
    return None