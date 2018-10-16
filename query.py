from bs4 import BeautifulSoup
import re
import requests
import sys

BASE_QUERY_CS_URL = "https://directory.utexas.edu/index.php?q=%28%26%28cn%3D{0}*%29%28utexasEduPersonMajor%3D*Compute"\
                    "r+Science%2C+Entry-Level*%29%29&scope=student&submit=Search"


def make_query(name):
    return_html = requests.get(BASE_QUERY_CS_URL.format(name)).text
    soup = BeautifulSoup(return_html, 'html.parser')
    raw_names = str(soup.find_all("a", href=lambda href: href and "index.php?q=%28%26%28cn%3D" in href))
    return masterclean(raw_names)


def masterclean(raw_html):
    html_purged = re.sub(re.compile('<.*?>'), '', raw_html)
    html_purged = html_purged[1:len(html_purged)-1]
    names = re.split(r"[\s\W]*,[\s\W]*", html_purged)
    return [name.strip() for name in names]


if len(sys.argv) != 2:
    raise ValueError("Usage: query.py <name>")

query = sys.argv[1].lower().strip()
print(make_query(query))
