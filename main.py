import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

# print(soup.prettify()) 
print(soup.div)
print(soup.div.attrs)
print(soup.div.span.string)