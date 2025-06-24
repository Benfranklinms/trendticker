import requests
from bs4 import BeautifulSoup


def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("span", class_="VU-ZEz").get_text()
    price = soup.find("div", class_="Nx9bqj CxhGGd").get_text()
    image_tag = soup.find("img", class_="DByuf4 IZexXJ jLEJ7H")
    
    image = image_tag["src"]
    
    return {
        "title": title,
        "price": price,
        "image": image
    }