def test_create_item(client):
    response = client.post("/registration", json={"user_name": "testing", "password": "password"})
    print(response)
    assert response.status_code == 201
    data = response.get_json()
    assert data == "Registration succesful"