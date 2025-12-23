import os
from error import Missing, Duplicate
import pytest 
from model.explorer import Explorer

#set this bef
os.environ["CRYPTID_SQLITE_DB"] = ":memory"
from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="khoi",
        country="VN",
        description="alibaba"
    )
    
def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample
    
def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)
        
def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample
    
def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("random_bullshit")
        
def test_modify(sample):
    explorer.country = 'CN'
    resp = explorer.modify(sample.name,sample)
    assert resp == sample
    
def test_modify_missing():
    thing: Explorer = Explorer(name="random_bullshit",country="US",description="none")
    with pytest.raises(Missing):
        _= explorer.modify(thing.name,thing)
        
def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _=explorer.delete(sample.name)
        