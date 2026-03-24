def test_successful_signup(client):
    # Arrange - client fixture provides TestClient

    # Act
    response = client.post("/activities/Basketball%20Team/signup?email=test@example.com")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up test@example.com for Basketball Team"}
    # Verify added
    resp = client.get("/activities")
    assert "test@example.com" in resp.json()["Basketball Team"]["participants"]


def test_duplicate_signup(client):
    # Arrange
    client.post("/activities/Art%20Studio/signup?email=dup@example.com")  # First signup

    # Act
    response = client.post("/activities/Art%20Studio/signup?email=dup@example.com")  # Second attempt

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is already signed up for this activity"}


def test_nonexistent_activity(client):
    # Arrange - client fixture provides TestClient

    # Act
    response = client.post("/activities/Nonexistent/signup?email=test@example.com")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_when_full(client):
    # Arrange
    # Chess Club has max 12, currently 2 participants
    # Sign up 10 more to fill it
    for i in range(10):
        client.post(f"/activities/Chess%20Club/signup?email=user{i}@example.com")

    # Act
    response = client.post("/activities/Chess%20Club/signup?email=full@example.com")

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Activity is full"}