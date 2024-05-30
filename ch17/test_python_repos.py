#29/5/2024; exercise 17-3
from python_repos import get_repo_info, format_response, get_repo_dict

def test_status_code():
    r = get_repo_info()
    assert r.status_code == 200

def test_repo_dict():
    """asserts each repository returned has >10000 stars"""
    r = get_repo_info()
    response_dict = format_response(r)
    repo_dicts = get_repo_dict(response_dict)
    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10000