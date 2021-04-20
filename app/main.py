# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    """
    Method used to health check through ping
    """
    return {"ping": "pong"}
