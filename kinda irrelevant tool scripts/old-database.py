from datetime import datetime, date
import csv
with open('old_database.csv', 'r') as readFile:
    with open('old-database-formatted.csv', 'w') as outFile:

        #header_columns = ['Firstname','Lastname','NAQTCID','SD','AG','AS','AE','R-66','C837','T40','T104','T190','T246','T283']

        headers = ['Lastname','Firstname','Certi.Number','SD','R-66','AG','AGE','AS','ASE','T40','T40E']
        odb = csv.DictReader(readFile, fieldnames=headers)
        next(readFile)
        outputBuffer = ''
        for line in odb:

            outputLine = ''
            outputLine += line['Firstname'] + ','
            outputLine += line['Lastname'] + ','
            outputLine += line['Certi.Number'] + ','

            if line['SD'] != '--':
                if datetime.strptime(line['SD'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['SD'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            if line['AG'] != '--':
                if datetime.strptime(line['AG'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['AG'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            if line['AS'] != '--':
                if datetime.strptime(line['AS'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['AS'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            if line['ASE'] != '--':
                if datetime.strptime(line['ASE'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['ASE'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            if line['R-66'] != '--':
                if datetime.strptime(line['R-66'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['R-66'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            outputLine += '--,'  # c837

            if line['T40'] != '--':
                if datetime.strptime(line['T40'], '%b-%d-%Y') > datetime.today():
                    outputLine += line['T40'] + ','
                else:
                    outputLine += '--,'
            else:
                outputLine += '--,'

            outputLine += '--,' # t104
            outputLine += '--,'  # t190
            outputLine += '--,'  # t246
            outputLine += '--\n'  # t283
            #print(outputLine)
            outputBuffer += outputLine
        outFile.write(outputBuffer)