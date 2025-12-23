from model.creature import Creature
from service import creature as code

sample = Creature(
        name="ghoti",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    )

def test_create():
    resp = code.create(sample)
    assert resp == sample
    
def test_get_exists():
    resp = code.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    resp = code.get_one("sample")
    assert resp is None