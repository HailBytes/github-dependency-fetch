# Python program to scrape github insight dependencies 
# list and produce a dependency list SBOM

# Module to make network requests and handle sessions
import requests

# Module to pull cookie data from chrome using SQLite for injection
from pycookiecheat import chrome_cookies

# Module to handle DOM manipulation
from bs4 import BeautifulSoup

# Instantiate a session to inject cookies into
session = requests.Session()

organization = "HailBytes"

# Define the Github Insights dependency page
start_url = "https://github.com/orgs/%s/insights/dependencies".format(organization)
current_url = start_url
# Retrieve the Github cookies from Chrome
cookies = chrome_cookies(start_url)

# Create a list to store the dependency names
dependencies = []

def get_dependencies_for_url(url, cookies):

	# Inject the cookies into the session and retrieve the dependency URL
	response = session.get(url, cookies = cookies)

	# Parse the dependency URL using BeautifulSoup's html5lib parser
	soup = BeautifulSoup(response.content, 'html5lib')

	# Pull all the elements containing dependency names
	dependency_list = soup.find_all("a", class_="js-navigation-open")

	# Iterate over the dependency elements
	for dep in dependency_list:
		# Check if there is a dependency name
		#if dep.string is not None:
		# Print out the dependency name for reference
		print(dep.string)
		# Append the dependency name for export
		if dep.string:
			dependencies.append(str(dep.string).strip())

	# Print the dependencies for review
	print(dependencies)

	# Grab the URL for the next page of results
	next_url = soup.select_one("a[href*=after]")

	# Print the URL for review
	print(next_url['href'])

	# Return the URL for the next iteration
	return next_url['href']

# This entire section should be iterated to failure by grabbing
# the "next" HREF as the last action and triggering another pull
iterations = 313

while iterations > 1:
	current_url = get_dependencies_for_url(current_url, cookies)
	iterations = iterations - 1

# Export the dependency list
filename = 'github_dependencies_7_6_22.txt'
with open(filename, 'w', newline='') as f:
  f.write(str(dependencies))

