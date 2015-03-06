import csv
reader = csv.reader(open('data.txt','r'),delimiter = ',')

print "{obervations:["
row_so_far = 0

for row in reader:
    row_so_far += 1

    print '{'
    print '"date": ' + '"' + row[0] + '",'
    print '"temperature": ' + row[1]

    if row_so_far < 365:
        print "},"
    else:
        print "}"

print "] }"
