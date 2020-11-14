### Project: Registry parser and merger
#### Author: Ryan Kim

This project is for merging two certification registries because of the database migration. I used these files to generate new registries by combining an old and current csv roster of students.

This code has since been retired and was modified to run on the web server.

1. Download the excel spreadsheet from the naqtc.cse.unr.edu website

2. Move the roster.xlsx to this directory

3. Convert the xlsx to csv using convert_xlsx_csv.py

4. There is a copy of the current registry (registry-sorted.csv) in the w2 server so go scp that

5. With the roster.csv and registry-sorted.csv in this directory execute: `$ python3 merge.py`

6. registry-final.csv is the document I would submit. This is what is displayed on `https://www.unr.edu/naqtc/qualified-technician-registry`