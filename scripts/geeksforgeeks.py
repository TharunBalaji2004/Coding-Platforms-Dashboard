import requests
from bs4 import BeautifulSoup as bs

def geeksforgeeks():
    r = requests.get("https://auth.geeksforgeeks.org/user/tharunbalaji31")
    soup = bs(r.content,"html.parser")
    total = soup.find("span", {"class": "score_card_value"})
    count = soup.find_all("li", {"class": "tab"})

    print("Total problems solved:",total.get_text())
    L = []
    for tags in count:
        s = tags.get_text()
        num = s[s.index('(')+1 : s.index(')')]
        L.append(num)

    print(L)

geeksforgeeks()