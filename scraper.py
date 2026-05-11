import requests
from bs4 import BeautifulSoup

url = "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-dotnettools/vsextensions/csharp/1.26.0/vspackage
"

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
