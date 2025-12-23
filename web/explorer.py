from fastapi import APIRouter, HTTPException, status
import service.explorer as service
from model.explorer import Explorer
from error import Missing, Duplicate
router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all():
    return service.get_all()

@router.get("/{name}")
def get_one(name: str):
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(
            status_code= 404,
            detail=exc.msg
        )

@router.post("/")
def create(explorer : Explorer):
    try:
        return service.create(explorer=explorer)
    except Duplicate as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

@router.patch("/")
def modify(name: str,explorer : Explorer):
    try:
        return service.modify(name,explorer=explorer)
    except Missing as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

@router.put("/")
def replace(explorer : Explorer):
    return service.replace(explorer=explorer)

@router.delete("/{name}")
def delete(name : str):
    try:
        return service.delete(name=name)
    except Missing as exc:
        raise HTTPException(
            status_code=404,
            detail=exc.msg
        )

