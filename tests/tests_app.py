import pytest

from app import app

# import app as app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get("/")
    assert b"Welcome to the Flask App!" in rv.data


def test_about(client):
    rv = client.get("/about")
    assert b"This is the about page." in rv.data


def test_api_data(client):
    rv = client.get("/api/data")
    json_data = rv.get_json()
    assert json_data["name"] == "Flask App"


def test_form_get(client):
    rv = client.get("/form")
    assert b'<form method="POST">' in rv.data


def test_form_post(client):
    rv = client.post("/form", data={"name": "Test User"})
    assert b"Thank you, Test User!" in rv.data
