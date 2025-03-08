import requests
from datetime import datetime


start_time = datetime.now()
response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response)
end_time = datetime.now()

print(end_time - start_time)