from django.test import override_settings
from rest_framework.test import APIClient

from tests.utils import decode_content


@override_settings(DRF_QUERYFIELDS_EXCLUDE_ARG_NAME="omit")
def test_list_response_filtered_excludes():
    response = APIClient().get('/quotes/?omit=line')
    expected = [
        {
            'character': 'Customer',
            'sketch': 'CHEESE SHOP',
        },
        {
            'character': 'The Black Knight',
            'sketch': 'HOLY GRAIL',
        },
    ]
    content = decode_content(response)
    assert content == expected
