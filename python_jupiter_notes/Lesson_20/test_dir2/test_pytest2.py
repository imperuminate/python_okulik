import requests
import allure


@allure.feature("Post")
@allure.story("GET")
def test_get_one_post(new_post_id):
    with allure.step(f"Run the GET for {new_post_id} post"):
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/posts/{new_post_id}"
        ).json()
    with allure.step(f"Check that post id is {new_post_id}"):
        assert response["id"] == new_post_id


@allure.feature("Example")
def test_num(num):
    assert 444 == 444

@allure.feature("Example")
def test_num2(num):
    print(num)

@allure.feature("Example")
def test_num3(num):
    print(num)

@allure.feature("Example")
def test_num4(num):
    print(num)


@allure.feature("Example")
def test_num5(num):
    print(num)

@allure.feature("Example")
def test_num6(num):
    print(num)
    
@allure.feature("Example")
def test_num7(num):
    print(num)