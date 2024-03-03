import requests
import re
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# print(soup.prettify()) 
# print(soup.div)
# print(soup.div.attrs)
# print(soup.div.span.string)

# for child in soup.div.children:
#     print(child.string)

# print(soup.find_all("h1"))

# print(soup.find_all(re.compile("[ou]l")))

print(soup.find_all(["h1", "a"]))