import csv
reader = csv.reader(open('data.txt','r'),delimiter = ',')
print '<weather_data>'

for row in reader:
    print '<observation>'
    print '<date>' + row[0] + '</date>'
    print '<max_temperature>' + row[1] + '</max_temperature>'

print '</weather_data>'
