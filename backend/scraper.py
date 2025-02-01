import requests
from bs4 import BeautifulSoup  

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)

# fancy parser? 
soup = BeautifulSoup(page.content, "html.parser")

# find the job container, all containers
results = soup.find(id="ResultsContainer")

# sort by class name: card content
job_cards = results.find_all("div", class_="card-content")

## card_content things, a lot to sort through
#for job_card in job_cards:
#	title_element = job_card.find("h2", class_="title")
#	company_element = job_card.find("h3", class_="company")
#	location_element = job_card.find("p", class_="location")
#	print(title_element.text.strip())
#	print(company_element.text.strip())
#	print(location_element.text.strip())
#	print()

# this filters by string exactly, bad
python_jobs = results.find_all("h2", string="Python")
print("string attempt before this. len jobs:", len(python_jobs))

# pass a function
python_jobs = results.find_all("h2",
	string=lambda text: "python" in text.lower())

print("new job len:", len(python_jobs))

# get python jobs, only h2 in them
for line in python_jobs:
	print(line.text.strip())

#print("Look at one python element:", python_jobs[0])

# to get python job cards, need to go up a level
# didn't go up enough last time
python_job_cards = [
	h2_element.parent.parent.parent for h2_element in python_jobs]

for job_card in python_job_cards:
	title_element = job_card.find("h2", class_="title")
	company_element = job_card.find("h3", class_="company")
	location_element = job_card.find("p", class_="location")
	print(title_element.text.strip())
	print(company_element.text.strip())
	print(location_element.text.strip())
	print()
