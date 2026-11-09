import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture
def client():
    main.books.clear()
    main.next_book_id = 1
    with TestClient(main.app) as test_client:
        yield test_client
    main.books.clear()
    main.next_book_id = 1


def test_list_books_starts_empty(client):
    response = client.get("/books")

    assert response.status_code == 200
    assert response.json() == []


# Add tests for creating, reading, updating, and deleting books.
# Also test missing books and invalid request data.
