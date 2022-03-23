import requests
import time

url = "http://127.0.0.1:8000/shot_get"

index = 0

while True:
    params = {
        "index": index
    }

    response = requests.get(url=url, params=params)
    response_data = response.json()
    data = response_data.get("message")
    index = index + len(data)
    for item in data:
        print(item.get("message"))

    time.sleep(2)


