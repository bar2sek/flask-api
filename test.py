import requests

BASE = "http://0.0.0.0:5000/"

data = [{"likes": 10, "name": "Wow! What a dumb video!", "views": 20},
        {"likes": 45, "name": "How to program", "views": 500},
        {"likes": 123420, "name": "Why python is cool", "views": 3231231234},
        {"likes": 2345, "name": "Shoveling snow", "views": 3211231}]

for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", data[i])
    print(response.json())

input()

response = requests.patch(BASE + "video/2", {"views": 99, "likes": 101})
print(response.json())