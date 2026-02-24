def test_create_advertiser_success(client):
    payload = {"name": "Acme"}
    response = client.post("/advertisers/", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "id" in data


def test_create_duplicate_advertiser_returns_400(client):
    payload = {"name": "Duplicate"}
    client.post("/advertisers/", json=payload)
    # Calls post a second time
    response = client.post("/advertisers/", json=payload)

    assert response.status_code == 409
    assert "detail" in response.json()


def test_create_advertiser_validation_error(client):
    response = client.post("/advertisers/", json={})
    assert response.status_code == 422


def test_list_advertisers_empty(client):
    response = client.get("/advertisers/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_advertisers_returns_created_items(client):
    client.post("/advertisers/", json={"name": "A"})
    client.post("/advertisers/", json={"name": "B"})
    response = client.get("/advertisers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2