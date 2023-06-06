import requests
from bs4 import BeautifulSoup
import csv
import json

api_url = 'https://api.opensea.io/api/v1/assets?order_by={}&order_direction={}&offset={}&limit={}'
headers = {'Accept': 'application/json', 'X-API-KEY': '609c816a67654d2fa8413c364469a8c1'}

offset = 0
limit = 50
all_assets_count = 0
artist_list = []

output_file = 'opensea_artists.csv'

while True:
    response = requests.get(api_url.format('sale_date', 'desc', offset, limit), headers=headers)

    json_dict = json.dumps(response.json())
    if 'assets' not in json_dict:
        print('Finished fetching all NFT collections')
        break

    new_assets = response.json()['assets']
    all_assets_count += len(new_assets)

    asset_list = []
    
    for asset in new_assets:
        if asset['creator'] is None or asset['creator']['user'] is None or asset['creator']['user']['username']  is None:
            continue
        artist_name = asset['creator']['user']['username']
        asset_list.append(artist_name)
    
    unique_asset_list = list(set(asset_list))

    for asset in unique_asset_list:
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([asset])
    
    offset += limit

    if len(new_assets) < limit:
        break

print(f'Retrieved {all_assets_count} assets in total.')