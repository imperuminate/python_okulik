import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    @allure.step("Create a post")
    def create_new_post(self, payload):
        self.responce = requests.post(self.url, json=payload, headers=self.headers)
        self.responce_json = self.responce.json()


    @allure.step("Check that 400 error recieved")
    def check_negative_request(self):
        assert self.responce.status_code == 400
