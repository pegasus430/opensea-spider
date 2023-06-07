import requests
# from bs4 import BeautifulSoup
import csv
# import json
import random

offset = 0
limit = 50
all_assets_count = 0
multi_artist_collections = []
index = 0

collections_url = "https://api.opensea.io/api/v1/collections?offset={}&limit={}"
collection_url = "https://api.opensea.io/api/v1/collection/{}"

headers = {
    "accept": "application/json",
    "X-API-KEY": "609c816a67654d2fa8413c364469a8c1"
}

output_file = 'opensea_multi_artist_collections.csv'

session = requests.session()

proxies = [
    {'http': '180.183.120.117:8080', 'https': '180.183.120.117:8080'},
    {'http': '103.139.25.121:8080', 'https': '103.139.25.121:8080'},
    {'http': '47.243.124.21:3128', 'https': '47.243.124.21:3128'},
    {'http': '116.212.133.219:8080', 'https': '116.212.133.219:8080'},
    {'http': '103.106.219.141:8080', 'https': '103.106.219.141:8080'},
    {'http': '165.16.27.35:1981', 'https': '165.16.27.35:1981'},
    {'http': '154.236.189.19:1976', 'https': '154.236.189.19:1976'},
    {'http': '188.132.222.45:8080', 'https': '188.132.222.45:8080'},
    {'http': '213.136.101.40:3128', 'https': '213.136.101.40:3128'},
    {'http': '135.125.206.30:3128', 'https': '135.125.206.30:3128'},
    {'http': '181.57.216.110:999', 'https': '181.57.216.110:999'},
    {'http': '120.197.40.219:9002', 'https': '120.197.40.219:9002'},
    {'http': '138.118.104.50:999', 'https': '138.118.104.50:999'},
    {'http': '188.132.221.212:8080', 'https': '188.132.221.212:8080'},
    {'http': '177.93.45.154:999', 'https': '177.93.45.154:999'},
    {'http': '140.206.62.198:9002', 'https': '140.206.62.198:9002'},
    {'http': '8.213.129.15:8118', 'https': '8.213.129.15:8118'},
    {'http': '183.164.242.173:8089', 'https': '183.164.242.173:8089'},
    {'http': '134.209.29.120:8080', 'https': '134.209.29.120:8080'},
    {'http': '198.199.86.11:3128', 'https': '198.199.86.11:3128'},
    {'http': '41.77.129.154:53281', 'https': '41.77.129.154:53281'},
    {'http': '138.68.60.8:8080', 'https': '138.68.60.8:8080'}
]

while True:
    proxy = random.choice(proxies)
    
    print(proxy)
    session = requests.session()
    session.proxies = proxy
    response = session.get(collections_url.format(offset, limit), headers=headers)

    if response.status_code == 200:
        index += 1
        collection_list = response.json()['collections']
        for collection in collection_list:
            if collection['slug']:
                print(collection['slug'])

            session = requests.session()
            
            proxy = random.choice(proxies)
            print(proxy)
            session.proxies = proxy
            response = session.get(collection_url.format(collection['slug']))

            if response.status_code == 200:
                collection_info = response.json()['collection']
                asset_contracts = collection_info['primary_asset_contracts']

                if len(asset_contracts) > 1:
                    artists = set()
                    for contract in asset_contracts:
                        artist_name = contract['artist_name']
                        if artist_name:
                            artists.add(artist_name)
                        print(artist_name)
                        print(f"Name: {collection_info['name']}")
                        print(f"The following artists are associated with {collection['slug']}:")
                        with open(output_file, mode='a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([collection_info])
                        exit()
                else:
                    print(index)
                    print("Getting the next collection")
                    break
            else:
                print("Error with collection")
                exit()
    else:
        print("Error retrieving collections")
        exit()
    offset += limit

    if len(collection_list) < limit:
        exit()