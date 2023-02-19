import requests
from bs4 import BeautifulSoup as bs

def leetcode():
    r = requests.get("https://leetcode.com/tharunbalaji31/")
    soup = bs(r.content,"html.parser")
    total = soup.find("div", {"class": "text-[24px] font-medium text-label-1 dark:text-dark-label-1"})
    tags = soup.find_all("span", {"class":"mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1"})
    rating = soup.find("div", {"class":"text-label-1 dark:text-dark-label-1 flex items-center text-2xl"})

    if (rating == None): rating = "Not Participated"
    else: rating = rating.get_text()

    easy = tags[0].get_text()
    medium = tags[1].get_text()
    hard = tags[2].get_text()

    print("Total problems solved: ",total.get_text())
    print("Easy problems solved: ",easy)
    print("Medium problems solved: ",medium)
    print("Hard problems solved: ",hard)
    print("Contest Rating:",rating)


