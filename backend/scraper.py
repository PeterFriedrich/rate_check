# beautiful soup scraping test script
import requests
from bs4 import BeautifulSoup

# request the whole html page?
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# soup object, uses python html parser
soup = BeautifulSoup(page.content, "html.parser")
# soup find containers by id
results = soup.find(id="ResultsContainer")

# find all python header 2 python jobs
python_jobs = results.find_all(
	"h2", string=lambda text: "python" in text.lower()
	)

# other information is in the parent^3 of the h2 "python"
python_job_cards = [
	h2_element.parent.parent.parent for h2_element in python_jobs]

# for loop each job card. find each element, h2:title etc.
# print out stripped text
for job_card in python_job_cards:
	title_element = job_card.find("h2", class_="title")
	company_element = job_card.find("h3", class_="company")
	location_element = job_card.find("p", class_="location")
	print(title_element.text.strip())
	print(company_element.text.strip())
	print(location_element.text.strip())
	#print(location_element) would print all the html
	# find <a> tags in card. read href
	#print(job_card.find_all("a")) would print whole tag
	link_url = job_card.find_all("a")[1]["href"]
	print(f"Apply here: {link_url}\n")

