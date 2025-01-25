import httpx
from bs4 import BeautifulSoup

# empty array for image links
image_links = []
# Scrape the first 4 pages
for page in range(4):
    url = f"URL HERE={page}"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for image_box in soup.select("div.row.product"):
        result = {
            "link": image_box.select_one("img").attrs["src"],
            "title": image_box.select_one("h3").text,
        }
        # Append each image and title to the empty array
        image_links.append(result)
