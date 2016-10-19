from tests.utils import assert_response


def test_model_list_response_unfiltered(client):
    response = client.get('/snippets/')
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
    assert_response(response, expected_content=expected)


def test_model_detail_response_unfiltered(client):
    response = client.get('/snippets/3/')
    expected = {
        'id': 3,
        'title': 'Russian roulette',
        'code': '[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo "click"',
        'linenos': False,
        'language': 'bash',
    }
    assert_response(response, expected_content=expected)


def test_model_list_response_filtered_includes(client):
    response = client.get('/snippets/?fields=title,language')
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
    assert_response(response, expected_content=expected)


def test_model_detail_response_filtered_includes(client):
    response = client.get('/snippets/3/?fields=title,language')
    expected = {
        'title': 'Russian roulette',
        'language': 'bash',
    }
    assert_response(response, expected_content=expected)


def test_model_list_response_filtered_excludes(client):
    response = client.get('/snippets/?fields!=code,language')
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
    assert_response(response, expected_content=expected)


def test_model_detail_response_filtered_excludes(client):
    response = client.get('/snippets/3/?fields!=id,linenos,code')
    expected = {
        'title': 'Russian roulette',
        'language': 'bash',
    }
    assert_response(response, expected_content=expected)


def test_model_response_filtered_with_some_bogus_fields(client):
    response = client.get('/snippets/3/?fields=title,spam,eggs')
    expected = {
        'title': 'Russian roulette',
    }
    assert_response(response, expected_content=expected)


def test_model_response_filtered_with_only_bogus_fields(client):
    response = client.get('/snippets/3/?fields=blah')
    expected = {}
    assert_response(response, expected_content=expected)


def test_model_response_filtered_with_multiple_fields_in_separate_query_args(client):
    response = client.get('/snippets/3/?fields=title&fields=linenos,language')
    expected = {
        'title': 'Russian roulette',
        'linenos': False,
        'language': 'bash',
    }
    assert_response(response, expected_content=expected)


def test_model_response_filtered_with_include_and_exclude(client):
    response = client.get('/snippets/3/?fields=id&fields!=language')
    expected = {
        'id': 3,
    }
    assert_response(response, expected_content=expected)


def test_model_exclude_wins_for_ambiguous_filtering(client):
    response = client.get('/snippets/3/?fields=id,title,code&fields!=id')
    expected = {
        'title': 'Russian roulette',
        'code': '[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo "click"',
    }
    assert_response(response, expected_content=expected)
