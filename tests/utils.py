import json


def decode_content(response, expected_status_code=200):
    assert response.status_code == expected_status_code
    try:
        content = response.json()
    except AttributeError:
        content = json.loads(response.content.decode('utf-8'))
    return content
