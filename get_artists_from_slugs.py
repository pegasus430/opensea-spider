import requests
import csv
import time

headers = {
    "accept": "application/json",
    "X-API-KEY": "609c816a67654d2fa8413c364469a8c1"
}

request_url = "https://api.opensea.io/api/v1/assets?collection={}&order_direction=desc&offset=0&limit=20"

slugs = []
artists = []
total_artists_number = 0

def count_occurrences(my_list, element):
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    return count

with open('opensea_artists.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        slugs.append(row)

for slug in slugs:
    occurrences = count_occurrences(slugs, slug)
    if occurrences > 1:
        print(f"{slug} appears {occurrences} times in the list.")
        artists.append(slug[0])
    else:
        continue

total_artists_number = len(list(set(artists)))

for element in list(set(artists)):
   
   with open('opensea_artists_with_multicollection.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([element])

print(f"Total Artists number is {total_artists_number}")
