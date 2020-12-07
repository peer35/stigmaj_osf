import shutil
from bs4 import BeautifulSoup
import lxml
from config import CROSSREF_FILE, OSF_NODE_ID
from parsers import getGuid

with open(CROSSREF_FILE, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "xml")
    doi_data = soup.find_all("doi_data")
    for d in doi_data:
        id=d.doi.string[8:len(d.doi.string)]
        guid=getGuid(id)
        d.resource.string = f'https://osf.io/{OSF_NODE_ID}/wiki/{id}/'
        #collection = d.find('collection', {'property': 'crawler-based'})
        #collection.item.resource.string = f'https://osf.io/{guid}/'
        #collection = d.find('collection', {'property': 'text-mining'})
        #collection.item.resource.string = f'https://osf.io/{guid}/download/'

with open("output/crossref_osf.xml", "w", encoding='utf-8') as file:
    file.write(str(soup))

print(soup)
