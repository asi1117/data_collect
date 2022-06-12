import csv

path = 'C:/Users/Admi/Desktop/oculus/go/iteam_reviews/646891152077200.csv'
first = 0
with open(path, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            first += 1

print(first)