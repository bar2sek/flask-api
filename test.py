import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Wow! What a dumb video!", "views": 20},
        {"likes": 45, "name": "How to program", "views": 500},
        {"likes": 123420, "name": "Why python is cool", "views": 3231231234},
        {"likes": 2345, "name": "Shoveling snow", "views": 3211231}]

for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())