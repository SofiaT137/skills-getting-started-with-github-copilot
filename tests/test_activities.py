def test_get_activities(client):
    # Arrange - client fixture provides TestClient

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 9
    expected_activities = [
        "Chess Club", "Programming Class", "Gym Class", "Basketball Team",
        "Swimming Club", "Art Studio", "Drama Club", "Debate Team", "Science Club"
    ]
    assert set(data.keys()) == set(expected_activities)
    # Check structure of one activity
    chess = data["Chess Club"]
    assert "description" in chess
    assert "schedule" in chess
    assert "max_participants" in chess
    assert "participants" in chess
    assert isinstance(chess["participants"], list)
    assert chess["max_participants"] == 12
    assert len(chess["participants"]) == 2