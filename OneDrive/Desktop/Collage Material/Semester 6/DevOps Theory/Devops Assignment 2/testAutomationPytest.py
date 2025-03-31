import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4),
    ("http://localhost:8000/subtract/5/3", 2),
    ("http://localhost:8000/multiply/2/3", 6),
]

@pytest.mark.parametrize("url, expected", testcases)
def test_api(url, expected):
    response = requests.get(url)
    assert response.json()["result"] == expected
