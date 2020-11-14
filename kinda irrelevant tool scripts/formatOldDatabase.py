from datetime import datetime, date
import csv, operator

def addYears(d, years):
    try:
#Return same day of the current year
        return d.replace(year = d.year + years)
    except ValueError:
#If not same day, it will return other, i.e.  February 29 to March 1 etc.
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


filename = 'old-database.csv'
fields_o = 'StudentID,StudentName,Class,Pass,Genre,Type,ACI,Date,TestName'.split(',')
fields = ['Firstname','Lastname','NAQTCID','SD','AG','AS','AE','R-66','C837','T40','T104','T190','T246','T283'] #0 - 13
test_fields = ['','','','Sampling and Density', 'Aggregate', 'Asphalt', '', 'R-66','C837','T40','T104','T190','T246','T283']
bullshit = '{},{},{}, {},{},{}, {},{},{}, {},{},{}, {},{}'
with open(filename, 'r') as csvfile, open('old-database-unsorted.csv', 'w') as outFile:
    reader = csv.DictReader(csvfile, fieldnames=fields_o)
    next(reader)
    outputBuffer = []
    for row in reader:
        if row['Genre'] == 'Performance' and row['Pass'] == 'pass':

            found = False
            for out in outputBuffer:
                if out is not None:
                    if out[2] == 'NV' + row['StudentID'].zfill(6):
                        found = True
            if found:
                for out in outputBuffer:
                    if out is not None:
                        if out[2] == 'NV' + row['StudentID'].zfill(6):
                            #print(out, 1)
                            date = datetime.strptime(row['Date'], "%Y-%m-%d")
                            date = addYears(date, 5)

                            if date > datetime.today():
                                expdate = datetime.strftime(date, '%b-%d-%Y')
                                out[test_fields.index(row['TestName'])] = expdate
                                #print(expdate)
                                #print(out, 2)

            else:
                firstname = row['StudentName'].split(' ')[0]
                lastname = ' '.join(row['StudentName'].split(' ')[1: len(row['StudentName'].split(' '))]).rstrip()
                naqtcid = 'NV'+row['StudentID'].zfill(6)
                sd = '--'
                ag = '--'
                asp = '--'
                ae = '--'
                r66 = '--'
                c837 = '--'
                t40 = '--'
                t104 = '--'
                t190 = '--'
                t246 = '--'
                t283 = '--'
                date = datetime.strptime(row['Date'], "%Y-%m-%d")
                date = addYears(date,5)
                if date > datetime.today():
                    expdate = datetime.strftime(date, '%b-%d-%Y')
                    if row['TestName'] == 'Sampling and Density':
                        sd = expdate
                    elif row['TestName'] == 'Aggregate':
                        ag = expdate
                    elif row['TestName'] == 'Asphalt':
                        asp = expdate
                    elif row['TestName'] == 'R-66':
                        r66 = expdate
                    elif row['TestName'] == 'C837':
                        c837 = expdate
                    elif row['TestName'] == 'T40':
                        t40 = expdate
                    elif row['TestName'] == 'T104':
                        t104 = expdate
                    elif row['TestName'] == 'T190':
                        t190 = expdate
                    elif row['TestName'] == 'T246':
                        t246 = expdate
                    elif row['TestName'] == 'T283':
                        t283 = expdate
                output = [
                    firstname,
                    lastname,
                    naqtcid,
                    sd,
                    ag,
                    asp,
                    ae,
                    r66,
                    c837,
                    t40,
                    t104,
                    t190,
                    t246,
                    t283
                ]
                outputBuffer.append(output)

    #writing to the file
    for out in outputBuffer:
        noob = True
        for i in range(3,14):
            if out[i] != '--':
                noob = False
        if not noob:
            outFile.write(','.join(out)+'\n')


def sort():
    data = csv.reader(open('old-database-unsorted.csv', 'r'), delimiter=',')
    sortedlist = sorted(data, key=operator.itemgetter(2))  # 0 specifies according to first column we want to sort
    # now write the sorte result into new CSV file
    with open('old-database-formatted.csv', 'w') as f:
        fileWriter = csv.writer(f, delimiter=',')
        for row in sortedlist:
            fileWriter.writerow(row)

sort()