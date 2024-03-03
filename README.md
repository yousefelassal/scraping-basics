<div align="center">
  
# web scraping w/ bs4

</div>

#### create a BeautifulSoup object from a webpage:
```py
soup = BeautifulSoup(webpage.content, "html.parser")
```

#### Within the `soup` object, tags can be called by name:
```py
first_div = soup.div
```

#### or by CSS selector:
```py
all_elements_of_header_class = soup.select(".header")
```

#### or by a call to `.find_all`:
```py
all_p_elements = soup.find_all("p")
```

#### We can get the children of a tag by accessing the `.children` attribute:
```py
for child in soup.ul.children:
    print(child)
```

#### We can also navigate up the tree of a tag by accessing the `.parents` attribute:
```py
for parent in soup.li.parents:
    print(parent)
```
