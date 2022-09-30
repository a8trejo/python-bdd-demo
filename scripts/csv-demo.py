import csv
import os

print(os.getcwd())

# os.chdir('..')
# print(os.getcwd())

with open('../tdd/data.csv') as tddCsv:
    csv_reader = csv.reader(tddCsv, delimiter=',')
    csv_rows = list(csv_reader)
    print(csv_rows)
