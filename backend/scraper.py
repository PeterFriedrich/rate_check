import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# test comment

print(page.text)
