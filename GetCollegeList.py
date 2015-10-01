from bs4 import BeautifulSoup
from requests import Session

with Session() as user:
    data = user.get('https://www.utexas.edu/world/univ/alpha/')
    html = BeautifulSoup(data.content)
    colleges = html.findAll(attrs={'class': 'institution'})
    for college in colleges:
        item = college.get_text().encode('ascii', 'ignore')
        with open('collegeList.txt', 'a') as entry:
            entry.write(item + "\n")






