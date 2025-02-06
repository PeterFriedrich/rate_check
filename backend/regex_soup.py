# using regex to scrape a webpage

import re
from urllib.request import urlopen

# target:
# <TITLE > Profile: Dionysus</title  />

# open page and decode html
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
print("\n" + "First 60 chars of html: \n" + html[:60] + "\n")

# match title pattern: open title, any text after
# any text middle, close title any text after
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # remove html tags

print("After scraping title: \n" + title)
