import requests


def get_author():
    resp = requests.get(
        "http://127.0.0.1:8000/author", params={
            "id": 2,
        }
    )
    print(resp.status_code)
    print(resp.json())

def create_author():
    resp = requests.post("http://127.0.0.1:8000/author", json={"name": "test"})
    print(resp.status_code)
    print(resp.json())


def get_channel():
    resp = requests.get(
        "http://127.0.0.1:8000/channel", params={
            "id": 1,
        }
    )
    print(resp.status_code)
    print(resp.json())


def create_channel():
    resp = requests.post(
        "http://127.0.0.1:8000/channel",
        json={
            "author_id": 1,
            "title": "test",
            "login_data": "dvaeaef"
        }
    )
    print(resp.status_code)


def get_post():
    resp = requests.get(
        "http://127.0.0.1:8000/post", params={
            "id": 1,
        }
    )
    print(resp.status_code)
    print(resp.json())


def create_post():
    resp = requests.post(
        "http://127.0.0.1:8000/post",
        json={
            "channel_id": 1,
            "title": "test",
            "text": "wahhhhhhhhhhhhhh"
        }
    )
    print(resp.status_code)


def create_rental():
    data = {
        "items": [
            {"book": 1, "quantity": 5, "price": 780.00},
            {"book": 2, "quantity": 1, "price": 450.00}
        ],
        "start_date": "2026-04-28",
        "end_date": "2026-05-18",
        "reader": 1
    }
    resp = requests.post("http://127.0.0.1:8000/rental", json=data)
    print(resp.status_code)
    print(resp.json())
