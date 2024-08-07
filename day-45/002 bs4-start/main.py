from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

link_titles = soup.select(".titleline a")
article_text = []
article_link = []

for title in link_titles:
    article_text.append(title.getText())
    article_link.append(title.get("href"))

link_votes = [int(score.getText().split()[0]) for score in soup.select("tr .score")]

most_votes = max(link_votes)
most_votes_index = link_votes.index(most_votes)

print(article_text[most_votes_index])
print(article_link[most_votes_index])



# with open("website.html", encoding='utf-8') as file:
#     content = file.read()
    
# soup = BeautifulSoup(content, "lxml")

# all_p_tags = soup.find_all(name="p")
# all_a_tags = soup.find_all(name="a")

# # print(all_a_tags)

# # for tag in all_a_tags:
# #     print(tag.get("href"))

# the_h1 = soup.find(name="h1", id="name")
# the_h3 = soup.select_one(selector=".heading")

# print(the_h3)