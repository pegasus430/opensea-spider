import requests
from bs4 import BeautifulSoup
import csv
import json
import time

api_url = 'https://api.opensea.io/api/v1/assets?order_by={}&order_direction={}&offset={}&limit={}'
headers = {'Accept': 'application/json', 'X-API-KEY': '609c816a67654d2fa8413c364469a8c1'}

offset = 10000
limit = 50
all_assets_count = 0
artist_list = []
total_scrapped_count = 0

output_file = 'opensea_artists_new.csv'

while True:
    asset_list = []
    while True:
        response = requests.get(api_url.format('sale_date', 'desc', offset, limit), headers=headers)

        if response.status_code != 200:
            print('Request failed with status code', response.status_code)
            print('30 seconds delaying...')
            time.sleep(30)
            continue
        else:
            break
    
    print("Request was successful...", response.status_code)
    json_dict = json.dumps(response.json())

    if 'assets' not in json_dict:
        print('Finished fetching all NFT collections')
        break

    new_assets = response.json()['assets']
    all_assets_count += len(new_assets)
    print(f"Totally {all_assets_count} items scrapped...")

    for asset in new_assets:
        if asset['creator'] is None or asset['creator']['user'] is None or asset['creator']['user']['username']  is None:
            continue
        artist_name = asset['creator']['user']['username']
        collection_name = asset['collection']['name']

        if [artist_name, collection_name] not in asset_list:
            asset_list.append([artist_name, collection_name])
        else:
            continue
    
    for asset in asset_list:
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([asset])
    
    offset += limit

    if len(new_assets) < 0:
        break

print(f'Retrieved {all_assets_count} assets in total.')