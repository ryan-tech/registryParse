import csv
from datetime import datetime
#I need to see who will be expiring for any of the modules for May 2020 and June 2020.
#I need the persons name, cert number and which module it is for i.e. Sampling density, etc.



with open('registry-final.csv', 'r') as readFile:
    next(readFile)
    headers = ['Firstname','Lastname','NAQTC ID','Sampling and Density', 'Aggregate', 'Asphalt', 'Asphalt Extended', 'R-66', 'C837', 'T40', 'T104', 'T190', 'T246', 'T283']
    data = csv.DictReader(readFile, fieldnames=headers)
    #print(headers)
    tests = ['Sampling and Density', 'Aggregate', 'Asphalt', 'Asphalt Extended', 'R-66', 'C837', 'T40', 'T104', 'T190', 'T246', 'T283']
    date_range_start = datetime(2020,5,1)
    date_range_end = datetime(2020,6,30)

    result = [[] for x in tests] # will store people who are expiring during the date range
    print(result)
    for row in data:
       for test in tests:
           if row[test] != '--':
               expDate = datetime.strptime(row[test], "%b-%d-%Y")
               if expDate >= date_range_start and expDate <= date_range_end:
                   result[tests.index(test)].append(row)



    for t in tests:
        print("=========================================")
        print("Test: " + t)
        for r in result[tests.index(t)]:
            print(r["Firstname"] + " " + r["Lastname"] + " " + r["NAQTC ID"])




