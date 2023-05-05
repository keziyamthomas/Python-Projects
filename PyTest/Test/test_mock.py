import requests
from Code import app

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key":"mock_value"}

def test_get_json_from_url(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests,"get",mock_get)
    result = app.get_json("https://someurl")
    assert result["mock_key"] == "mock_value"