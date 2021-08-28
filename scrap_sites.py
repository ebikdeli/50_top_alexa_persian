import re

matching = '[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

with open('all_sites.txt', 'r') as file:
    data_lines = file.read()

data = data_lines.split('\n')

all_hname_domain = []

with open('alexa_50_result.txt', 'w') as file:
    for line in data:
        if line.startswith('/siteinfo/'):
            line = line.replace('/siteinfo/', '')
            file.write('www.' + line)
            file.write('\n')
            # all_hname_domain.append(line)