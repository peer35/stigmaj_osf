import json

import requests
from config import OSF_NODE_ID, OSF_TOKEN, NAME_GUID_FILE, OSF_API_URL


def getOSFStorageFiles(url=False):
    headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
    if (url):
        res = requests.get(url, headers=headers)
    else:
        res = requests.get(f'{OSF_API_URL}/nodes/{OSF_NODE_ID}/files/osfstorage?format=json', headers=headers)
    print(res.url)
    return res.json()


def getFileById(id):
    # 5f28048b9c9094019048927f
    headers = {'Authorization': f'Bearer {OSF_TOKEN}'}
    res = requests.get(f' https://osf.io/{OSF_NODE_ID}/files/osfstorage/{id}/', headers=headers)
    print(res.url)


def _store(data, filename):
    '''
    Store the data dict as a json file

    :param data: dict
    :param filename: string
    :return:
    '''
    with open(filename, 'w') as f:
        json.dump(data, f, indent=1)


osf_api_data = getOSFStorageFiles()
next = True
data = []
while next:
    for d in osf_api_data['data']:
        if d['attributes']['kind'] == 'file':
            print(d)
            print(d['attributes']['name'])
            print(d['attributes']['guid'])
            if d['attributes']['guid'] == None:  # touch the file to generate a guid
                getFileById(d['id'])
            data.append({'name': d['attributes']['name'], 'guid': d['attributes']['guid']})
    if osf_api_data['links']['next'] != None:
        osf_api_data = getOSFStorageFiles(url=osf_api_data['links']['next'])
    else:
        next = False

_store(data, NAME_GUID_FILE)
