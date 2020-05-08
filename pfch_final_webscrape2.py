#for individual item metadata (1:07:45 time stamp in vid):
#open olympian_gods.json and load entries
#loop through each entry and download the html page
#parse each page with BS and pull out addt'l metadata
#add that metadata back into the json file and resave it

import requests
from bs4 import BeautifulSoup
import json

import csv

with open("olympian_gods.json", "r") as olympian_gods_json_file:
    olympian_gods = json.load(olympian_gods_json_file)

olympian_gods_details = []
with open("olympian_gods.csv", "w") as csv_out:
    godwriter = csv.writer(csv_out)

    for god in olympian_gods:
        #print(god["url"])
        url = god["url"]
        #need actual url ^
        page_request_results = requests.get(url)
        page_html = page_request_results.text
        soup = BeautifulSoup(page_html, "html.parser")

        parentage_refs = soup.find("span", attrs = {"class":"family-refs"})
        individual_ref = parentage_refs.text.split(", ")

        for each_ref in individual_ref:
            source = each_ref[0:-1]

    #        print(source)

        #print(parentage)
        godwriter.writerow([individual_ref])
        #godwriter.writerow([each_ref])

#
#
        parentage_dict = {
            "name" : god["name"],
        #"source" : individual_ref,
            "sources": source
            #"url" : god["url"]
            }
#have to break up individual_ref into own keys?

    #    olympian_gods_details.append(parentage_dict)

    #    json.dump(olympian_gods_details, open("olympian_gods_details.json", "w"), indent=2)

        #metadata = soup.find("span", attrs ={"class":"family-refs"})
        #^sources/references
