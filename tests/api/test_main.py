from starlette.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_ping():
    """
    it should answer pong
    """
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
