import requests

url = "http://127.0.0.1:8000/long_get"


def long_get(uid):
    params = {
        "uid": uid
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        print(response.text)
        long_get(uid)
    elif response.status_code == 400:
        long_get(uid)


if __name__ == '__main__':
    long_get(uid="test1")
