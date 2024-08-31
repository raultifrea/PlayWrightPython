from playwright.sync_api import *
import pytest

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
        api_context = playwright.request.new_context(
        base_url='https://dummyjson.com',
        extra_http_headers={'Content-Type': 'application/json'}
    )
        yield api_context
        api_context.dispose()

def test_users_api(api_context: APIRequestContext):
    query = 'Emily'
    response = api_context.get(f'/users/search?q={query}')
    # response_products = api_context.get('/products')

    user_data = response.json() #dictionary

    print("Users found:", user_data['total'])

    for user in user_data['users']:
          print('Checking user:', user['firstName'])
          assert query in user['firstName']


def test_create_user(api_context: APIRequestContext):

    # api_context.fetch(
    #       "users/add",
    #       method="POST",
    #        data={
    #              "firstName": "Raul",
    #              "lastName": "Tifrea",
    #              "age": 32
    #        } 
    # )
    #same as:

    response = api_context.post(
          "users/add",
           data={
                 "firstName": "Raul",
                 "lastName": "Tifrea",
                 "age": 32
           }  
        )
    user_data = response.json()
    print(f'\n{user_data}')

    assert user_data['id'] == 209
    assert user_data['firstName'] == "Raul"

def test_update_user(api_context: APIRequestContext):
      print(api_context.get('users/1').json()["lastName"])
      response = api_context.put(
          "users/1",
          data= {
                "lastName": "NewLastName",
                "age": 20
          }
      )
      user_data = response.json()
      print(user_data)
      assert user_data['lastName'] == "NewLastName"
      assert user_data['age'] == 20

def test_delete_user(api_context: APIRequestContext):
      api_context.delete('users/1')

def on_api_call(route: Route):
        response = route.fetch()
        user_data = response.json()
        user_data['lastName'] = "Tifrea"
        user_data['age'] = 20
        route.fulfill(
                response=response,
                json=user_data,
                )

def test_mock_api(page: Page):
        USERS_API_URL = 'https://dummyjson.com/users/1'

        page.route(USERS_API_URL, on_api_call)
        response = page.goto(USERS_API_URL)
        print("Got data:", response.json())