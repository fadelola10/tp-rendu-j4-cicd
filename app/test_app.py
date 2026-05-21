import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'version' in response.json
    assert response.json['app'] == 'FormaTech'

def test_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert 'version' in response.json
