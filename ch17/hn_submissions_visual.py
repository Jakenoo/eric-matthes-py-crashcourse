#26/5/2024; more API practice
from operator import itemgetter
import requests
import plotly.express as px

#Make API call, verify response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#format info from each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:21]:
    #Make new API call per submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #build dictionary per article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    #skip promotional articles and print notice of omission
    except KeyError:
        print(f"Submission {submission_id} omitted; restricted post.")
        continue
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

#print info on top 20 articles
# print(len(submission_dicts))
# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")

#data setup for graph
article_links, comments = [], []
for dict in submission_dicts:
    #create links out of article titles
    article_url = dict['hn_link']
    article_name = dict['title']
    
    #append link to list for graph
    article_link = f"<a href='{article_url}'>{article_name}</a>"
    article_links.append(article_link)
    comments.append(dict['comments'])

#make bar graph
fig = px.bar(x=article_links, y=comments, title="Top 20 articles on HackerNews and"
             +" Corresponding Comments", labels={"x": "Article Titles", 
                                                 "y": "Comments"})
fig.show()