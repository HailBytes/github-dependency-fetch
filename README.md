![up](https://user-images.githubusercontent.com/35319750/178548717-ffb33bde-68c3-47eb-8f89-df061ffbc1b1.png)
# github-dependency-fetch
Python CLI tool to use the requests library and pyCookieSteal to impersonate your GitHub session and export your dependency insights in a text format.

1. Log into your GitHub account with Google Chrome.
2. Update the dependency_fetch.py script with your Organization URL if using GitHub Advanced Security to pull organization-wide, or your repository insights URL if using regular GitHub. (ex: https://github.com/HailBytes/github-dependency-fetch/network/dependencies)

3. Run the dependency_fetch.py script, your dependencies will be output in the console and written to a text file in the same directory as the dependency_fetch.py script.
