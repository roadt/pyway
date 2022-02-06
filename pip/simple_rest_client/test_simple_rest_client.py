
import pytest
from simple_rest_client.api import API

# create api instance
api = API(
    api_root_url='https://reqres.in/api',
    params={},
    headers={},
    timeout=2,
    append_slash=False,
    json_encode_body=True
)
# add users resource
api.add_resource(resource_name='users')

@pytest.fixture
def restapi():
    return api


def test_show_actions(restapi):
    # show resource actions
    actions = restapi.users.actions
    print(actions)
    assert actions == {'list': {'method': 'GET', 'url': 'users'}, 'create': {'method': 'POST', 'url': 'users'}, 'retrieve': {'method': 'GET', 'url': 'users/{}'}, 'update': {'method': 'PUT', 'url': 'users/{}'}, 'partial_update': {'method': 'PATCH', 'url': 'users/{}'}, 'destroy': {'method': 'DELETE', 'url': 'users/{}'}}


def test_list_actions(restapi):
    # list action
    response = api.users.list(body=None, params={}, headers={})
    assert response.url   == 'https://reqres.in/api/users'
    assert response.method  == 'GET'
    assert response.status_code  == 200

    print(response.body)
    body = response.body
    assert len(body['data']) == body['per_page']
    assert response.headers 
    assert response.client_response.cookies != None


def test_create(restapi):
    # create action
    body = {'name': 'morpheus', 'job': 'leader'}
    response = api.users.create(body=body, params={}, headers={})
    assert response.status_code == 201

def test_retrieve(restapi):
    # retrieve action
    response = api.users.retrieve(2, body=None, params={}, headers={})
    assert response.status_code == 200

def test_update(restapi):
    # update action
    body = {'name': 'morpheus', 'job': 'leader'}
    response = api.users.update(2, body=body, params={}, headers={})
    assert response.status_code == 200


def test_partial_update(restapi):
    # partial update action
    body = {'name': 'morpheus', 'job': 'leader'}
    response = api.users.partial_update(2, body=body, params={}, headers={})
    assert response.status_code == 200


def test_destroy(restapi):
    # destroy action
    response = api.users.destroy(2, body=None, params={}, headers={})
    assert response.status_code == 204

