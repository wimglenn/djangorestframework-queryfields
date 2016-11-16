from django.test import Client

from tests.utils import decode_content


def test_list_response_unfiltered():
    response = Client().get('/quotes/')
    expected = [
        {
            'character': 'Customer',
            'line': "It's certainly uncontaminated by cheese",
            'sketch': 'CHEESE SHOP',
        },
        {
            'character': 'The Black Knight',
            'line': "It's just a flesh wound",
            'sketch': 'HOLY GRAIL',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_detail_response_unfiltered():
    response = Client().get('/quotes/parrot/')
    expected = {
        'character': 'Shopkeeper',
        'line': "Well, he's...he's, ah...probably pining for the fjords",
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected


def test_list_response_filtered_includes():
    response = Client().get('/quotes/?fields=character,line')
    expected = [
        {
            'character': 'Customer',
            'line': "It's certainly uncontaminated by cheese",
        },
        {
            'character': 'The Black Knight',
            'line': "It's just a flesh wound",
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_detail_response_filtered_includes():
    response = Client().get('/quotes/parrot/?fields=character,line')
    expected = {
        'character': 'Shopkeeper',
        'line': "Well, he's...he's, ah...probably pining for the fjords",
    }
    content = decode_content(response)
    assert content == expected


def test_list_response_filtered_excludes():
    response = Client().get('/quotes/?fields!=character')
    expected = [
        {
            'line': "It's certainly uncontaminated by cheese",
            'sketch': 'CHEESE SHOP',
        },
        {
            'line': "It's just a flesh wound",
            'sketch': 'HOLY GRAIL',
        },
    ]
    content = decode_content(response)
    assert content == expected


def test_detail_response_filtered_excludes():
    response = Client().get('/quotes/parrot/?fields!=character')
    expected = {
        'line': "Well, he's...he's, ah...probably pining for the fjords",
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected


def test_response_filtered_with_some_bogus_fields():
    response = Client().get('/quotes/parrot/?fields=sketch,spam,eggs')
    expected = {
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected


def test_response_filtered_with_only_bogus_fields():
    response = Client().get('/quotes/parrot/?fields=blah')
    expected = {}
    content = decode_content(response)
    assert content == expected


def test_response_filtered_with_multiple_fields_in_separate_query_args():
    response = Client().get('/quotes/parrot/?fields=character&fields=sketch')
    expected = {
        'character': 'Shopkeeper',
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected


def test_response_filtered_with_include_and_exclude():
    response = Client().get('/quotes/parrot/?fields=character&fields=sketch&fields!=line')
    expected = {
        'character': 'Shopkeeper',
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected


def test_exclude_wins_for_ambiguous_filtering():
    response = Client().get('/quotes/parrot/?fields=line,sketch&fields!=line')
    expected = {
        'sketch': 'PET SHOP',
    }
    content = decode_content(response)
    assert content == expected
