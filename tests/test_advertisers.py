def test_create_advertiser_success(client):
    """Advertiser is created and returns id and name."""
    payload = {"name": "Acme"}
    response = client.post("/advertisers/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "id" in data


def test_create_duplicate_advertiser_returns_409(client):
    """Creating an advertiser with a duplicate name returns 409 Conflict."""
    payload = {"name": "Duplicate"}
    client.post("/advertisers/", json=payload)
    response = client.post("/advertisers/", json=payload)
    assert response.status_code == 409
    assert "detail" in response.json()


def test_create_advertiser_validation_error(client):
    """Missing required fields returns 422 Unprocessable Entity."""
    response = client.post("/advertisers/", json={})
    assert response.status_code == 422


def test_list_advertisers_empty(client):
    """Listing advertisers on a fresh DB returns an empty list."""
    response = client.get("/advertisers/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_advertisers_returns_created_items(client):
    """All created advertisers are returned by the list endpoint."""
    client.post("/advertisers/", json={"name": "A"})
    client.post("/advertisers/", json={"name": "B"})
    response = client.get("/advertisers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2