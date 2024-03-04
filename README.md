<div align="center">
  
# web scraping w/ [bs4](https://beautiful-soup-4.readthedocs.io/en/latest/)

</div>

#### create a BeautifulSoup object from a webpage:
```py
soup = BeautifulSoup(webpage.content, "html.parser")
```

#### Within the `soup` object, tags can be called by name:
```py
first_div = soup.div
```

#### or by CSS selector (select by classname):
```py
all_elements_of_header_class = soup.select(".header")
```


#### select by id
```py
soup.select("#selected")
```

#### loop through all of the links inside a `.recipieLink` div
```py
for link in soup.select(".recipeLink > a"):
  webpage = requests.get(link)
  new_soup = BeautifulSoup(webpage)
```

#### or by a call to `.find_all`:
```py
all_p_elements = soup.find_all("p")
```

#### We can use `.get_text()` to retrieve the text inside of whatever tag we want to call it on.
```html
<h1 class="results">Search Results for: <span class='searchTerm'>Funfetti</span></h1>
```
If this is the HTML that has been used to create the soup object, we can make the call:
```py
soup.get_text()
```
Which will return:
```txt
'Search Results for: Funfetti'
```

#### We can use the `.compile()` function from the re module.
We will use the regex: `[ou]l` which means “match either o or u and l“.
```py
import re
soup.find_all(re.compile("[ou]l"))
```

#### We can also just specify all of the elements we want to find by supplying the function with a list of the tag names we are looking for:
```py
soup.find_all(['h1', 'a', 'p'])
```

#### We can pass a dictionary to the attrs parameter of find_all with the desired attributes of the elements we’re looking for. 
```py
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})
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
