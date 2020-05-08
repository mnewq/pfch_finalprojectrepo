#web scraping: https://www.theoi.com/greek-mythology/olympian-gods.html
#start with olympian gods, other categories if time

import requests
from bs4 import BeautifulSoup
import json

all_data = []
url = "https://www.theoi.com/greek-mythology/olympian-gods.html"

page_request_results = requests.get(url)
page_html = page_request_results.text

soup = BeautifulSoup(page_html, "html.parser")

all_divs = soup.find_all("div", attrs = {"class":"caption"})
#^printing this creates a list, so loop through it

for a_div in all_divs:

    all_ahref_in_div = a_div.find("a")
#turned fina_all into find
    title = all_ahref_in_div.text
    link = "https://www.theoi.com/" + all_ahref_in_div["href"]
#link = relative url

#create somewhere for data to go
    olympian_gods = {
        "name": title,
        "url": link
    }

    all_data.append(olympian_gods)

json.dump(all_data, open("olympian_gods.json", "w"), indent=2)
#print(all_data)

    #print(title,link)
#    print(all_ahref_in_div)
#    print("---")


#treat each god page like a search page from example? then write one loop script for that?
