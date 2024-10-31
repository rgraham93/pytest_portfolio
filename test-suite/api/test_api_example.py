# Example API tests reside here
import pytest
import httpx
from typing import Generator

@pytest.fixture
def client() -> Generator[httpx.Client, None, None]:
    """Fixture that creates and yields an HTTPX client."""
    with httpx.Client(base_url="https://api.example.com") as client:
        yield client

def test_get_user(client: httpx.Client):
    """Test getting a user endpoint."""
    # Arrange
    user_id = "123"
    expected_status_code = 200
    
    # Act
    response = client.get(f"/users/{user_id}")
    
    # Assert
    assert response.status_code == expected_status_code
    assert response.json()["id"] == user_id
    assert "name" in response.json()
    assert "email" in response.json()

def test_create_user(client: httpx.Client):
    """Test creating a new user."""
    # Arrange
    new_user = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    expected_status_code = 201
    
    # Act
    response = client.post("/users", json=new_user)
    
    # Assert
    assert response.status_code == expected_status_code
    assert response.json()["name"] == new_user["name"]
    assert response.json()["email"] == new_user["email"]
    assert "id" in response.json()

def test_invalid_user_id(client: httpx.Client):
    """Test requesting a non-existent user."""
    # Arrange
    invalid_id = "999999"
    expected_status_code = 404
    
    # Act
    response = client.get(f"/users/{invalid_id}")
    
    # Assert
    assert response.status_code == expected_status_code