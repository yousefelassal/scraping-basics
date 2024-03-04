import requests
from bs4 import BeautifulSoup

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# print(soup.prettify())

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
    links.append(prefix+a["href"])
    
turtle_data = {}
#follow each link:
for link in links:
    webpage = requests.get(link)
    turtle = BeautifulSoup(webpage.content, "html.parser")
#   print(turtle.prettify())
#   print(turtle.select(".name")[0].get_text())
    turtle_name = turtle.select(".name")[0].get_text()
    turtle_data[turtle_name] = []

print(turtle_data)