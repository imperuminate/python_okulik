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
    yield 1
    requests.delete("https://jsonplaceholder.typicode.com/posts/1")


@pytest.fixture()
def num():
    return 3