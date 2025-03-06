import requests
import allure


@allure.feature("Post")
@allure.story("DELETE")
def test_delete(new_post_id):
    with allure.step(f"Run DELETE to delete post with {new_post_id} id"):
        requests.delete(f"https://jsonplaceholder.typicode.com/posts{new_post_id}")


@allure.feature("Post")
@allure.story("DELETE")
@allure.title("Удаление поста с айди 1")
@allure.issue("https://i0.wp.com/synapse-qa.com/wp-content/uploads/2022/01/Used-Bug-Advocacy-pic.png?w=582&ssl=1", "WPA-29345")
def test_delete_post1():
    with allure.step("Run DELETE to delete post with 1 id"):    
        requests.delete("https://jsonplaceholder.typicode.com/posts1")
    with allure.step("Check that 2 == 2"):
        assert 2 != 2