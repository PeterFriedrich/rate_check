# building first web scraper real python tutorial

# urllib python url tools
from urllib.request import urlopen


url = "http://olympus.realpython.org/profiles/aphrodite"

# return httpresponse object
page = urlopen(url)

# read the bytes, decode utf-8
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

print(f"This html variable is just type: {type(html)}")
print(f"As an example, this is me slicing [0:50]")
print(html[0:50], "\n")

# can now use .find() string method, string slice
print("We want to use find to get <title>")
title_index = html.find("<title>")
print(f"This is just the index tho: {title_index}")
start_index = title_index + len("<title>")
print(f"This is the start index: {start_index}")
end_index = html.find("</title>")
print(f"This is the end tag index: {end_index}")
# we now slice across the index
title = html[start_index:end_index]
print(f"This is the title: {title}, \n")

url2 = "http://olympus.realpython.org/profiles/poseidon"

def page_opener(url):
	# takes in the url and returns the page html
	page = urlopen(url)
	html = page.read().decode("utf-8")
	start_index = html.find("<title>") + len("<title>")
	end_index = html.find("</title>")
	title = html[start_index:end_index]
	return title

print("Trying to print aphrodite title:", page_opener(url))
print("Trying to print poseidon title:", page_opener(url2))

# bruh title was slightly differnt, so -1 was returned for the index

# regular expressions
import re

# this matches a start, c end, *any amount of b, including 0
re.findall("ab*c", "ac")

k_url =  "https://www.kijiji.ca/b-services/edmonton/tutor/k0c72l1700203"
