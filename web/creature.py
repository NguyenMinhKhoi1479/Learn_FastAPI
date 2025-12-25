import os
#load file env
from dotenv import load_dotenv
load_dotenv()
from fastapi import APIRouter, HTTPException
from error import Missing, Duplicate
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    import service.creature as service
from model.creature import Creature

#router
router = APIRouter(prefix="/creature")

@router.get("/")
def get_all():
    return service.get_all()

@router.get("/{name}")
def get_one(name: str):
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404,
                            detail=exc.msg)

@router.post("/")
def create(creature : Creature):
    try:
        return service.create(creature=creature)
    except Duplicate as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

@router.patch("/")
def modify(name: str,creature : Creature):
    try:
        return service.modify(name,creature=creature)
    except Missing as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

@router.delete("/{name}")
def delete(name : str):
    try:
        return service.delete(name=name)
    except Missing as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

