import requests


def all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    assert len(response) == 100, "Not all posts returned "


def one_post():
    post_id = 22
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
    assert response["id"] == post_id, f"Not {post_id} id"


def add_post():
    btitle = "Hello world"
    bbody = "Nice to see you"
    buser_id = 444
    body = {"title": btitle, 
            "body": bbody, 
            "userId": buser_id}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    responce = requests.post("https://jsonplaceholder.typicode.com/posts", json=body, headers=headers)
    assert responce.status_code == 201 
    responce = responce.json()
    assert responce["title"] == btitle


def add_new_post():
    btitle = "Hello world"
    bbody = "Nice to see you"
    buser_id = 4
    body = {"title": btitle, 
            "body": bbody, 
            "userId": buser_id}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    responce = requests.post("https://jsonplaceholder.typicode.com/posts", json=body, headers=headers).json()
    return responce["userId"]


def delete_new_post(post_id):
    requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")


def update_post_with_deleting_extra_fields():
    post_id = add_new_post()
    body = {"title": "foo"}
    headers = {"Content-type": "application/json; charset=UTF-8"}
    responce = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=body, headers=headers)
    assert responce.status_code == 200, "Status code NOT 200"
    assert responce.json()["id"] == 4, f"Id NOT 4. Id is {responce.json()["id"]}"
    delete_new_post(post_id=post_id)


def update_post():
    body = {"title": "foo"}
    headers = {"Content-type": "application/json; charset=UTF-8"} 
    #Хедер можно и не передавать для этого сервера, для этого сайта, в любом методе
    responce = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=body, headers=headers).json()
    print(responce)


def delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(response.status_code)


all_posts()
one_post()
add_post()
update_post_with_deleting_extra_fields()
update_post()
delete_post()