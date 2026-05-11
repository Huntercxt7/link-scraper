import requests
from bs4 import BeautifulSoup

url = "https://community.chocolatey.org/packages/visualstudio2019buildtools/16.0.0.0"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = []

for a in soup.find_all("a"):
    href = a.get("href")
    if href:
        links.append(href)

with open("links.txt", "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print("done")
