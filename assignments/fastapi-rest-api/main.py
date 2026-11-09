from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Reading List API")


class Book(BaseModel):
    title: str
    author: str
    pages: int


books: dict[int, Book] = {}
next_book_id = 1

# Add GET, POST, PUT, and DELETE routes for the reading list.
