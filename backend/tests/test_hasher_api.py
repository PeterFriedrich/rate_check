import requests

AUTH_SERVICE_URL = "http://localhost:8000"

def test_hasher_api():
    """Test password hashing via the auth-service API."""
    password = "securepassword123"
    response = requests.post(f"{AUTH_SERVICE_URL}/hash", json={"password":password})

    assert response.status_code == 200
    hashed_password = response.json().get("hashed_password")

    assert hashed_password is not None
    assert isinstance(hashed_password, str)
