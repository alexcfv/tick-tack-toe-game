def test_create_item(client):
    response = client.post("/registration", json={"user_name": "Test Item", "password": "password"})
    assert response.status_code == 201
    data = response.get_json()
    assert data == "Registration succesful"