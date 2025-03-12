import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.myschoolgist.com/ng/federal-government-unity-schools-in-nigeria/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
schools = soup.find_all('tr')

fgc = []

for school in schools[1:]:
    raw = school.find_all('td')
    row = [r.text.strip() for r in raw]
    if len(row)!=1:
        states=row[0].capitalize()
        sch=row[1]
        sc=sch.replace(',', '')
        fed=sc.replace(')', '),')
        school_list = [f.strip() for f in fed.split(",")]

        # gen = [s.split('(')[1] for s in school_list]
        # sex = gen.replace(")", '').capitalize()
        # gender = sex.replace('Boys & girls', 'Co-Educational')

        main = [{"state":states.strip(), "school":college} for college in school_list]
        fgc.append(main)

flat_gc = [item for sublist in fgc for item in sublist]
df=pd.DataFrame(flat_gc)
df = df[df['school'] != '']

df.to_csv('C:\\Users\\HP\\Desktop\\feddy-db\\webscraping-activities\\raw-fgc-data.csv')