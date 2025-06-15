import requests

def test_health():
    res = requests.get("http://localhost:8000/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

if __name__ == "__main__":
    test_health()
