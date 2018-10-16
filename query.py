from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

# TODO: Should we make this search for exact names? Right now "Daniel" also returns "Danielle"
BASE_QUERY_CS_URL = "https://directory.utexas.edu/index.php?q=%28%26%28cn%3D{0}*%29%28utexasEduPersonMajor%3D*Compute"\
                    "r+Science%2C+Entry-Level*%29%29&scope=student&submit=Search"


def make_query(name):
    return_html = requests.get(BASE_QUERY_CS_URL.format(name)).text
    soup = BeautifulSoup(return_html, 'html.parser')
    raw_names = str(soup.find_all("a", href=lambda href: href and "index.php?q=%28%26%28cn%3D" in href))
    return master_clean(raw_names)


def master_clean(raw_html):
    html_purged = re.sub(re.compile('<.*?>'), '', raw_html)
    html_purged = html_purged[1:len(html_purged)-1]
    names = re.split(r"[\s\W]*,[\s\W]*", html_purged)
    return [name.strip() for name in names]


name_list = []
master_list = []

# Create a list of names from text file
with open('search_names.txt') as f:
    for line in f:
        name_list.append(line.rstrip('\n'))

# TODO: @Stefan make this more Pythonic
for individual_name in name_list:
    returned_names = make_query(individual_name)

    # TODO: add check for 'vCard', we also need to figure out what happens when no names are returned
    for single_name in returned_names:
        master_list.append(single_name)

# Create a Pandas dataframe from master_list
df = pd.DataFrame(master_list, columns=["Name"])
# Export dataframe to CSV
df.to_csv('names.csv', index=False)
