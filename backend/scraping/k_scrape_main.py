# main script for running scraping funcs

from kijiji_scraper import *

main_listing_page_url = "https://www.kijiji.ca/b-edmonton/tutor/k0l1700203?dc=tru"


# grabbing specific listings to scrape them
listings_urls = listings_scrape(main_listing_page_url)