import csv

txt_file = r"students_updated.txt"
csv_file = r"students_updated.csv"

in_txt = csv.reader(open(txt_file, "r"), delimiter=',')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)