import pytest
import os
import json

from app.app import app


@pytest.fixture
def client():
    return app.test_client()

def test_helloworld(client):
    response=client.get('/')
    assert response.status_code == 200
    assert 'Hello World!' in str(response.data)

def test_version(client):
    os.environ['VERSION'] = "1.0"
    os.environ['COMMITSHA'] = "abc"
    response=client.get('/version')
    assert response.status_code == 200
    data=json.loads(response.data)
    assert '1.0' in data["myapplication"][0].get("version")
    assert 'abc' in data["myapplication"][0].get("lastcommitsha")

