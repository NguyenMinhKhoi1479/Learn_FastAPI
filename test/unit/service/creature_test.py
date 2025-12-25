
import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
import pytest

from model.creature import Creature
from error import Missing, Duplicate
from service import creature as service

@pytest.fixture()
def sample() -> Creature:
    return Creature(
        name="cat",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    )
@pytest.fixture()
def create_sample() -> Creature:
    return Creature(
        name="123",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    )

def test_create(create_sample):
    resp = service.create(create_sample)
    assert resp == create_sample
    
def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = service.create(sample)
        resp == service.create(sample) 
        
def test_get_one(sample):
    resp = service.get_one(sample.name)
    assert resp == sample
    
def test_get_one_missing():
    with pytest.raises(Missing):
        _ = service.get_one("unknownable")

def test_modify(sample):
    sample.aka = "drake"
    resp = service.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    sample = Creature(
        name="asdasd",
        country='asdasd',
        area = "stasdasdr",
        description='asdasd asdasd',
        aka = "asdasd"
    )
    with pytest.raises(Missing):
        _ = service.modify("unknownable",sample)
        
def test_delete(sample):
    resp = service.delete(sample.name)
    assert resp is None
