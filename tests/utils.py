import json


def assert_response(response, expected_status_code=200, expected_content=None):
    assert response.status_code == expected_status_code
    try:
        content = response.json()
    except AttributeError:
        content = json.loads(response.content)
    assert content == expected_content
