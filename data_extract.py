import bs4
import re
import pandas as pd

academy_shows = []

url = 'https://en.wikipedia.org/wiki/Academy_Awards'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text)

for link in soup.find_all('ul', href=True):
    if re.search('/wiki/*.*_Academy_Awards',links['href']) is not None:
        academy_shows.append(links['href'])

#clean data for the list of all the acadmey awards
for i in academy_shows:        
    for i in academy_shows:
        if i[:6] == '/wiki/':
            x = i.strip('/wiki/')
            academy_shows.remove(i)
            academy_shows.append(x)
    for i in academy_shows:
        if len(i) > 19:
            academy_shows.remove(i)

'''#collect all the links for the annual oscar shows
for i in oscar.links:
    if re.search('.th Academy Awards', i) is not None:
        oscar_shows.append(i)
    elif re.search('.st Academy Awards', i) is not None:
        oscar_shows.append(i)
    elif re.search('.rd Academy Awards', i) is not None:
        oscar_shows.append(i)
    elif re.search('.nd Academy Awards', i) is not None:
        oscar_shows.append(i)
    else:
        continue
        
#prep the data to be ordered
for i in oscar_shows:
    if len(i) == 18:
        oscar_edition.append(int(i[:1]))
    elif len(i) == 19:
        oscar_edition.append(int(i[:2]))
    else:
        continue

#create a dataframe of oscar data
oscars = pd.DataFrame({'oscar_number':oscar_edition,'oscar_show':oscar_shows})   
#sort the oscar data by edition number 
oscars = oscars.sort_values('oscar_number')

#loop through the oscar pages
for index, row in oscars.iterrows():
    edition = wikipedia.page(row['oscar_show'])'''
