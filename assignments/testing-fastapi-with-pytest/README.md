# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Write automated tests for a reading-list REST API using pytest and FastAPI's `TestClient`. Practice isolating test data and checking responses without starting a separate web server.

## 📝 Tasks

### 🛠️ Set Up the Test Client

#### Description
Install the required packages and use the provided test scaffold to send requests to the FastAPI application directly.

#### Requirements
Completed program should:

- Install the dependencies with `pip install fastapi httpx pytest`.
- Run the tests with `pytest -q`.
- Use `TestClient` to make requests to the app without starting Uvicorn.
- Use the provided fixture to clear the in-memory book collection before and after each test.
- Keep the provided test that verifies the collection starts empty.

### 🛠️ Test Successful CRUD Requests

#### Description
Add tests that verify creating, listing, retrieving, updating, and deleting books works as expected.

#### Requirements
Completed program should:

- Check that `POST /books` returns HTTP 201 and the created book, including its ID.
- Check that `GET /books` returns the created books and `GET /books/{book_id}` returns the requested book.
- Check that `PUT /books/{book_id}` returns the updated book.
- Check that `DELETE /books/{book_id}` returns HTTP 204.
- Assert relevant response JSON fields as well as status codes.

### 🛠️ Test Error Responses and Isolation

#### Description
Test how the API responds to missing books and confirm that test data does not leak between tests.

#### Requirements
Completed program should:

- Check that getting, updating, or deleting a missing book returns HTTP 404.
- Check that creating a book without a required field returns HTTP 422.
- Keep each test independent so it passes regardless of test execution order.
- Run the full test file with `pytest -q` and confirm all tests pass.
