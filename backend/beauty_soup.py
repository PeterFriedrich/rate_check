# beautiful soup again
# can run:
# python -i beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# open url, decode the bytes to html, run parser
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# grabs all text, with newlines
all_text = soup.get_text()
text_no_space = re.sub(r'\n+', '\n', all_text) 

# grab all img tags
img_tags = soup.find_all("img")

# grab specific ones
special_im = soup.find_all("img", src="/static/dionysus.jpg")
