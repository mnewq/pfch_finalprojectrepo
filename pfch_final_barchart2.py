# no of sources per god
import csv
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

df = pd.read_csv('god_details.csv')


god_names = df["name"]


left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

height = [5, 12, 7, 12, 2, 5, 10, 5, 5, 9, 5, 5, 3, 6, 2, 13, 7, 4, 6, 2, 4, 4, 2, 11, 4, 5, 1]
 #ideally some would be one lower--given time I would run an elif through the json file and exclude list results of "et al"
#I would also like to figure out to #counter rather than counting them manually, but I tihnk that has to be done in the json file, as they are part of a list within a dictionary within a list?

plt.bar(x = left, height = height, tick_label = god_names,
          width = 0.5, color = ['black'])

plt.xlabel('God Name')
plt.xticks(rotation=90)
plt.ylabel('No. of Sources')
plt.title('Number of Parentage Sources per Olympian God')

plt.show()
