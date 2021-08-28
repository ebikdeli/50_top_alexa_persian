import bs4
import requests
# import socket
# from urllib3 import ProxyManager

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
### URL = 'https://www.alexa.com/topsites/countries/IR'

### proxies = {'https': 'http://186.159.11.36:999'}

"""
req = requests.get('https://httpbin.org/ip', proxies=proxies)
print('with proxy: ', req.json())
req = requests.get('https://httpbin.org/ip')
print('without proxy: ', req.json())
"""
### req = requests.get(URL, proxies=proxies)

### print(req.status_code)
# print(req.content)
"""
with open('alexa_iran.txt', 'wb') as file:
    file.write(req.content)
"""


with open('alexa_iran.txt', 'r') as file:
    data = file.read()
soup = bs4.BeautifulSoup(data, 'html.parser')

all_links = soup.find_all('a')
with open('all_sites.txt', 'wt') as file:
    for link in all_links:
        file.write('\n')
        file.write(link['href'])





"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('165.227.33.90', 8081))
print(sock)
print(sock.send(b'Hello server'))
"""