import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")
content = response.text

soup = BeautifulSoup(content, "html.parser")
score = soup.find_all(name="span", class_="score")
score2 = [point.getText() for point in score]
score3 = [int(point.split()[0]) for point in score2]
print(score3)
maxim = max(score3)



title = soup.find_all(name="span", class_="titleline")
title2 = [text.getText() for text in title]
print(title2)

print(max(score3))

for i in range(0,len(score3),1):
    if maxim == score3[i]:
        break

print("Maximum\n")
print(maxim)
print(title2[i])
