# app/main.py

import os, sys, json
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

SECRET_KEY = "my_super_secret_key_123"

class usermanager:
    def __init__(self, NAME, Age):
        self.name = NAME
        self.age = Age

    def save_to_db(self):
        db_file = "database.txt"
        with open(db_file, "a") as f:
            f.write(f"{self.name}, {self.age}\n")


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open("output.png", "wb") as f:
        f.write(contents)
    return {"filename": file.filename, "status": "saved"}


def downloadImage(url: str):
    response = requests.get(url)
    with open("output.png", "wb") as f:
        f.write(response.content)
    return "output.png"


def misSpelled_functn(x):
    return x*2
