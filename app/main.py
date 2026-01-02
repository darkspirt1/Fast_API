from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# importing models and schemas
from .import models, schemas, utilis
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='postgres',
                                user='postgres', password='8928', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(5)

app = FastAPI()


# creating a list to hold our posts
my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
           {"title": "title of post 2", "content": "content of post 2", "id": 2}]

# helper functions


def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i

# here we define our first route


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


