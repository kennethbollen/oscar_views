import wikipedia
import re

oscar = wikipedia.page('Academy_Awards')

oscar_shows = []

#collect all the links for the annual oscar shows
for i in oscar.links:
    if re.search('.th Academy Awards', i) is not None:
        oscar_shows.append(i)
    elif re.search('.st Academy Awards', i) is not None:
        oscar_shows.append(i)
    elif re.search('.rd Academy Awards', i) is not None:
        oscar_shows.append(i)
    else:
        continue
