import pytest
import requests
import sys
import numpy as np
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tasks.task_manager import *

def test_create_student_score_matrix():
    mat = create_student_score_matrix(5, 3)
    assert mat.shape == (5, 3)
    assert mat.min() >= 0 and mat.max() <= 100

def test_calculate_mean_per_subject():
    mat = np.array([[50, 60], [70, 80]])
    assert np.allclose(calculate_mean_per_subject(mat), [60, 70])

def test_calculate_student_variance():
    mat = np.array([[50, 70], [80, 80]])
    assert np.allclose(calculate_student_variance(mat), [100, 0])

def test_apply_magic_curve():
    mat = np.array([[90, 95], [100, 85]])
    result = apply_magic_curve(mat)
    expected = np.clip(mat * 1.1, 0, 100)
    assert np.allclose(result, expected)

def test_get_top_students():
    mat = np.array([[90, 95], [60, 65]])
    result = get_top_students(mat, 80)
    assert np.array_equal(result, np.array([0]))

def test_subject_wise_max_scores():
    mat = np.array([[20, 80], [70, 90]])
    assert np.array_equal(subject_wise_max_scores(mat), [70, 90])

def test_slice_students_by_index():
    mat = np.arange(20).reshape(5, 4)
    result = slice_students_by_index(mat, 1, 3)
    assert result.shape == (2, 4)

def test_calculate_subject_std():
    mat = np.array([[10, 20], [30, 40]])
    stds = calculate_subject_std(mat)
    assert len(stds) == 2

def test_normalize_scores():
    mat = np.array([[0, 50], [100, 100]])
    norm = normalize_scores(mat)
    assert norm.min() >= 0 and norm.max() <= 1
    
def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://kaizu-api-8cd10af40cb3.herokuapp.com/projectLog"
    payload = {
        "user_id": 444,
        "project_id": 200,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()
