# CH17 Example
#
# python_repos.py
#
# Processing an API Response; pages 379 - 383
# Example of issuing an API call and process results from Github
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# requests makes the actual API call using its get() method
# r is the response object
r = requests.get(url)

# This returns status code 200, which means successful response
print("Status code:", r.status_code)

# Store API response in a variable.  Actual response is json() method of r
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# Examine first repository
repo_dict = repo_dicts[0]

# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# Pull out values for some of the keys found from repo_dict
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print("\nName: ", repo_dict['name'])
#     print("Owner: ", repo_dict['owner']['login'])
#     print("Stars: ", repo_dict['stargazers_count'])
#     print("Repository: ", repo_dict['html_url'])
#     print("Created: ", repo_dict['created_at'])
#     print("Updated: ", repo_dict['updated_at'])
#     print("Description: ", repo_dict['description'])

# Need the repository names to use as x-axis labels
# and stars to use as y-axis quantities
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualize the repositories using pygal Bar graph
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')


# Process results
# Output is: dict_keys(['total_count', 'incomplete_results', 'items'])
# print(response_dict.keys())
