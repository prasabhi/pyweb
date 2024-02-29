# tests/test_webapp.py
import pytest
import sys
sys.path.append('/src/main/python/')
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to my web application!" in response.data
