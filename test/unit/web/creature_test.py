import os
import pytest
from fastapi import HTTPException
os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.creature import Creature
from web import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="dragn",
        country='japan',
        area = "str",
        description='$',
        aka = "stinky"
    )

@pytest.fixture()
def fakes() -> list[Creature]:
    return creature.get_all()

def assert_duplicate(exc):
    assert "Duplicate" in exc.value.msg
    assert exc.value.status_code == 404
    
def assert_missing(exc):
    assert "Missing" in exc.value.msg
    assert exc.value.status_code == 404
    
def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = creature.create(fakes[0])
        assert_duplicate(exc)
def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]
    
def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = creature.get_one("hallo")
        assert_missing(exc)
    
def test_modify(fakes):
    assert creature.modify(fakes[0].name,fakes[0]) == fakes[0]
    
def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = creature.modify("hallo", sample)
        assert_missing(exc)
        
def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None
    
def test_delete_missing():
    with pytest.raises(HTTPException) as exc:
        _ = creature.delete("hallo")
        assert_missing(exc)
    
