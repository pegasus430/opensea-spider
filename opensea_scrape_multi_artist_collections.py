import requests
from bs4 import BeautifulSoup
import csv
import json

# url = "https://api.opensea.io/v2/listings/collection/slug/all"
# url = "https://api.opensea.io/v2/listings/collection/cool-cats-nft/all"

offset = 0
limit = 50
all_assets_count = 0

collections_url = "https://api.opensea.io/api/v1/collections?offset={}&limit={}"
collection_url = "https://api.opensea.io/api/v1/collection/{}"

headers = {
    "accept": "application/json",
    "X-API-KEY": "609c816a67654d2fa8413c364469a8c1"
}

multi_artist_collections = []
index = 0

proxy_url = '107.152.33.41:8080'
proxies = {
    'http': proxy_url,
    'https': proxy_url
}

output_file = 'opensea_multi_artist_collections.csv'

while True:
    response = requests.get(collections_url.format(offset, limit), headers=headers)

    if response.status_code == 200:
        index += 1
        collection_list = response.json()['collections']
        for collection in collection_list:
            # print(collection['name'], collection['slug'])
            response = requests.get(collection_url.format(collection['slug']))
            if response.status_code == 200:
                collection_info = response.json()['collection']
                asset_contracts = collection_info['primary_asset_contracts']

                if len(asset_contracts) > 1:
                    # with open(output_file, mode='a', newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerow([collection_info])
                    # exit()
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
                else:
                    print(index)
                    print("Getting the next collection")
                    break
            else:
                print("Error retrieving collection info")
                exit()
    else:
        print("Error retrieving collections")
        exit()
    offset += limit

    if len(collection_list) < limit:
        exit()

# headers = {
#     "accept": "application/json",
#     "X-API-KEY": "609c816a67654d2fa8413c364469a8c1"
# }

# response = requests.get(url, headers=headers)

# print(response.text)