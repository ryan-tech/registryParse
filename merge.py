# Download roster.xlsx from naqtc website
# Convert roster.xlsx to roster.csv
#

import csv, sys, operator
from datetime import datetime, date
def merge(rosterPath, olddbPath):
    old_database = olddbPath
    roster = rosterPath
    with open(old_database, 'r') as db, open(roster, 'r') as rstr, open('registry-1.csv', 'w') as outFile:
        header_columns = ['Firstname','Lastname','NAQTCID','SD','AG','AS','AE','R-66','C837','T40','T104','T190','T246','T283']
        old_db_csv = csv.DictReader(db, fieldnames=header_columns)
        combined_registry_buffer = rstr.readlines() #currently, registry is just the roster as a list of strings
        next(db)
        for old_db_row in old_db_csv:
            # for each row in the registry-unsorted.csv file, check if the entry matches an entry in the output buffer
            found = False

            for row in combined_registry_buffer:
                # Find the entry with matching ID's
                if row.split(',')[2] == old_db_row['NAQTCID']:
                    found = True
            if found is True:
                # if found, then merge the two
                # find the naqtcid again
                for row in combined_registry_buffer:
                    if row.split(',')[2] == old_db_row['NAQTCID']:
                        #make the modified row and append it to the combined_registry_buffer
                        line = row.split(',') #line from buffer, gonna be updating this variable then writing it to the buffer
                        combined_registry_buffer.remove(row)

                        for i in range(3, len(line)):
                            line[i] = line[i].rstrip()

                            """if (old_db_row['NAQTCID'] == 'NV001876'): #debugging
                                print(i)
                                print(line[i].rstrip())
                                print(old_db_row[header_columns[i]])
                                #end debugging
                            """
                            if old_db_row[header_columns[i]].rstrip() != '--' and line[i]== '--':
                                #(datetime.strptime(old_db_row[header_columns[i]], '%b-%d-%Y') >= datetime.strptime(line[i], '%b-%d-%Y')):
                                line[i] = old_db_row[header_columns[i]]

                        combined_registry_buffer.append(','.join(line) + '\n')
            else:
                # if not found, then just append that entry to the buffer
                row = []
                for i in header_columns:
                    row.append(old_db_row[i])
                combined_registry_buffer.append(','.join(row) + '\n')
        outFile.write(''.join(combined_registry_buffer))




"""
    We have all of the lines of the roster in the buffer. We need to add all the lines from the old database back into buffer.
    If a line from the old database has the same naqtcid from a line in the buffer, then combine the lines.
    else, add the line to the buffer
"""



def sort():
    data = csv.reader(open('registry-1.csv', 'r'), delimiter=',')
    headers = next(data, None)
    sortedlist = sorted(data, key=operator.itemgetter(1))  # 0 specifies according to first column we want to sort
    # now write the sorted result into new CSV file
    with open('registry-2.csv', "w") as f:
        fileWriter = csv.writer(f, delimiter=',')
        fileWriter.writerow(headers)
        for row in sortedlist:
            fileWriter.writerow(row)



def removeExp():
    # removes expired dates
    with open('registry-2.csv', 'r') as readFile:
        with open('registry-3.csv', 'w') as outFile:
            #readFile.readline()
            next(readFile)
            for line in readFile:
                line = line.split(',')
                for l in range(3,14):
                    line[l] = line[l].rstrip()
                    if line[l] != '--':
                        buffer = datetime.strptime(line[l], '%b-%d-%Y') #Feb-19-2024
                        if buffer >= datetime.today():
                            line[l] = buffer.strftime('%b-%d-%Y')
                        else:
                            line[l] = '--'
                line = ','.join(line)
                outFile.write(line+'\n')


def removeBlanks():
    with open('registry-3.csv', 'r') as f:
        with open('registry-final.csv', 'w') as r:
            r.write('Firstname,Lastname,NAQTC ID,Sampling and Density,Aggregate,Asphalt,Asphalt Extended,R-66,C837,T40,T104,T190,T246,T283\n')
            for line in f:
                if ',--,--,--,--,--,--,--,--,--,--,--' not in line:
                    r.write(line)


def runner(rosterPath, olddbPath):
    merge(rosterPath, olddbPath)
    sort()
    removeExp()
    removeBlanks()


if __name__ == "__main__":
    # merge() combines
    runner()

