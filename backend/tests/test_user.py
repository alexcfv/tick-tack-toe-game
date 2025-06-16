import pytest
from limiting import clients

@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": ["wrong", "name"]}, 400),
    ({"user_name": "Valid name", "password": ["wrong", "password"]}, 422),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 201),
])
def test_create_item(client, payload, expected_code):
    response = client.post("/registration", json=payload)
    assert response.status_code == expected_code

@pytest.mark.parametrize("id,expected_code", [
    (11111111111, 404),
    (1, 200),  # я уже знаю что тестовый юзер лежит под 2
    ("", 404),
])
def test_read_item(client, id, expected_code):
    clients.clear()
    response = client.get(f"/user/{id}")
    assert response.status_code == expected_code

@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": ["wrong", "name"]}, 400),
    ({"user_name": "Valid name", "password": ["wrong", "password"]}, 422),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 200),
])
def test_login(client, payload, expected_code):
    clients.clear()
    response = client.post("/login", json=payload)
    assert response.status_code == expected_code
    
@pytest.mark.parametrize("payload,expected_code", [
    ({}, 400),
    ({"password": "No name"}, 400),
    ({"user_name": ""}, 400),
    ({"user_name": ["wrong", "name"]}, 400),
    ({"user_name": "Valid name", "password": ["wrong", "password"]}, 400),
    ({"user_name": "Valid name", "password": ["wrong", "password"], "new_password" : ["wrong", "new_password"]}, 422),
    ({"user_name": "Valid name", "password": "OK"}, 400),
    ({"user_name": "Valid name", "password": "Valid password"}, 400),
    ({"user_name": "Valid name", "password": "Wrong password", "new_password": "new_password"}, 400),
    ({"user_name": "Valid name", "password": "Valid password", "new_password": "new_password"}, 200),    
])

def test_update(client, login_user_fixture, payload, expected_code):
    clients.clear()
    response = client.post("/update", json=payload)
    assert response.status_code == expected_code

def test_delete(client, login_user_fixture):
    response = client.post("/delete", json={"user_name": "Valid name", "password": "Valid password", "new_password": "new_password"})
    assert response.status_code == 204
    
def test_rate_limiting(client):
    clients.clear()

    for _ in range(10):
        response = client.get('/user/1')
        assert response.status_code == 200

    response = client.get('/user/1')
    assert response.status_code == 429
    assert b"Too many requests" in response.data