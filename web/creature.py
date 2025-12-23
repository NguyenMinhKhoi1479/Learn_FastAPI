from fastapi import APIRouter
import service.creature as service
from model.creature import Creature
router = APIRouter(prefix="/creature")

@router.get("/")
def get_all():
    return service.get_all()

@router.get("/{name}")
def get_one(name: str):
    return service.get_one(name)

@router.post("/")
def create(creature : Creature):
    return service.create(creature=creature)

@router.patch("/")
def modify(name: str,creature : Creature):
    return service.modify(name,creature=creature)

@router.put("/")
def replace(creature : Creature):
    return service.replace(creature=creature)

@router.delete("/{name}")
def delete(name : str):
    return service.delete(name=name)

