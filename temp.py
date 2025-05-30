import requests

def fetch_todos():
    response = requests.get("API網址")
    data = response.json()
    todos = data["data"]