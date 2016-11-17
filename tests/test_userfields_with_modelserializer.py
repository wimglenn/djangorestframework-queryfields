from rest_framework.test import APIClient

from tests.utils import decode_content


def test_model_list_response_unfiltered():
    response = APIClient().get('/snippets/')
    expected = [
        {
            'id': 1,
            'title': 'Fork bomb',
            'code': ':(){ :|: & };:',
            'linenos': False,
            'language': 'bash',
        },
        {
            'id': 2,
            'title': 'French flag',
            'code': "print((u'\x1b[3%s;1m\u2588'*78+u'\n')%((4,)*26+(7,)*26+(1,)*26)*30)",
            'linenos': False,
            'language': 'python',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_model_detail_response_unfiltered():
    response = APIClient().get('/snippets/3/')
    expected = {
        'id': 3,
        'title': 'Russian roulette',
        'code': '[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo "click"',
        'linenos': False,
        'language': 'bash',
    }
    content = decode_content(response)
    assert content == expected


def test_model_list_response_filtered_includes():
    response = APIClient().get('/snippets/?fields=title,language')
    expected = [
        {
            'title': 'Fork bomb',
            'language': 'bash',
        },
        {
            'title': 'French flag',
            'language': 'python',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_model_detail_response_filtered_includes():
    response = APIClient().get('/snippets/3/?fields=title,language')
    expected = {
        'title': 'Russian roulette',
        'language': 'bash',
    }
    content = decode_content(response)
    assert content == expected


def test_model_list_response_filtered_excludes():
    response = APIClient().get('/snippets/?fields!=code,language')
    expected = [
        {
            'id': 1,
            'title': 'Fork bomb',
            'linenos': False,
        },
        {
            'id': 2,
            'title': 'French flag',
            'linenos': False,
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_model_detail_response_filtered_excludes():
    response = APIClient().get('/snippets/3/?fields!=id,linenos,code')
    expected = {
        'title': 'Russian roulette',
        'language': 'bash',
    }
    content = decode_content(response)
    assert content == expected


def test_model_response_filtered_with_some_bogus_fields():
    response = APIClient().get('/snippets/3/?fields=title,spam,eggs')
    expected = {
        'title': 'Russian roulette',
    }
    content = decode_content(response)
    assert content == expected


def test_model_response_filtered_with_only_bogus_fields():
    response = APIClient().get('/snippets/3/?fields=blah')
    expected = {}
    content = decode_content(response)
    assert content == expected


def test_model_response_filtered_with_multiple_fields_in_separate_query_args():
    response = APIClient().get('/snippets/3/?fields=title&fields=linenos,language')
    expected = {
        'title': 'Russian roulette',
        'linenos': False,
        'language': 'bash',
    }
    content = decode_content(response)
    assert content == expected


def test_model_response_filtered_with_include_and_exclude():
    response = APIClient().get('/snippets/3/?fields=id&fields!=language')
    expected = {
        'id': 3,
    }
    content = decode_content(response)
    assert content == expected


def test_model_exclude_wins_for_ambiguous_filtering():
    response = APIClient().get('/snippets/3/?fields=id,title,code&fields!=id')
    expected = {
        'title': 'Russian roulette',
        'code': '[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo "click"',
    }
    content = decode_content(response)
    assert content == expected
