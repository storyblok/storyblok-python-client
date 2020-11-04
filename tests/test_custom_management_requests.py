import pytest
import storyblok
import os

user_token = os.getenv('USER_TOKEN')

@pytest.fixture
def client():
    return storyblok.Client()

def test_get(client):
    response = client.get('/spaces/91322/tags/',auth_token=user_token)

    assert response.code == 200
    assert 'tags' in response.body.keys()
    assert type(response.body['tags']) is list

    first_tag = response.body['tags'][0]
    assert 'name'           in first_tag.keys()
    assert 'taggings_count' in first_tag.keys()
