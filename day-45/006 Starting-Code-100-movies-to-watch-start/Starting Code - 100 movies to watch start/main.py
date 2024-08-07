import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text)

movie_titles = soup.select("section .title")

movie_list = []

for movie in movie_titles:
    movie_list.insert(0, movie.getText())
    

with open("100_greatest_movies.txt", "w", encoding="utf-8") as f:
    for movie in movie_list:
        f.write(f"{movie}\n")