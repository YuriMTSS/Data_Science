import json
from time import time
import requests
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one/blog/")
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "html.parser")
posts = soup.find_all(class_="post")

all_posts = []
for post in posts:
    info = post.find(class_= 'post content')
    title = info.h2.a.text
    preview = info.p.text
    time = info.find(class_='post_date')['datetime']
    author = post.find(class_ = 'post-author').text

    all_posts.append({
        'title': title,
        'preview': preview,
        'author': author[5:],
        'time': time
    })

print(all_posts)
with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)


