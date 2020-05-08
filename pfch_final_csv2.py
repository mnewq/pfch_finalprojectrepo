#ideally this would be folded into the webscrape2 script, but for clarity for visiualization, it was separated out
import json
import csv


with open('olympian_gods_details.json') as json_file:
    data = json.load(json_file)

# now we will open a file for writing
data_file = open('god_details.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for god in data:
    if count == 0:

        # Writing headers of CSV file
        header = god.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(god.values())

data_file.close()
