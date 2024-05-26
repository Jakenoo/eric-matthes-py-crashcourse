#26/5/2024; example in chapter 17
import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

#Make an API call, store response in response_dict
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

#Gather values from their respective keys
repo_dicts = response_dict['items']
repo_names, repo_links, stars, hover_texts = [], [], [], []
for repo_dict in repo_dicts:
    #append repo names to list above; never got this to work with hover texts
    #and links at the same time
    repo_name = repo_dict['name']
    repo_names.append(repo_name)
    #create layout for turning repo names into active links
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    #gather star count
    stars.append(repo_dict['stargazers_count'])
    #build hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    #HTML line break
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#Setup for style of graph
title = "Most Starred Python Projects on Github"
labels = {'x': 'Repository', 'y':'Stars'}

#Make visualization
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
             hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()