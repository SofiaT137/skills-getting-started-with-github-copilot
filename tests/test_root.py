def test_root_redirect(client):
    # Arrange - client fixture provides TestClient

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"