def test_estudiante_notas_requires_login(client):
    response = client.get("/estudiante/notas")
    assert response.status_code == 302
