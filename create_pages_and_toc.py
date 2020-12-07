from config import OSF_NODE_ID, DOAJ_FILE
from parsers import parseDoaj, getGuid
from osf_wiki import osfWiki
import time

wiki = osfWiki()

articles = parseDoaj(DOAJ_FILE)
print(articles)

TOC = ''
keywords = []
for a in articles:
    names = []
    authors_list = []
    for au in a['authors']:
        names.append(au['name'])
        authors_list.append(f"*{au['name']}*  \n{au['affiliation']}")
    author_block = '\n\n'.join(authors_list)
    id = a['doi'].string[8:len(a['doi'])]

    TOC = f"{TOC}\n\n [{a['title']}](https://osf.io/{OSF_NODE_ID}/wiki/{id}).\n {', '.join(names)}"

    article_md = f"## {a['title']}. ##  \n" \
                 f"Stigma Research and Action, [online], {a['date']}.  \n" \
                 f" doi: https://dx.doi.org/{a['doi']}\n\n" \
                 f"### Abstract ###\n{a['abstract']}\n\n" \
                 f"### Keywords: ###\n{', '.join(a['keywords'])}\n\n" \
                 f"### Full Text: ###\n[pdf](https://osf.io/{getGuid(id)})\n\n" \
                 f"### Authors ####\n{author_block}"

    with open(f"output/{id}.md", 'w', encoding="utf8") as f:
        f.write(article_md)
    wiki.setPageContent(name=id, content=article_md)
    for k in a['keywords']:
        if k not in keywords:
            keywords.append(k)

with open("output/TOC.md", 'w', encoding="utf8") as f:
    f.write(TOC)

print(",".join(keywords))
