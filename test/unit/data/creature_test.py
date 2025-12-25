import os 
import pytest
from model.creature import Creature
from error import Missing,Duplicate

#set value for env file
os.environ["CRYPTID_UNIT_TEST"] = "true"
from data import creature as data

@pytest.fixture()
def sample() -> Creature:
    return Creature(
        name="qwe",
        country='japan',
        area = "str",
        description='meow meow',
        aka = "stinky"
    )
    
def test_create(sample):
    resp = data.create(sample)
    assert resp == sample
    
def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        resp = data.create(sample)
        resp == data.create(sample) 
        
def test_get_one(sample):
    resp = data.get_one(sample.name)
    assert resp == sample
    
def test_get_one_missing():
    with pytest.raises(Missing):
        _ = data.get_one("unknownable")

def test_modify(sample):
    sample.aka = "drake"
    resp = data.modify(sample.name, sample)
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
        _ = data.modify("unknownable",sample)
        
def test_delete(sample):
    resp = data.delete(sample.name)
    assert resp is None
