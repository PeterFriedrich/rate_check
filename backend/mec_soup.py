# mechanical soup lets you browse apparently

import mechanicalsoup

# browser is headless browser.
browser = mechanicalsoup.Browser()

# just get url
url = "http://olympus.realpython.org/login"

# get login page, 
login_page = browser.get(url)
login_html = login_page.soup

#print(login_html)

# select form tag? 
form = login_html.select("form")[0]

# select inputs
print("Select the form:")
print(f"\n{form}\n")
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

print("\nThis is the form with input values added")
print(form, "\n")

# submit inputs, get back the profile page url
profiles_page = browser.submit(form, login_page.url)

print(profiles_page.url)
