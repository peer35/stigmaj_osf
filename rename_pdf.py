import shutil
from bs4 import BeautifulSoup
import lxml
import requests

from config import PDF_PATH, CROSSREF_FILE, ROOT_URL


# http://stigmaj.org/article/download/45/pdf

with open(CROSSREF_FILE, encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "xml")
    doi_data = soup.find_all("doi_data")
    for d in doi_data:
        id = d.doi.string[8:len(d.doi.string)]
        print(id)
        f = d.resource.string[-2:]
        url = f'{ROOT_URL}/article/download/{f}/pdf'
        filename = f'{f}.pdf'
        print(url)
        r = requests.get(url, allow_redirects=True)
        open(f'{PDF_PATH}/{filename}', 'wb').write(r.content)
        old_name = f'{PDF_PATH}/{filename}'
        new_name = f'{PDF_PATH}/renamed/{id}.pdf'
        shutil.copy(old_name, new_name)
