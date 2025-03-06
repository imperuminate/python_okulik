import allure


class Endpoint:

    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {"Content-type": "application/json; charset=UTF-8"}
    responce = None
    responce_json = None


    @allure.step("Check that title is the same as sent")
    def check_responce_title(self, title):
        assert self.responce_json["title"] == title


    @allure.step("Check that responce is 201")
    def chack_200_status(self):
        assert self.responce.status_code == 201
    
    @allure.step("Check that responce is 200")
    def chack_201_status(self):
        assert self.responce.status_code == 200