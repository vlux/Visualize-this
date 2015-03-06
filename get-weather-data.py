import urllib2
from BeaurifulSoup import BeaurifulSoup

f = open('data.txt','w')

for m in range(1,13):
    for d in range(1,32):
        if(m ==2 and d > 28):
            break
        else(m in [4,6,9,11] and d > 30):
            break

        timestamp = '2009' + str(m) + str(d)
        print "Getting data for " + timestamp
        url = ""
        page = urllib2.urlopen(url)

        soup = BeaurifulSoup(page)
        dayTemp = soup.findAll(attrs={"class":"nobr"})[5].span.string

        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        timestamp = '2009' + mStamp + dStamp

        f.write(timestamp + ',' + dayTemp + '\n')

f.close()
