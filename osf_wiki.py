import requests

from config import OSF_NODE_ID, OSF_API_URL, OSF_TOKEN


class osfWiki():
    def __init__(self):
        self.wikis = self._retrieveWikis()

    def _retrieveWikis(self):
        page = 1
        more = True
        while more:
            data = self._retrieveWikisPage(page=page)
            if page == 1:
                resdata = data
            else:
                for d in data['data']:
                    resdata['data'].append(d)
            page = page + 1
            if data['links']['next'] == None:
                more = False
        return resdata

    def _retrieveWikisPage(self, page=1):
        headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
        res = requests.get(f'{OSF_API_URL}/nodes/{OSF_NODE_ID}/wikis/?page={page}', headers=headers)
        print(res.url)
        return res.json()

    def _getPageId(self, name):
        for page in self.wikis['data']:
            if page['attributes']['name'] == name:
                return page['id']
        return False

    def _getPageContent(self, id):
        headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
        res = requests.get(f'{OSF_API_URL}/wikis/{id}/content/', headers=headers)
        print(res.text)
        return res.text

    def _updatePage(self, id, content):
        headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
        data = {'content': content, 'type': 'wiki_versions'}
        res = requests.post(f'{OSF_API_URL}/wikis/{id}/versions/', headers=headers, data=data)
        return res.json()

    def _createPage(self, name, content):
        headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
        data = {'name': name, 'content': content, 'type': 'wikis'}
        res = requests.post(f'{OSF_API_URL}/nodes/{OSF_NODE_ID}/wikis/', headers=headers, data=data)
        return res.json()

    def setPageContent(self, name, content):
        id = self._getPageId(name)
        if id:
            print(f'Update page {name} with id {id}')
            res = self._updatePage(id, content)
        else:
            print(f'Create page {name}')
            res = self._createPage(name, content)
        return res
