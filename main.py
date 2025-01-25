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

# download image objects
for image_object in image_links:
    # create a new .jpg image file
    with open(f"./images/{image_object['title']}.jpg", "wb") as file:
        image = httpx.get(image_object["link"])
        # save the image binary data into the file
        file.write(image.content)
        print(f"Image {image_object['tile']} has been collected")

