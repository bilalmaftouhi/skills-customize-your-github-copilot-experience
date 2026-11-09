from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Reading List API")


class Book(BaseModel):
    title: str
    author: str
    pages: int


books: dict[int, Book] = {}
next_book_id = 1


def book_response(book_id: int, book: Book) -> dict:
    return {"id": book_id, **book.model_dump()}


@app.get("/books")
def list_books() -> list[dict]:
    return [book_response(book_id, book) for book_id, book in books.items()]


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book_response(book_id, books[book_id])


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> dict:
    global next_book_id
    book_id = next_book_id
    next_book_id += 1
    books[book_id] = book
    return book_response(book_id, book)


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book) -> dict:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    books[book_id] = book
    return book_response(book_id, book)


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    if book_id not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    del books[book_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
