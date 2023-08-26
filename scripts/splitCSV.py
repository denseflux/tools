import pandas as pd
import yaml
import html2markdown
from bs4 import BeautifulSoup
import datetime

""" Reading whole csv file with panda library """
df = pd.read_csv('./data/entries.csv')

""" iterate over each row """
for index, row in df.iterrows():

# keys:
# title
# summary
# author(s)
# categories
#   - os, categories, something
# links

    """ just grab the first row for testing """
    if index == 2:

        # todo
        # transformers: html to markdown
        # comma separated categories to list
        slug = row['slug']
        summaryHTML = BeautifulSoup(row['summary'])
        print(summaryHTML.p)
        row['summary'] = html2markdown.convert(str(summaryHTML.p))

        row['updated'] =         datetime.datetime.utcfromtimestamp(row['updated']/1000).strftime('%Y-%m-%d %H:%M:%S')
        """ Dump DataFrame into individual .md as yaml code """
        with open(f'./data/{slug}.md', 'w') as outfile:
            yaml.dump(
                row.to_dict(),
                outfile,
                sort_keys=False,
                width=72, 
                indent=4
            )
