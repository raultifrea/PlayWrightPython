import pytest
from playwright.sync_api import Playwright, APIRequestContext
from tests_github.credentials import *

@pytest.fixture(scope='session')
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url='https://api.github.com',
        extra_http_headers= {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {GITHUB_ACCESS_TOKEN}"
        }
    )
    yield context
    context.dispose()

@pytest.fixture(autouse=True, scope='session')
def create_test_repository(api_context: APIRequestContext):
    # Create the test repo
    post_response = api_context.post(
        "/user/repos",
        data={"name": GITHUB_REPO}
    )
    assert post_response.ok, f"Failed to create repo: {post_response.text()}"

    yield

    # Delete the test repo
    delete_response = api_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )
    assert delete_response.ok, f"Failed to delete repo: {delete_response.text()}"