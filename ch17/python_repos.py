#29/5/2024; refactored
import requests

def get_repo_info():
    """Make API call and return response"""
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    r = requests.get(url, headers=headers)
    return r

def format_response(response):
    """Returns JSON formatted response from API call"""
    response_dict = response.json()
    return response_dict

def show_repo_info(response_dict):
    """Prints info on each repository from response"""
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

def get_repo_dict(repo_dicts):
    """Returs list of dictionaries for each repository respectively"""
    repo_dicts = repo_dicts['items']
    return repo_dicts

def show_repo_dict_items(repo_dicts):
    """Prints short summary for each repository"""
    print(f"Repositories returned: {len(repo_dicts)}")
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")

r = get_repo_info()
response_dict = format_response(r)
show_repo_info(response_dict)
repo_dicts = get_repo_dict(response_dict)
show_repo_dict_items(repo_dicts)