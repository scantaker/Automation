import csv

FIRST_USERNAME = ''

with open('/Users/zhangsicai/Desktop/logincredential.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    column = [row['Username'] for row in reader]
    FIRST_USERNAME = column[0]

print(FIRST_USERNAME)