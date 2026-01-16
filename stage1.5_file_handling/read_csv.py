import csv

with open('new.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        if row:
            print(row)
