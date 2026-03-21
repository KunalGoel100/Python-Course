import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
content = response.text

soup = BeautifulSoup(content,"html.parser")
temp = soup.find_all(name="h3", class_="title")

names = [name.getText() for name in temp]

file = open("Top100_Movies.txt","w",encoding="utf-8")

for i in names:
    print(i)
    file.write(f"{i}\n")
file.close()

