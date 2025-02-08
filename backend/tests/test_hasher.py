# unit test for hasher

import pytest
from authenticator.hasher import Hasher

def test_password_hashing():
    # basic check for pass word hasher 
    password = "securepassword"
    hashed_password = Hasher.hash_password(password)

    assert Hasher.verify_password(password, hashed_password) == True
    assert Hasher.verify_password("wrongpassword", hash_password) == False
