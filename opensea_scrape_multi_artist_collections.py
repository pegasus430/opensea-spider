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

collection_url = "https://api.opensea.io/api/v1/collection/{}"

headers = {
    "accept": "application/json",
    "X-API-KEY": "609c816a67654d2fa8413c364469a8c1"
}

slugs_file = 'slugs.csv'
output_file = 'opensea_multi_artist_collections.csv'

slugs = []
i = 0

# with open(slugs_file, newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in reader:
#         slugs.append(row)

# Get the unique collection info
# slug = slugs[165]
# for slug in slugs:
# url = collection_url.format(slug[0])
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     collection_info = response.json()

#     if "primary_asset_contracts" in collection_info['collection']:
#         # collection = collection_info['collection']["primary_asset_contracts"]
#         collection = collection_info['collection']["editors"]
#     else:
#         print("There is no primary asset contract in this collection. Skipping...")
    
#     artist_set = set()
#     if len(collection) > 1:
#         print(f"The '{slug[0]}' collection has {len(collection)} different artists).")
#         # artist_set.add(slug[0])
#         with open('target.csv', mode='a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(slug[0])
#     else:
#         print(f"The '{slug[0]}' collection has only one artist.")
    # if "created_by" in collection:
    #     created_by = collection["created_by"]
    #     for artist in created_by:
    #         artist_set.add(artist["user"]["username"])
    #     if len(artist_set) > 1:
    #         print(f"The '{slug[0]}' collection has {len(artist_set)} different artists contributing to its assets.")
    #     elif len(artist_set) == 1:
    #         print(f"The '{slug[0]}' collection has only one artist.")
    #     else:
    #         print(f"///////No artist information found for the '{slug[0]}' collection.///////")
    # else:
    #     print(f"No artist information found for the '{slug[0]}' collection.")
# else:
#     print(f"Error requesting {url}. Status code: {response.status_code}")

# failed_attempts = 0

# for slug in slugs[21895:]:
#     i +=1
#     print(i)
#     print(slug[0])

#     if i % 20 == 0:
#         print("------------------- 3 Seconds Delaying------------------")
#         time.sleep(10)

#     url = collection_url.format(slug[0])
#     time.sleep(0.3)
#     response = requests.get(url, headers=headers)
    
    # if response.status_code == 429:
    #     failed_attempts += 1
    #     if failed_attempts == 30:
    #         exit()
#     if response.status_code == 200:
#         collection_info = response.json()

#         if "primary_asset_contracts" in collection_info['collection']:
#             # collection = collection_info['collection']["primary_asset_contracts"]
#             collection = collection_info['collection']["editors"]
#         else:
#             print("There is no primary asset contract in this collection. Skipping...")
        
#         artist_set = set()
#         if len(collection) > 1:
#             print(f"The '{slug[0]}' collection has {len(collection)} different artists).")
#             # artist_set.add(slug[0])
#             with open('target.csv', mode='a', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow([slug[0]])
#         else:
#             print(f"The '{slug[0]}' collection has only one artist.")
#     else:
#         print(f"Error requesting. Status code: {response.status_code}")

# Get the collection full name from slugs
target_slugs = []
with open('target.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        target_slugs.append(row)

for slug in target_slugs:
    url = collection_url.format(slug[0])
    # time.sleep(1)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        collection_info = response.json()

        if "name" in collection_info['collection']:
            collection_name = collection_info['collection']["name"]
            with open('opensea_multi_artist_collections.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([collection_name])
        else:
            print("There is no primary asset contract in this collection. Skipping...")
    else:
        print(f"Error occured.. {response.status_code}")
        exit()

        