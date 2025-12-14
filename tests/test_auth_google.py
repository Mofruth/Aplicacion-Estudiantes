def test_google_login_route_exists(client):
    response = client.get("/login/google")
    assert response.status_code in (302, 401)
