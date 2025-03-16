# main script for running scraping funcs

from kijiji_scraper import *

listing_url = "https://www.kijiji.ca/b-edmonton/tutor/k0l1700203?dc=tru"

for entry in listings_scrape(listing_url):
    print(entry)
    print('\n')

