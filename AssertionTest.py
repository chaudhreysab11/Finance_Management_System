import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_dbstore(app,client):
    res = client.get('/teststore')
    assert res.status_code == 200

def test_dbfetch(app,client):
    res = client.get('/testfetch')
    assert res.status_code == 200


