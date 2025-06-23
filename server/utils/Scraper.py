import requests
from bs4 import BeautifulSoup

def get_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Print first 1000 chars of HTML for debug (optional)
    # print(soup.prettify()[:1000])

    title_tag = soup.find("span", class_="VU-ZEz")
    price_tag = soup.find("div", class_="Nx9bqj CxhGGd")
    image_tag = soup.find("img", class_="DByuf4 IZexXJ jLEJ7H")

    if not title_tag or not price_tag or not image_tag:
        raise Exception("❌ Could not find product details — class names may have changed or access blocked.")

    title = title_tag.get_text(strip=True)
    price = price_tag.get_text(strip=True)
    image = image_tag.get("src")

    return {
        "title": title,
        "price": price,
        "image": image
    }
