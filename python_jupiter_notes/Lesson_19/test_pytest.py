import requests
import pytest


@pytest.fixture()
def new_post_id():
    btitle = "Hello world"
    bbody = "Nice to see you"
    buser_id = 4
    body = {"title": btitle, "body": bbody, "userId": buser_id}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=body, headers=headers
    ).json()
    print("fixture start")
    yield 1
    requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print("fixture finished")

@pytest.fixture(scope="session")
def hello():
    print("Hello")
    yield
    print("Buy")


@pytest.mark.skip("Post id not setup yet")
def test_get_one_post(new_post_id, hello):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{new_post_id}"
    ).json()
    print("test function finished")
    assert response["id"] == new_post_id


@pytest.mark.regresion
def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 100


@pytest.mark.regresion
def test_add_post():
    btitle = "Hello world"
    bbody = "Nice to see you"
    buser_id = 444
    body = {"title": btitle, "body": bbody, "userId": buser_id}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    responce = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=body, headers=headers
    )
    assert responce.status_code == 201
    assert responce.json()["title"] == btitle


@pytest.mark.smoke
def test_one():
    assert 1 == 1


@pytest.mark.smoke
def test_two():
    assert 1 == 1


@pytest.mark.parametrize("logins", ["", " ", "#$%^&", "dsd"])
def test_three(logins):
    assert logins == "dsd"
