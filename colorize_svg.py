import csv
from BeaurifulSoup import BeaurifulSoup

reader = csv.reader(open('data.txt','r'),delimiter =',')

svg = open('data.svg','r').read()

unemployment = {}
min_value = 100;
max_value = 0
for row in reader:
try:
    full_fips = row[1] + row[2]
    rate = float(row[8].strip())
    unemployment[full_fips] = rate
except:
    pass

soup = BeautifulSoup(svg,selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')

colors = [,,,]

for p in paths:
    if p['id'] not in ['State','separator']:
        # pass
try:
    rate = unemployment[p['id']]
except:
    continue
if rate > 10:
    color_class = 5
elif rate > 8:
    color_class = 4
elif rate > 6:
    color_class = 3
elif rate > 4:
    color_class = 2
elif rate > 2:
    color_class = 1
else:
    color_class = 0

color = colors[color_class]
p['style'] = path_style + color

print soup.prettify()
