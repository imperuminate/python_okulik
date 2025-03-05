import unittest
import requests
import sys


class TestPostAPI(unittest.TestCase):

    def setUp(self):
        btitle = "Hello world"
        bbody = "Nice to see you"
        buser_id = 4
        body = {"title": btitle, "body": bbody, "userId": buser_id}
        headers = {"Content-type": "application/json; charset=UTF-8"}
        requests.post(
            "https://jsonplaceholder.typicode.com/posts", json=body, headers=headers
        ).json()
        self.post_id = 2

    def tearDown(self):
        requests.delete(f"https://jsonplaceholder.typicode.com/posts/{self.post_id}")

    def test_get_one_post(self):
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/posts/{self.post_id}"
        ).json()
        self.assertEqual(response["id"], self.post_id)


class TestWithoutFixtures(unittest.TestCase):

    @unittest.skip("Reason: Dont need this test to be run")
    def test_get_all_posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        self.assertEqual(len(response), 100)

    @unittest.skipIf(sys.platform == "darwin", "Not for macOS run")
    def test_add_post(self):
        btitle = "Hello world"
        bbody = "Nice to see you"
        buser_id = 444
        body = {"title": btitle, "body": bbody, "userId": buser_id}
        headers = {"Content-type": "application/json; charset=UTF-8"}
        responce = requests.post(
            "https://jsonplaceholder.typicode.com/posts", json=body, headers=headers
        )
        self.assertEqual(responce.status_code, 201)
        self.assertEqual(responce.json()["title"], btitle)


"""
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
"""
