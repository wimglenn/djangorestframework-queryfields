import pytest
from rest_framework.test import APIClient

from tests.app.fields import Kapow
from tests.utils import decode_content


"""
These tests ensure that unneeded fields don't get serialized at all.  The `boom` field on an `ExplosiveSerializer`
will raise error if it is ever serialized, so these tests can guarantee that there is no unnecessary serializing
happening server side when filtering with drf_queryfields.
"""


def test_list_response_unfiltered():
    with pytest.raises(Kapow):
        APIClient().get('/explosives/')


def test_detail_response_unfiltered():
    with pytest.raises(Kapow):
        APIClient().get('/explosives/bunger/')


def test_list_response_filtered_includes():
    response = APIClient().get('/explosives/?fields=safe')
    expected = [{'safe': 'green wire'}, {'safe': 'helium'}]
    content = decode_content(response)
    assert content == expected


def test_detail_response_filtered_includes():
    response = APIClient().get('/explosives/bunger/?fields=safe')
    expected = {'safe': 'tom thumb'}
    content = decode_content(response)
    assert content == expected


def test_list_response_filtered_excludes():
    response = APIClient().get('/explosives/?fields!=boom')
    expected = [{'safe': 'green wire'}, {'safe': 'helium'}]
    content = decode_content(response)
    assert content == expected


def test_detail_response_filtered_excludes():
    response = APIClient().get('/explosives/bunger/?fields!=boom')
    expected = {'safe': 'tom thumb'}
    content = decode_content(response)
    assert content == expected
