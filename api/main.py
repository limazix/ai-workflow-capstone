# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    """
    Method used to check the api avaliability
    """
    return {"ping": "pong!"}
