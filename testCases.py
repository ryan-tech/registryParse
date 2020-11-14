import csv
from datetime import datetime

with open('registry-unsorted.csv', 'r') as olddb, open('roster.csv', 'r') as roster, open('registry-final.csv', 'r') as registry:
    header_columns = ['Firstname', 'Lastname', 'NAQTCID', 'SD', 'AG', 'AS', 'AE', 'R-66', 'C837', 'T40', 'T104', 'T190',
                      'T246', 'T283']
    old_db_csv = csv.DictReader(olddb, fieldnames=header_columns)
    roster_csv = csv.DictReader(roster, fieldnames=header_columns)
    registry_csv = csv.DictReader(registry, fieldnames=header_columns)

    # skips headers

    #next(roster_csv, None)
    #next(registry_csv, None)

    sum_x = 0
    sum_y = 0

    # Test case 1:
    # all rows in old database are in the registry
    for old_db_row in old_db_csv:
        registry.seek(0)
        found = False

        for registry_row in registry_csv:
            # search the registry
            if registry_row['NAQTCID'] == old_db_row['NAQTCID']:
                # if the id's match then it's been found
                found = True
                # We also wanna check that all valid tests from the unsorted registry entry are found in the new registry
                for i in range(3, 14):
                    if old_db_row[header_columns[i]] != '--':
                        if registry_row[header_columns[i]] != old_db_row[header_columns[i]]:
                            if datetime.strptime(old_db_row[header_columns[i]], '%b-%d-%Y') >= datetime.today():
                                found = False
                                break

        if found is False:

            allExpired = True
            # check if it's not found because all of the person's tests expired
            for i in range(3, 14):
                if old_db_row[header_columns[i]] != '--':
                    if datetime.strptime(old_db_row[header_columns[i]], '%b-%d-%Y') >= datetime.today():
                        allExpired = False
                        break
            if not allExpired:
                print(old_db_row['NAQTCID'] + ' is missing from the registry. (old_db)')


    # test case 2:
    # checks all rows in new db to see if all entries are in the registry
    for roster_row in roster_csv:
        registry.seek(0)
        found = False
        for registry_row in registry_csv:
            if roster_row['NAQTCID'] == registry_row['NAQTCID']:
                found = True
                for i in range(3, 14):
                    if roster_row[header_columns[i]] != '--':
                        if registry_row[header_columns[i]] != roster_row[header_columns[i]]:
                            if datetime.strptime(old_db_row[header_columns[i]], '%b-%d-%Y') >= datetime.today():
                                found = False
        if found is False:
            print(roster_row['NAQTCID'] + ' is missing from the registry. (roster)')