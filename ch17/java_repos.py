#29/5/2024; some practice with API calls
import requests, plotly.express as px
import pandas as pd

url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"

#Make API call, store response in response_dict in JSON format
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total Repositories: {len(response_dict['items'])}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#sample info on repositories
# print("Here is some information on select repositories:")
# for dict in response_dict['items']:
#     print(f"\nRepository name: {dict['name']}")
#     print(f"Github Owner: {dict['owner']['login']}")
#     print(f"Number of Stars: {dict['stargazers_count']}")
#     print(f"URL: {dict['html_url']}")

#setup for graph
names, stars = [], []
for dict in response_dict['items']:
    names.append(dict['name'])
    stars.append(dict['stargazers_count'])

#create matrix/table for plotting
data = []
data.append(names)
data.append(stars)
data_frame = pd.DataFrame(data).transpose()
data_frame.columns = ['Repositories', 'Stars']

title = "Most Starred Java repositories on Github"

#create graph
fig = px.bar(data_frame=data_frame, x='Repositories', y='Stars', title=title)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='DarkOrchid')
fig.show()