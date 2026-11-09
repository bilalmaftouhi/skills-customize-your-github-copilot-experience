# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing a reading list. Practice defining request data with Pydantic, creating FastAPI routes, and using HTTP methods and status codes.

## 📝 Tasks

### 🛠️ Set Up the API and Book Model

#### Description
Use the provided starter code to run a FastAPI application and define the data each book in the reading list will contain.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn, then run the application with `uvicorn main:app --reload`.
- Define a Pydantic model for a book with a title, author, and page count.
- Store books in an in-memory collection and assign each new book a unique ID.
- Make FastAPI's interactive documentation available at `/docs`.

### 🛠️ Create and Read Books

#### Description
Add routes that let users create books and read the reading list or an individual book.

#### Requirements
Completed program should:

- Provide `GET /books` to return all books.
- Provide `GET /books/{book_id}` to return one book by ID.
- Return HTTP 404 when a requested book does not exist.
- Provide `POST /books` to validate and add a book, assign it an ID, and return the created book with HTTP 201.

### 🛠️ Update and Delete Books

#### Description
Complete the API's basic CRUD functionality by allowing users to replace or remove a book.

#### Requirements
Completed program should:

- Provide `PUT /books/{book_id}` to replace a book's details.
- Provide `DELETE /books/{book_id}` to remove a book and return HTTP 204.
- Return HTTP 404 when an update or delete targets a book that does not exist.
- Test each route using the interactive documentation at `/docs`.
- Note that books are stored in memory and will be cleared when the application restarts.
