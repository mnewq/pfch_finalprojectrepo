Untangling the family trees of Olympian gods:

When completed, this in-progress project aims to illustrate the overlapping and contradictory parentages of the Greek gods. In the lore and study of ancient Greek mythology, many classical sources have attributed deities’ parentage to a variety of other deities; it becomes almost impossible to keep track of how many variations of parentage a single member of the pantheon has, let alone which is the most commonly agreed upon by ancient historians and authors. By illuminating the connections, we move from the standard two-dimensional family tree with its alternative dotted lines to a model focusing on relativity that can be used as a reference guide for those wishing to untangle the pantheon.

The end result could be used by academics, students, researchers, and people with a general interest in Greek mythology who find the shifting family trees difficult to keep track of; as well as by educators and informational professionals to use the visualization itself to highlight lessons in information literacy to a general audience. What better way to underline the way fake news has always affected the way people interact with the world around them, and to encourage current students to search out multiple sources for fact-checking, than to show that some of the oldest products of human imagination were not agreed upon either?

All data has been scraped from Theoi.com and collected using Python scripts. The primary dataset came from the encyclopedia’s Olympian Gods section. The visualizations were made through MatPlotLib.

-----
To run the codes, follow this sequence:
1. pfch_final_webscrape.py
2. pfch_final_webscrape2.py (using olympian_gods.json)
3. pfch_final_csv2.py (using olympian_gods_details.json) --> this step can be skipped but I found it easier to have a separate script for use in the next step.
4. pfch_final_barchart2.py
