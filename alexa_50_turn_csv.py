import json
import requests
import bs4

sites = []

describe = dict()

## This block clean the list of '50 websites'
with open('alexa_50_result.txt') as file:
    websites = file.readlines()
for link in websites:
    sites.append(link.replace('\n', ''))

for site in sites:
    #if site == 'www.google.com':
    #    #describe[site] = 'موتور جست و جوی قدرتمند'
    #    pass
    #else:
    try:
        if site == 'www.iau.ac.ir':
            print('AZAD')
            r = requests.get(url='https://www.iau.ir/fa', timeout=10)
            print(r.status_code)
            describe[site] = 'وبسایت رسمی دانشگاه آزاد اسلامی'
            continue
        else:
            r = requests.get(url='https://' + site, timeout=10)

        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.content, 'html.parser')
            desc = soup.find_all('meta')
            i = 1
            for meta in desc:           
                try:
                    if meta['name'] == 'description':
                        describe[site] = meta['content']
                        break
                    elif i == len(desc):
                        title = soup.find('title').string
                        describe[site] = title
                        break
                    else:
                        i += 1
                except KeyError:
                    i += 1
                    #continue
        else:
            describe[site] = 'ACCESS RESTRICTED'

    except requests.ConnectionError:
        describe[site] = 'CONNECTION FAILED'
        continue
    except requests.Timeout:
        describe[site] = 'CONNECTION TIMEOUT'
        continue

    print(f'{site}  :  {describe[site]}')

with open('site_desc.json', 'wt', encoding='utf-8') as file:    
    json.dump(describe, file, ensure_ascii=False)

with open('site_desc.txt', 'wt', encoding='utf-8') as file:    
    json.dump(describe, file, ensure_ascii=False)
