from BeautifulSoup import BeautifulSoup

f = open('data.xml','r')
xml = f.read()

soup = BeautifulSoup(xml)
observations = soup.findAll('observation')

for o in observation:
    print o.date.string + ',' + o.max_temperatur.string
    
