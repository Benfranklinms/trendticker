import requests
from bs4 import BeautifulSoup


def get_info():
    url = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYQRLPCQ&marketplace=FLIPKART&q=iphone+15&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&fm=organic&iid=fa230c83-b099-4ad2-98eb-bf7c0fd3f546.MOBGTAGPAQNVFZZY.SEARCH&ppt=hp&ppn=homepage&ssid=v5dlbkshds0000001750672551706&qH=2f54b45b321e3ae5"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("span", class_="VU-ZEz").get_text()
    price = soup.find("div", class_="Nx9bqj CxhGGd").get_text()
    
    return {
        "title": title,
        "price": price
    }