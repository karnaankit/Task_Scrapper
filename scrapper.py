from base64 import encode
from encodings import utf_8
import requests
import json


def parser():
    json_data = {}
    params = {
        'page': 0,
        'title': "प्रतिनिधि"
    }
    try:
        with open('results.json', encoding='utf-8') as f:
            json_data = json.load(f)
            title = json_data.get('data').get('title')
            page = json_data.get('data').get('page') + 1
    except:
        json_data["data"] = params
        json_data["data"]["articles"] = []
        json.dump(json_data, open('results.json', 'w'), indent=4)
        title = json_data.get('data').get('title')
        page = json_data.get('data').get('page') + 1
    temp_page = page
    while (page <= temp_page + 2):
        try:
            params['page'] = page
            params['title'] = title
            search = requests.get('https://bg.annapurnapost.com/api/search', params=params)
            data = search.json()

            if search.status_code == 200 and data['status'] == 'success':
                json_data["data"]['page'] = params['page']
                for i in data["data"]["items"]:
                    json_data["data"]["articles"].append(i)
                json.dump(json_data, open('results.json', 'w'), indent=4)
                print("Fetched page:", page, 'successfully')
                page = page + 1
                params['page'] = page
        except Exception as exc:
            print(exc)


if __name__ == '__main__':
    parser()
    print("Scraping complete")
