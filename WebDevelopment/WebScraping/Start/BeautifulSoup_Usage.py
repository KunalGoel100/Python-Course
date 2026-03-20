from bs4 import BeautifulSoup
import lxml

file = open("website.html",'r')
content = file.read()
# print(content)

soup = BeautifulSoup(content,"html.parser")

allAnchorTags = soup.find_all(name="a")
for tag in allAnchorTags:
    print(tag.getText()) # To get the text
    print(tag.get("href")) # To get the link

print(soup.h1.get("id"))

t = soup.find_all(name="h1", class_="qw")
print(t)

temp = soup.select(selector=".  qw") # select based on CSS identifier
print(temp)