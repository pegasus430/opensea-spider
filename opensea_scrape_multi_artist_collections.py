import requests
from bs4 import BeautifulSoup
import csv
import json
import random
import time

offset = 50050
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
slugs_file = 'slugs.csv'

# session = requests.session()
slugs = []
while True:
    # proxy = random.choice(proxies)

    # session = requests.session()
    # session.proxies = proxy
    time.sleep(1)
    response = requests.get(collections_url.format(offset, limit), headers=headers)

    if response.status_code == 200:
        collection_list = response.json()['collections']
        for collection in collection_list:
            if collection['slug']:
                print(collection['slug'])
                with open(slugs_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([collection['slug']])
                slugs.append(collection['slug'])
                index += 1
            print(index)
            
            # response = session.get(collection_url.format(collection['slug']))

            # if response.status_code == 200:
            #     collection_info = response.json()['collection']
            #     asset_contracts = collection_info['primary_asset_contracts']

            #     if len(asset_contracts) > 1:
            #         artists = set()
            #         for contract in asset_contracts:
            #             artist_name = contract['artist_name']
            #             if artist_name:
            #                 artists.add(artist_name)
            #             print(artist_name)
            #             print(f"Name: {collection_info['name']}")
            #             print(f"The following artists are associated with {collection['slug']}:")
                        # with open(output_file, mode='a', newline='') as file:
                        #     writer = csv.writer(file)
                        #     writer.writerow([collection_info])
            #             exit()
            #     else:
            #         print(index)
            #         print("Getting the next collection")
            #         break
            # else:
            #     print("Error with collection")
            #     exit()
    else:
        print(index)
        print("Error retrieving collections")
        exit()
    offset += limit

    if len(collection_list) < limit:
        exit()