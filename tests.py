import pytest 
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Treinar bjj",
        "description": "Toda segunda"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=(new_task_data))
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json


def test_get_all_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task_by_id():
    ID = 1
    response = requests.get(f"{BASE_URL}/tasks/{ID}")
    response_json = response.json()

    assert response.status_code == 200
    assert ID  == response_json["id"]



def test_update_task():
    ID = 1
    payload = {
        "title": "Treinar boxe",
        "description": "",
        "completed": True
    }

    response = requests.put(f"{BASE_URL}/tasks/{ID}", json=payload)
    response_json = response.json()
    response.status_code == 200
    assert "message" in response_json

    # Nova requisição tarefa especifica
    response = requests.get(f"{BASE_URL}/tasks/{ID}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["description"] == payload["description"]
    assert response_json["completed"] == payload["completed"]


def delete_task():
    ID = 1
    response = requests.delete(f"{BASE_URL}/tasks/{ID}")
    response.status_code == 200
    response_json = response.json()
    assert "message" in response_json


    # Verifica se a tarefa especifica foi deletada 
    response = requests.get(f"{BASE_URL}/tasks/{ID}")
    assert response.status_code == 404
