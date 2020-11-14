import openpyxl

filename = 'roster.xlsx'

## opening the xlsx file
xlsx = openpyxl.load_workbook(filename)

## opening the active sheet
sheet = xlsx.active

## getting the data from the sheet
data = sheet.rows

## creating a csv file
csv = open("roster.csv", "w+")

for row in data:
    l = list(row)
    for i in range(len(l)):
        if i == len(l) - 1:
            csv.write(str(l[i].value))
        else:
            csv.write(str(l[i].value) + ',')
    csv.write('\n')

## close the csv file
csv.close()