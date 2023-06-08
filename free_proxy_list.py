import requests
 
# use to parse html text
from lxml.html import fromstring 
from itertools import cycle
import traceback
 
 
def to_get_proxies():
    # website to get free proxies
    url = 'https://free-proxy-list.net/' 
 
    response = requests.get(url)
 
    parser = fromstring(response.text)
    # using a set to avoid duplicate IP entries.
    proxies = set() 
 
    for i in parser.xpath('//tbody/tr')[:10]:
 
        # to check if the corresponding IP is of type HTTPS
        if i.xpath('.//td[7][contains(text(),"yes")]'):
 
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
 
            proxies.add(proxy)
        return proxies
    
proxies = to_get_proxies()
 
# to rotate through the list of IPs
proxyPool = cycle(proxies) 
 
# insert the url of the website you want to scrape.
url = '' 
 
# for i in range(1, 11):
 
#     # Get a proxy from the pool
#     proxy = next(proxyPool)
#     print("Request #%d" % i)

print(proxyPool)
 
    # try:
    #     response = requests.get(url, proxies={"http": proxy, "https": proxy})
    #     print(response.json())
 
    # except:
       
    #     # One has to try the entire process as most
    #     # free proxies will get connection errors
    #     # We will just skip retries.
    # print("Skipping.  Connection error")