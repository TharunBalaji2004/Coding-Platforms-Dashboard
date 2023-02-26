import requests
from bs4 import BeautifulSoup as bs

def codechef():
    r = requests.get("https://www.codechef.com/users/r_a_h_u_l_kp")
    soup = bs(r.content,"html.parser")
    div_number = soup.find("div", {"class":"rating-header text-center"})
    div_number = div_number.find_all("div")
    L = []
    for tag in div_number:
        L.append(tag.get_text())
    rating = L[0]
    div = L[1][-2]
    star = L[2]
    print(rating,div,star)
    rating = str(L[0]).strip("?i\n    Provisional Rating, click to know more")
    print(rating)
codechef()