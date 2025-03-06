import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):

    @allure.step("Update a post")
    def make_changes_in_post(self, post_id, payload):
        self.responce = requests.put(f"{self.url}/{post_id}", 
                                     json=payload, 
                                     headers=self.headers)
        self.responce_json = self.responce.json()

    

