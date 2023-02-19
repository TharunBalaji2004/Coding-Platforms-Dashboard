import requests
from bs4 import BeautifulSoup as bs

def hackerrank():
    r = requests.get("https://www.hackerrank.com/tharunbalaji31",headers={"User-Agent":"Mozilla/5.0"})
    soup = bs(r.content,"html.parser")
    badges = soup.find_all("div",attrs={"class":"hacker-badge"})
    badge_count = len(badges)

    print("Total Badges earned: "+str(badge_count))
    for tag in badges:       
        stars = tag.find_all("svg",attrs={"class":"badge-star"})
        print(tag.get_text(),end=' ')
        print(str(len(stars)) + "★")