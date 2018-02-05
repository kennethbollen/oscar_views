import wikipedia
import re
import pandas as pd

oscar = wikipedia.page('Academy_Awards')

oscar_shows = []
oscar_edition = []

#collect all the links for the annual oscar shows
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
