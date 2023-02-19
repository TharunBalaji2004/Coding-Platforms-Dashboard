import requests
from bs4 import BeautifulSoup

def skillrack():
    url = "http://www.skillrack.com/profile/383836/f911a6f9b2a18fa90b25a6f0e7bc884dea66a139"

    r = requests.get(url)
    htmlcontent = r.content

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    # print(soup.prettify)

    # print(soup.find('div',class_ = 'value').get_text())

    L = soup.find_all('div',class_='value')

    d = {"RANK":"","LEVEL":"","GOLD MEDALS":"","SILVER MEDALS":"",
        "BRONZE MEDALS":"","TOTAL PROGRAMS SOLVED":"","CODE TEST":"",
        "CODE TRACK":"","DAILY CHALLENGES":"","DAILT TESTS":"","CODE TUTOR":"",
        "C":"","PYTHON3":"","JAVA":"","CPP17":"","SQL":""}

    scores = []
    for tag in L:
        temp = str(tag)
        temp = temp.split("</i>")
        temp = temp[-1]
        temp = temp.split("\n")
        scores.append(temp[0])

    i = 0

    for key in d.keys():
        d[key] = scores[i]
        i += 1

    print(d)
