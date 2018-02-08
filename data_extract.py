import bs4
import requests
import re
import pandas as pd

oscar_pages = []
oscar_shows = []

url = 'https://en.wikipedia.org/wiki/Academy_Awards'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text)

for link in soup.find_all('a', href=True, title=True):
	if re.search('. Academy Awards', link['title']) is not None:
		oscar_pages.append(link['href'])

#clean and upload
for i in range(len(oscar_pages)):
	if len(oscar_pages[int(i)]) > 25:
		del(oscar_pages[int(i)])
        
#remove the duplicates and create a numpy array
df_pages = pd.Series(oscar_pages)
df_shows = pd.Series(oscar_shows)
df_pages = df_pages.unique()
df_shows = df_shows.unique()





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
