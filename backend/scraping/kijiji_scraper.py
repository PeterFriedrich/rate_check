import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

listing_url = "https://www.kijiji.ca/b-edmonton/tutor/k0l1700203?dc=tru"
# create a function to scrape all the top listing links

def listings_scrape(listing_url):
    # input: url of the listing page
    # output: list of urls of the top listings

    response = requests.get(listing_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all the listing links on page
    all_links = soup.find_all('a')

    # get the href, convert to absolute urls
    urls = []
    for link in all_links:
        href = link.get('href')
        if href and "v-" in href:
            absolute_url = urljoin(listing_url, href)
            urls.append(absolute_url)

    return urls

    
