from behave import *
import requests
from config import *
from utilities.resources import *

TEST_CONFIG = get_config()
GITHUB_URL = TEST_CONFIG['API']['github']
GITHUB_TOKEN = TEST_CONFIG['API']['github_token']
GITHUB_REPO_PATH = TEST_CONFIG['API']['github_repo']
GITHUB_AUTH = f'Bearer {GITHUB_TOKEN}'
GITHUB_GET_HEADER = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": GITHUB_AUTH,
}
GITHUB_PAYLOAD_HEADER = {
    **GITHUB_GET_HEADER,
    "Content-Type": "application/json",
}

# Given I request the latest release of the "a8trejo/github-demo" repo
@given('I request the latest release of the "{text}" repo')
def step_impl(context, text):
    print("...Finding Github Latest Release Tag....")
    get_latest_release_url = f'{GITHUB_URL}/repos/{text}{ApiResources.getLatestRelease}'
    get_latest_release_resp = requests.request(
        "GET", get_latest_release_url, headers=GITHUB_GET_HEADER
    )
    print("...Get Latest Release Status Code: " + str(get_latest_release_resp.status_code))
    assert get_latest_release_resp.status_code == 200
    latest_release_tag = get_latest_release_resp.json().get("tag_name")
    print("...GitHub Latest Release Tag: " + str(latest_release_tag))
    print("---------------------------------------------------------")

    context.latest_release_resp = {**get_latest_release_resp.json()}


# Then I can validate its data
@then('I can validate its data')
def step_impl(context):
    latest_release_name = context.latest_release_resp.get("name")
    print("---------------------------------------------------------")
    print(latest_release_name)
    print("---------------------------------------------------------")
    assert latest_release_name != ''

# Given I search for <branch name> in a PR
@given('I search for {branch_name} in a PR')
def step_impl(context, branch_name):
    print(f"...Searching {branch_name} on Github's PRs....")

    # https://api.github.com/search/issues?q=repo:a8trejo/github-demo+is:pr+bug in:baseRefName
    search_pr_url = f'{GITHUB_URL}/search/issues?q=repo:{GITHUB_REPO_PATH}+is:pr+{branch_name} in:baseRefName'
    search_pr_resp = requests.request(
        "GET", search_pr_url, headers=GITHUB_GET_HEADER
    )
    assert search_pr_resp.status_code == 200
    search_pr_json = search_pr_resp.json()

    print("...Status Code: " + str(search_pr_resp.status_code))
    print(f"...PR Name: {search_pr_json.get('items')[0].get('title')}")
    print("---------------------------------------------------------")

    context.search_pr_json = {**search_pr_json}

# Then I can get the PR body
@then('I can get the PR body')
def step_impl(context):
    # https://api.github.com/repos/{{REPO_PATH}}/pulls/:{pull_number}
    pr_number = context.search_pr_json.get('items')[0].get('number')
    get_pr_url = f'{GITHUB_URL}/repos/{GITHUB_REPO_PATH}/pulls/{pr_number}'
    get_pr_resp = requests.request(
        "GET", get_pr_url, headers=GITHUB_GET_HEADER
    )
    context.latest_code = get_pr_resp.status_code
    # assert get_pr_resp.status_code == 200

# And status code should be 200
# There is no @and
@then('status code should be {status_code:d}')
def step_imp(context, status_code):
    assert context.latest_code == status_code
