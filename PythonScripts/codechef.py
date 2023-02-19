import requests
from bs4 import BeautifulSoup as bs

def codechef():
    r = requests.get("https://codechef.com/users/tharunbalaji31")
    soup = bs(r.content,"html.parser")
    div_number = soup.find("div", {"class":"rating-header text-center"})
    div_number = div_number.find_all("div")
    for tag in div_number:
        print(tag.get_text())