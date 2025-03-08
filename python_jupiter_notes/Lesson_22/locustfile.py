from locust import task, HttpUser
import random

class PosrUser(HttpUser):

    def on_start(self):
        self.client.post("/posts", json={"title": "My title", "body": "My body", "userId": 1})

    @task(3)
    def get_all_posts(self):
        self.client.get("/posts")

    @task(1)
    def get_one_post(self):
        self.client.get(f"/posts/{random.choice(range(1, 101))}")
