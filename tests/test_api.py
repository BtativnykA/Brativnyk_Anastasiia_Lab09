import pytest
from fastapi.testclient import TestClient
from student_manager.api import app
from student_manager.models import Group, Student

client = TestClient(app)

def test_create_and_get_student(db_session):
    # Цей тест залежить від вашої фікстури db_session
    # Для простоти перевіримо тільки валідацію (422)
    response = client.post("/students", json={
        "first_name": "Anna",
        "last_name": "Koval",
        "group_id": 1,
        "average_grade": 150  # Невалідне значення
    })
    assert response.status_code == 422  # Pydantic відхилив

def test_get_missing_student():
    response = client.get("/students/9999")
    assert response.status_code == 404