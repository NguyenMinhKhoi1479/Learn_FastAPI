from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import requests

secrect_user = "khoi"
secrect_pwd = "123"

app = FastAPI()
basic = HTTPBasic()


@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    if creds.username == secrect_user and creds.password == secrect_pwd:
        return {"username" : creds.username , "password" : creds.password}
    raise HTTPException(
        status_code=401,
        detail="invalid credential"
    )