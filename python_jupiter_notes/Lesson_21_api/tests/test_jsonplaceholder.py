import pytest


TEST_DATA = [
    {"title": "My title", "body": "My body", "userId": 1},
    {"title": "Your title", "body": "Your body", "userId": 2},
    {"title": "Our title", "body": "Our body", "userId": 3},
]

NEGATIVE_DATA = [
    {"title": ["My title"], "body": "My body", "userId": 1},
    {"title": {"Your title": " "}, "body": "Your body", "userId": 2},
    {"title": ("Our title"), "body": "Our body", "userId": 3},   
]


@pytest.mark.parametrize("data", TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.chack_200_status()
    create_post_endpoint.check_responce_title(title=data["title"])


@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    # create_post_endpoint.check_negative_request()
    create_post_endpoint.chack_200_status()
    create_post_endpoint.check_responce_title(title=data["title"])


def test_put_a_post(update_post_endpoint, ):
    payload = {"title": "My title", "body": "My body", "userId": 1}    
    update_post_endpoint.make_changes_in_post(post_id=33, payload=payload)
    update_post_endpoint.chack_201_status()
    update_post_endpoint.check_responce_title(payload["title"])