import pytest
from test_api_lesson_21.endpoints.create_post import CreatePost
from test_api_lesson_21.endpoints.update_post import UpdatePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()