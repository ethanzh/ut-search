import requests
import re
from bs4 import BeautifulSoup

base_query_cs_url = "https://directory.utexas.edu/index.php?q=%28%26%28cn%3D{0}*%29%28utexasEduPersonMajor%3D*Compute" \
                    "r+Science%2C+Entry-Level*%29%29&scope=student&submit=Search"

return_html = requests.get(base_query_cs_url.format("ethan")).text

soup = BeautifulSoup(return_html, 'html.parser')

print(soup.prettify())

print(soup.find_all("a", href=lambda href: href and "index.php?q=%28%26%28cn%3D" in href))

